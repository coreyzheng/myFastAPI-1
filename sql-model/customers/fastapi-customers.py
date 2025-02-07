from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Customer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    phone: str
    address: str
    email: str

sqlite_file_name = "sqllite_customers.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/customers/")
def create_customer(customer: Customer, session: SessionDep) -> Customer:
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


@app.get("/customers/")
def read_customers(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Customer]:
    customers = session.exec(select(Customer).offset(offset).limit(limit)).all()
    return customers

@app.get("/customers/{customer_id}")
def read_customer(customer_id: int, session: SessionDep) -> Customer:
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="customer not found")
    return customer

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="customer not found")
    session.delete(customer)
    session.commit()

    return {"ok": True}

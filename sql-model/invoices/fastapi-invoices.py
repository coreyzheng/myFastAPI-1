from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

from invoice import *


sqlite_file_name = "sqllite_invoices.db"
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


@app.post("/invoices/")
def create_invoice(invoice: Invoice, session: SessionDep) -> Invoice:
    session.add(invoice)
    session.commit()
    session.refresh(invoice)
    return invoice


@app.get("/invoices/")
def read_invoices(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Invoice]:
    invoices = session.exec(select(Invoice).offset(offset).limit(limit)).all()
    return invoices

@app.get("/invoices/{invoice_id}")
def read_invoice(invoice_id: int, session: SessionDep) -> Invoice:
    invoice = session.get(Invoice, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="invoice not found")
    return invoice

@app.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id: int, session: SessionDep):
    invoice = session.get(Invoice, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="invoice not found")
    session.delete(invoice)
    session.commit()
    return {"invoice deleted": True}

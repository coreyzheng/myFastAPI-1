from sqlmodel import Field, Session, SQLModel, create_engine, select

class Invoice(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_id: int
    product_id: int
    units: int
    amount: float
    invoice_date: str
    def __init__(self):
        print ("object invoice is initiated.")

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from settings import get_db
from schemas import ItemCreate, Item
from crud import create_item

app = FastAPI()

@app.post("/items/", response_model=Item)
def create_item_endpoint(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)
from fastapi import FastAPI
from supabase import create_client, Client
import os

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

@app.get("/")
def read_root():
    return {"Hello": "World"}

# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

class ProcessedData(BaseModel):
    original_name: str
    processed_name: str
    age_plus_10: int
    email_domain: str

# Подключение к БД
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD")
    )

@app.post("/api/process")
async def process_data(data: dict):
    try:
        # Обработка данных
        processed = {
            "original_name": data["Name"],
            "processed_name": data["Name"].upper(),
            "age_plus_10": data["Age"] + 10,
            "email_domain": data["Email"].split("@")[1]
        }
        
        # Сохранение в БД
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO processed_data (original_name, processed_name, age, email_domain) VALUES (%s, %s, %s, %s)",
            (processed["original_name"], processed["processed_name"], 
             processed["age_plus_10"], processed["email_domain"])
        )
        conn.commit()
        
        return {"status": "success", "processed_data": processed}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
import os
import time
from psycopg2 import OperationalError

app = FastAPI()

class ProcessedData(BaseModel):
    original_name: str
    processed_name: str
    age_plus_10: int
    email_domain: str

# Функция для создания таблицы
def create_table():
    max_retries = 5
    retry_delay = 3
    
    for attempt in range(max_retries):
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS processed_data (
                    id SERIAL PRIMARY KEY,
                    original_name VARCHAR(255) NOT NULL,
                    processed_name VARCHAR(255) NOT NULL,
                    age INTEGER NOT NULL,
                    email_domain VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            print("Таблица успешно создана или уже существует")
            return True
        except OperationalError as e:
            if attempt == max_retries - 1:
                print(f"Не удалось создать таблицу после {max_retries} попыток: {e}")
                return False
            print(f"Попытка {attempt + 1} не удалась, повтор через {retry_delay} сек...")
            time.sleep(retry_delay)

# Подключение к БД с повторами
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "postgres"),
        database=os.getenv("DB_NAME", "mydb"),
        user=os.getenv("DB_USERNAME", "postgres"),
        password=os.getenv("DB_PASSWORD", "password")
    )

# Создаем таблицу при старте приложения
@app.on_event("startup")
async def startup_event():
    print("Пытаемся создать таблицу...")
    create_table()

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
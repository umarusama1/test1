from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

PORT = int(os.getenv("PORT", 8000))
DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/live")
def live():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        return {"status": "Well done"}
    except Exception as e:
        return {"status": "Maintenance"}

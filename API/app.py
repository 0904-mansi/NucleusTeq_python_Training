from fastapi import FastAPI, HTTPException
from fastapi.responses import Response, JSONResponse
import asyncpg

app = FastAPI()

# PostgreSQL database connection settings
DATABASE_URL = "postgresql://postgres:password@localhost/api_test"

# Function to establish database connection
async def get_connection():
    return await asyncpg.connect(DATABASE_URL)

CREATE_TABLE_QUERY = """
   CREATE TABLE IF NOT EXISTS students (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100),
       age INT,
       gender VARCHAR(10),
       grade VARCHAR(10)
   );
"""

async def create_table(conn):
    await conn.execute(CREATE_TABLE_QUERY)

@app.on_event("startup")
async def startup_event():
    conn = await get_connection()
    await create_table(conn)
    await conn.close()

# POST Method
@app.post("/students/")
async def create_student(student: dict):
    conn = await get_connection()
    try:
        query = "INSERT INTO students (name, age, gender, grade) VALUES ($1, $2, $3, $4) RETURNING id"
        student_id = await conn.fetchval(query, student["name"], student["age"], student["gender"], student["grade"])
        return "Student added Successfully." , {"id": student_id}
    finally:
        await conn.close()

# GET Method
@app.get("/students/{student_id}")
async def read_student(student_id: int):
    conn = await get_connection()
    try:
        query = "SELECT id, name, age, gender, grade FROM students WHERE id = $1"
        student = await conn.fetchrow(query, student_id)
        if student:
            return dict(student)
        else:
            raise HTTPException(status_code=404, detail="Student not found")
    finally:
        await conn.close()

# Get all Students Method
@app.get("/students/")
async def read_all_students():
    conn = await get_connection()
    try:
        query = "SELECT * FROM students"
        students = await conn.fetch(query)
        return students
    finally:
        await conn.close()

# view JSON Data in localhost 
@app.get("/")
async def get_all_data():
    conn = await get_connection()
    try:
        query = "SELECT * FROM students"
        result = await conn.fetch(query)
        students = [dict(record) for record in result]
        return JSONResponse(content=students)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    finally:
        await conn.close()

# PUT Method
@app.put("/students/{student_id}")
async def update_student(student_id: int, student_update: dict):
    conn = await get_connection()
    try:
        query = """
            UPDATE students
            SET name = $1, age = $2, gender = $3, grade = $4
            WHERE id = $5
            RETURNING id
        """
        updated_student_id = await conn.fetchval(
            query, student_update["name"], student_update["age"], student_update["gender"], student_update["grade"], student_id
        )
        if updated_student_id:
            return {"id": updated_student_id}
        else:
            raise HTTPException(status_code=404, detail="Student not found")
    finally:
        await conn.close()

# DELETE Method
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    conn = await get_connection()
    try:
        query = "DELETE FROM students WHERE id = $1 RETURNING id"
        deleted_student_id = await conn.fetchval(query, student_id)
        if deleted_student_id:
            return {"id": deleted_student_id}
        else:
            raise HTTPException(status_code=404, detail="Student not found")
    finally:
        await conn.close()

# HEAD Method
@app.head("/students/{student_id}")
async def head_student(student_id: int):
    conn = await get_connection()
    try:
        query = "SELECT id FROM students WHERE id = $1"
        student = await conn.fetchval(query, student_id)
        if student:
            return Response(status_code=200)
        else:
            return Response(status_code=404)
    finally:
        await conn.close()

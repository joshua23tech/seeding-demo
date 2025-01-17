from pg8000.native import Connection 

def create_connection():
    db_conn = Connection(
        "joshuawork", 
        password="elmagico", 
        database="vehicles"
    )
    results = db_conn.run("SELECT * FROM cars;")
    for row in results:
        print(row)

if __name__ == "__main__":
    create_connection()
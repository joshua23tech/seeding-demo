from pg8000.native import Connection 

def create_connection():
    # Connect to the database
    db_conn = Connection(
        "joshuawork", 
        password="elmagico", 
        database="vehicles"
    )
    # Run an SQL query
    # results = db_conn.run("SELECT * FROM cars;")
    # Execute a loop over the iterable returned
    # for row in results:
        # print(row)
    
    # Close the connection to the database
    # db_conn.close()

    # will comment out the above to introduce new below
    return db_conn

if __name__ == "__main__":
    db = create_connection()
    db.close()
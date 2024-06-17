import psycopg2

try:
    conn = psycopg2.connect(db_url)
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")
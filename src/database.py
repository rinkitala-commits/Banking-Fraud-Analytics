from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///banking.db"

engine = create_engine(DATABASE_URL)

print("Database connection configured successfully.")
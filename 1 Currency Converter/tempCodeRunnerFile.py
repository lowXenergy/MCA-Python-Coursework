from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env

api_key = os.getenv("API_KEY")
db_host = os.getenv("DB_HOST")

print(api_key)
print(db_host)
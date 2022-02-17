import sqlite3
from domain.example import ContactRepository
from src.webserver import create_app
from src.domain.info import InfoRepository


database_path = "data/database.db"

repositories = {
    "info": InfoRepository(database_path),
    "contacts": ContactRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")

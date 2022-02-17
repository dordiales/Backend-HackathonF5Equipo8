import sqlite3
from domain.example import ExampleRepository
from src.webserver import create_app


database_path = "data/database.db"

repositories = {
    "examples": ExampleRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")

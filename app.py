import sqlite3
from domain.guide import ExampleRepository
from src.domain.experience import ExperienceRepository
from src.domain.guide import GuideRepository
from src.webserver import create_app


database_path = "data/database.db"

repositories = {
    "experiences": ExperienceRepository(database_path),
    "guides": GuideRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")

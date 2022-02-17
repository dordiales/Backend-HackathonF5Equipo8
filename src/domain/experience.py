import sqlite3


class Experience:
    def __init__(
        self, id, img, date, title, guideName, description, category, price, location
    ):
        self.id = id
        self.img = img
        self.date = date
        self.title = title
        self.guideName = guideName
        self.description = description
        self.category = category
        self.price = price
        self.location = location

    def to_dict(self):
        return {
            "id": self.id,
            "img": self.img,
            "date": self.date,
            "title": self.title,
            "guideName": self.guideName,
            "description": self.description,
            "category": self.category,
            "price": self.price,
            "location": self.location,
        }


class ExperienceRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            CREATE TABLE IF NOT EXISTS experiences (
                id INTEGER,
                img TEXT,
                date TEXT,
                title TEXT,
                guideName TEXT,
                description TEXT,
                category TEXT,
                price TEXT,
                location TEXT, 
                PRIMARY KEY(id)
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """SELECT * FROM experiences"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        result = []
        for item in data:
            experience = Experience(**item)
            result.append(experience)

        return result

    def save(self, experience):
        sql = """INSERT INTO experiences (id, img, date, title, guideName, description, category, price, location) VALUES (
            :id, :img, :date, :title, :guideName, :description, :category, :price, :location
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, experience.to_dict())
        conn.commit()

import sqlite3


class Guide:
    def __init__(self, id, img, name, valoration):
        self.id = id
        self.img = img
        self.name = name
        self.valoration = valoration

    def to_dict(self):
        return {
            "id": self.id,
            "img": self.img,
            "name": self.name,
            "valoration": self.valoration,
        }


class GuideRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            CREATE TABLE IF NOT EXISTS guides (
                id INTEGER,
                img TEXT,
                name TEXT,
                valoration INTEGER
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """SELECT * FROM guides"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        result = []
        for item in data:
            guide = Guide(**item)
            result.append(guide)

        return result

    def save(self, guide):
        sql = """insert into guides (id, img, name, valoration) values (
            :id, :img, :name, :valoration
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, guide.to_dict())
        conn.commit()

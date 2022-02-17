import sqlite3


class Example:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def to_dict(self):
        return {"data1": self.data1, "data2": self.data2}


class ExampleRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            CREATE TABLE IF NOT EXISTS examples (
                data1 varchar,
                data2 varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """SELECT * FROM examples"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        result = []
        for item in data:
            example = Example(**item)
            result.append(example)

        return result

    def save(self, example):
        sql = """insert into examples (data1, data2) values (
            :data1, :data2
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, example.to_dict())
        conn.commit()

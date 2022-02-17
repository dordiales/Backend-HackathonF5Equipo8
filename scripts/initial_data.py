import sys

sys.path.insert(0, "")


from src.domain.example import Example, ExampleRepository

database_path = "data/database.db"

example1 = Example(
    data1="exampledata",
    data2="anotherdata",
)
example2 = Example(
    data1="exampledata",
    data2="anotherdata",
)
example_repository = ExampleRepository(database_path)
example_repository.save(example1)
example_repository.save(example2)

print("base de datos inicializada en " + database_path)

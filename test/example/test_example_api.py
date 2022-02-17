from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.example import ExampleRepository, Example


def test_api_should_return_existing_examples():

    example_repository = ExampleRepository(temp_file())
    app = create_app(repositories={"examples": example_repository})
    client = app.test_client()

    example1 = Example(
        data1="exampledata1",
        data2="anotherdata",
    )
    example2 = Example(
        data1="exampledata2",
        data2="anotherdata",
    )
    example_repository.save(example1)
    example_repository.save(example2)

    response = client.get("/api/examples")

    assert response.json == [
        {
            "data1": "exampledata1",
            "data2": "anotherdata",
        },
        {
            "data1": "exampledata2",
            "data2": "anotherdata",
        },
    ]

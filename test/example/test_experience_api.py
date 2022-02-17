from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.experience import ExperienceRepository, Experience


def test_class_should_return_existing_Experiences():

    experience_repository = ExperienceRepository(temp_file())
    app = create_app(repositories={"experiences": experience_repository})
    client = app.test_client()

    experience1 = Experience(
        id=1,
        img="anotherdata",
        date="anotherdata",
        title="anotherdata",
        guideName="anotherdata",
        description="anotherdata",
        category="anotherdata",
        price="anotherdata",
        location="localexample",
    )
    experience2 = Experience(
        id=2,
        img="anotherdata",
        date="anotherdata",
        title="anotherdata",
        guideName="anotherdata",
        description="anotherdata",
        category="anotherdata",
        price="anotherdata",
        location="localexample",
    )
    experience_repository.save(experience1)
    experience_repository.save(experience2)

    response = client.get("/api/experiences")

    assert response.json == [
        {
            "id": 1,
            "img": "anotherdata",
            "date": "anotherdata",
            "title": "anotherdata",
            "guideName": "anotherdata",
            "description": "anotherdata",
            "category": "anotherdata",
            "price": "anotherdata",
            "location": "localexample",
        },
        {
            "id": 2,
            "img": "anotherdata",
            "date": "anotherdata",
            "title": "anotherdata",
            "guideName": "anotherdata",
            "description": "anotherdata",
            "category": "anotherdata",
            "price": "anotherdata",
            "location": "localexample",
        },
    ]

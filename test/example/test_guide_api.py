from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.guide import Guide, GuideRepository


def test_api_should_return_existing_guides():

    guide_repository = GuideRepository(temp_file())
    app = create_app(repositories={"guides": guide_repository})
    client = app.test_client()

    guide1 = Guide(id=1, img="anotherdata", name="Name", valoration=5)
    guide2 = Guide(id=2, img="anotherdata", name="Name", valoration=4)

    guide_repository.save(guide1)
    guide_repository.save(guide2)

    response = client.get("/api/guides")

    assert response.json == [
        {"id": 1, "img": "anotherdata", "name": "Name", "valoration": 5},
        {"id": 2, "img": "anotherdata", "name": "Name", "valoration": 4},
    ]

import connexion  # type: ignore
import logging
import time

from . import models

logger = logging.getLogger(__name__)


async def list_families() -> dict:
    result = models.FamilyListResponse(status=200, familyIds=[1, 2, 3, 4, 5])
    return result.model_dump()


async def get_family(familyId: int) -> dict:
    members = [
        models.FamilyPerson(personId=1, name="John"),
        models.FamilyPerson(personId=2, name="Jane"),
    ]
    result = models.FamilyResponse(status=200, familyId=familyId, members=members)
    return result.model_dump()


def main() -> None:
    app = connexion.AsyncApp(__name__)
    app.add_api(
        "openapi.yaml",
        strict_validation=True,
        validate_responses=True,
        swagger_ui=True,  # also works here
    )
    return app

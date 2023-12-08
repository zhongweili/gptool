from gptool.types.function import Function
from examples.video_search.src.functions.person.search_people.types import (
    FunctionInput,
    FunctionOutput,
    PersonSearchResult,
)
from tmdbv3api import Person

person = Person()


def search_people(params: FunctionInput) -> FunctionOutput:
    people_data = person.search(params.query)

    search_results = [
        PersonSearchResult(
            id=person["id"],
            name=person["name"],
            known_for_department=person["known_for_department"],
        )
        for person in people_data
    ]

    return FunctionOutput(search_results=search_results)


function = Function(
    function=search_people,
    description="Search for people by name.",
)

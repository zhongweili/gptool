from gptool.types.function import Function
from examples.video_search.src.functions.movie.get_popular_movies.types import (
    FunctionInput,
    FunctionOutput,
    MovieInfo,
)
from tmdbv3api import Movie

movie = Movie()


def get_popular_movies(params: FunctionInput) -> FunctionOutput:
    movies_data = movie.popular()
    print(movies_data)
    popular_movies = [
        MovieInfo(
            id=movie["id"],
            title=movie["title"],
            overview=movie["overview"],
            poster_path=movie["poster_path"],
        )
        for movie in movies_data[: params.limit]
    ]
    print(popular_movies)
    return FunctionOutput(popular=popular_movies)


function = Function(
    function=get_popular_movies,
    description="Get a list of popular movies.",
)

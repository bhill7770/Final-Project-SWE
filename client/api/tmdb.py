from flask import jsonify
import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
BASE_URL = "https://api.themoviedb.org/3/search/tv"
BASE_URL1 = "https://api.themoviedb.org/3/trending/tv/day"
BASE_URL2 = "https://api.themoviedb.org/3/tv"
PIC_URL = "https://image.tmdb.org/t/p/w200"
POSTER_SIZE = "w100"


def search_tv(query):

    query_params = {
        "api_key": os.getenv("TMDB_KEY"),
        "language": "en-US",
        "query": query,
    }

    response = requests.get(BASE_URL, params=query_params)

    data = response.json()
    # results = []
    # tv_shows = response.json()["results"]
    # for result in tv_shows:
    #     results.append(result["name"])
    #     results.append(result["poster_path"])
    # print(data)
    # poster_path = data["poster_path"]
    # poster_image = f"{PIC_URL}/{POSTER_SIZE}{poster_path}"
    # return (name, poster_image)
    return jsonify(results=data["results"])


# search_tv("snowpiercer")


def get_trending():
    new_params = {"api_key": os.getenv("TMDB_KEY")}
    # NEW_URL = BASE_URL1 + "?api_key=" + os.getenv("TMDB_KEY")
    # print(NEW_URL)

    response = requests.get(BASE_URL1, params=new_params)

    popular_data = response.json()

    # print(popular_data["results"])

    return jsonify(popular_data)


# get_trending()


def get_tv_detail(id):
    new_url = BASE_URL2 + "/" + id
    query_params = {
        "api_key": os.getenv("TMDB_KEY"),
        "language": "en-US",
    }
    response = requests.get(new_url, params=query_params)

    tv_details = response.json()

    return jsonify(tv_details)

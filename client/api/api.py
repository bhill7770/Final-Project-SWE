from crypt import methods
import flask
import os
from flask import Flask, jsonify

from imdb import search_movies, get_trending_movies, get_movie_detail
from tmdb import get_trending, search_tv, get_tv_detail
from books import search_books, get_book_detail
from wiki import get_best_sellers
from dbs import Users, UserProfile, Lists, ListItems, ListSharedWith, db

app = Flask(__name__)

uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = uri
# Gets rid of warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

# API Route
@app.route("/endpoint")
def index():
    # do stuff
    return {"names": ["Name1", "Name2", "Name3"]}


@app.route("/search", methods=["POST"])
def get_search():
    data = flask.request.get_json()
    query = data["query"]
    movie_results = search_movies(query)
    # tv_results = search_tv(query)

    return movie_results


@app.route("/search1", methods=["POST"])
def get_search1():
    data = flask.request.get_json()
    query = data["query"]
    tv_results = search_tv(query)
    # tv_results = search_tv(query)

    return tv_results


@app.route("/search2", methods=["POST"])
def get_search2():
    data = flask.request.get_json()
    query = data["query"]
    book_results = search_books(query)
    # tv_results = search_tv(query)

    return book_results


@app.route("/trending", methods=["GET"])
def trending():
    data = flask.request.get_json()
    trending_results = get_trending()
    # print(trending_results)
    return trending_results


@app.route("/trendingMovies", methods=["GET"])
def trending_movies():
    trending_movies = get_trending_movies()
    return trending_movies


@app.route("/bestSellers", methods=["GET"])
def best_selling_books():
    best_books = get_best_sellers()
    return best_books


# DB Calls to Handle Updates to a users Lists
@app.route("/getMyLists", methods=["POST"])
def get_my_lists():
    data = flask.request.get_json(force=True)
    my_lists = Lists.getUserLists(data["user_id"])
    return jsonify(my_lists)


@app.route("/addNewList", methods=["POST"])
def add_new_list():
    data = flask.request.get_json(force=True)
    user_id = data["user_id"]
    list_name = data["listName"]
    list_type = data["listType"]
    my_lists = Lists.addList(user_id, list_name, list_type, "")
    return jsonify(my_lists)


@app.route("/addNewItem", methods=["POST"])
def add_new_item():
    data = flask.request.get_json(force=True)
    list_id = data["list_id"]
    media_id = data["media_id"]
    my_item = ListItems.addListItem(list_id, str(media_id))
    return jsonify(my_item)


@app.route("/deleteList", methods=["POST"])
def delete_list():
    data = flask.request.get_json(force=True)
    list_id = data["list_id"]
    ret = Lists.deleteList(list_id)
    return jsonify(ret)


@app.route("/deleteItem", methods=["POST"])
def delete_item():
    data = flask.request.get_json(force=True)
    item_id = data["item_id"]
    ret = ListItems.deleteListItem(item_id)
    return jsonify(ret)


@app.route("/getMovieDetails", methods=["POST"])
def get_movie_details():
    data = flask.request.get_json(force=True)
    id = data["media_id"]
    movie_details = get_movie_detail(id)

    return movie_details


@app.route("/getTVDetails", methods=["POST"])
def get_tv_details():
    data = flask.request.get_json(force=True)
    id = data["media_id"]
    tv_details = get_tv_detail(str(id))

    return tv_details


@app.route("/getBookDetails", methods=["POST"])
def get_book_details():
    data = flask.request.get_json(force=True)
    id = data["media_id"]
    book_details = get_book_detail(id)

    return book_details


if __name__ == "__main__":
    app.run(debug=True)

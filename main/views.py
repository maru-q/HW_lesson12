from flask import Blueprint, render_template, request
from functions import search_posts_by_tag
import logging

logging.basicConfig(filename="info.log", level=logging.INFO)

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    s = request.args.get("s", "")
    posts = search_posts_by_tag(s)
    logging.info("Поиск по тегу осуществлен")
    return render_template("post_list.html", posts=posts, s=s)

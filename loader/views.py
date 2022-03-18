from flask import Blueprint, render_template, request
from functions import save_uploaded_picture, PictureWrongTipeError, add_post
from json import JSONDecodeError
import logging

logging.basicConfig(filename="exception.log", level=logging.exception(None))
logging.basicConfig(filename="info.log", level=logging.INFO)

load_blueprint = Blueprint("load_blueprint", __name__, template_folder="templates")


@load_blueprint.route("/post")
def load_post_page():
    return render_template("post_form.html")


@load_blueprint.route("/post", methods=["POST"])
def load_new_post_page():
    picture = request.files.get("picture", None)
    content = request.form.get("content", None)

    if not picture or not content:
        return "Данные не загружены, убедитесь, что все поля заполнены."

    try:
        picture_upload = save_uploaded_picture(picture)
    except PictureWrongTipeError:
        logging.info("Формат файла не поддерживатся")
        return "Формат файла не поддерживатся, допустимые форматы .jpg, .jpeg, .png"
    except FileNotFoundError:
        logging.exception("Ошибка загрузки файла")
        return "Ошибка загрузки файла"


    picture_url = "/"+picture_upload

    new_post = {"pic": picture_url, "content": content}

    try:
        new_posts = add_post(new_post)
    except FileNotFoundError:
        return "Нет доступа к файлу для записи данных"
    except JSONDecodeError:
        return "Ошибка чтения файла при записи"

    return render_template("post_uploaded.html", picture_url=picture_url, content=content)




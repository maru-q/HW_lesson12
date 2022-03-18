import json
from json import JSONDecodeError


POST_PATH = "posts.json"


def load_posts_from_json():
    """
    Возвращает все посты
    :return: posts
    """
    try:
        with open(POST_PATH, "r", encoding="utf-8") as file:
            posts_list = json.load(file)
        return posts_list
    except FileNotFoundError:
        raise FileNotFoundError
    except JSONDecodeError:
        raise JSONDecodeError


def search_posts_by_tag(tag):
    """
    Поиск постов по тегу
    :param: tag
    :return: post_found
    """
    post_found = []
    posts = load_posts_from_json()
    for post in posts:
        if tag.lower() in post["content"].lower():
            post_found.append(post)
    return post_found


class PictureWrongTipeError(Exception):
    pass


def save_uploaded_picture(picture):
    """
    Сохраняет картинку
    :param picture:
    :return: путь к файлу
    """
    filename = picture.filename

    file_type = filename.split(".")[-1]

    if file_type.lower() not in ["jpg", "jpeg", "png"]:
        raise PictureWrongTipeError

    picture.save(f"./uploads/images/{filename}")

    return f"uploads/images/{filename}"


# def add_post_to_feed(post):
#     posts = load_posts_from_json()
#     posts.append(post)
#

def add_post(post):
    """
    Добавляет пост в список постов JSON
    :param post:
    :return: -
    """
    data = load_posts_from_json()
    data.append(post)
    try:
        with open(POST_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    except FileNotFoundError:
        raise FileNotFoundError





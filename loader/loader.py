from flask import Blueprint, render_template, request
import logging
from loader.utils import save_picture
from main.utils import Post

POST_PATH = "posts.json"

loader_blueprint = Blueprint('loader_blueprint', __name__,template_folder='templates')
logging.basicConfig(filename='base.log', level=logging.INFO)

@loader_blueprint.route('/post', methods=["GET"])
def page_post_form():
    return render_template("post_form.html")

@loader_blueprint.route('/post', methods=["POST"])
def page_post():
    picture = request.files.get("picture")
    content = request.form["content"]

    if not picture or not content:
        return "Упс... Вы что-то пропустили"

    file_path = save_picture(picture)
    if not file_path:
        logging.info("Неверный формат файла")
        return "Неверный формат файла"
    post = Post(POST_PATH)

    new_post = {'pic': file_path,'content': content}
    post.add_post(new_post)

    return render_template('post_uploaded.html', file_path=file_path, content=content)

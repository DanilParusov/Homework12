from flask import Blueprint, render_template, request
from main.utils import Post
import logging

POST_PATH = "posts.json"

main_blueprint = Blueprint('catalog_blueprint', __name__,template_folder='templates')
logging.basicConfig(filename='base.log', level=logging.INFO)

@main_blueprint.route('/')
def catalog_page():
    return render_template("index.html")

@main_blueprint.route('/search')
def search_page():
    post = Post(POST_PATH)
    word = request.args['s']
    logging.info(f"Поиск: {word}")
    posts = post.get_posts_by_word(word)
    return render_template("post_list.html", posts=posts, word=word)
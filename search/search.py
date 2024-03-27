from flask import Blueprint,request,render_template
from functions import get_json_read,search_file
search_blueprint = Blueprint("search_blueprint", __name__, template_folder='templates')
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="UTF-8")

@search_blueprint.route('/search')
def get_search():
    word = request.values.get('s')
    logging.info(f"Был сделан запрос по слову {word}")
    file = get_json_read('posts.json')
    articles = search_file(word, file)
    return render_template('post_list.html', articles=articles)

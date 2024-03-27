from flask import Blueprint, request, render_template
from functions import write_file
import logging

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder='templates')
logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="UTF-8")

@loader_blueprint.route('/post', methods = ["GET"])
def get_load():
    return render_template("post_form.html")


@loader_blueprint.route('/post', methods = ["POST"])
def post_load():
    img = request.files.get('picture')

    if not img:
        return "Ошибка загрузки"



    filename = img.filename
    if filename.split(".")[-1] not in ['png','jpg']:
        logging.info("Загружаемый файл не картинка")
        return "Не правильное расширение файла. Файл должен быть *.jpg или *.png"
    path_img = f"static/uploads/{filename}"
    img.save(path_img)
    text = request.values.get('content')
    write_file("posts.json", path_img, text)

    return render_template("post_uploaded.html", img = '../../' + path_img, text = text)

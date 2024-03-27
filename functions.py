import json

def get_json_read(path):
    file = open(path, encoding="UTF-8")
    file = json.load(file)
    return file

def search_file(word,file):
    res = []

    for article in file:
        if word in article['content']:
            res.append(article)
    return res

def write_file(file, path,text):
    update_file = {
        "pic": path,
        "content": text,
    }

    with open(file, "r", encoding="UTF-8") as files:
        data = json.load(files)
    data.append(update_file)
    with open(file, 'w', encoding="UTF-8") as f:
        json.dump(data,f,ensure_ascii=False)

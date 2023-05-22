import os

from flask import Flask, render_template, request, redirect
from custom_md_to_html import *

port = 20011

app = Flask(__name__)

global files
files = []

def explore_path(path: str):
    global files
    if os.path.isfile(path):
        items = path.split("/")
        files.append({"path": path, "name": items[len(items)-1]})
        return files
    else:
        for item in os.listdir(path):
            if os.path.isfile(os.path.join(path, item)):
                files.append({"path": os.path.join(path, item), "name": item})
                continue
            elif os.path.isdir(os.path.join(path, item)):
                explore_path(path = os.path.join(path, item))
            else:
                print("   Error : Can't load", item, "from", path)
    
    return files

@app.route('/')
def index():
    return render_template('index.html', title="Accueil", stylesheet='index')

@app.route('/theme/<theme>')
def set_theme(theme):
    response = redirect('/')
    response.set_cookie('page_theme', theme)
    return response

@app.route('/faq')
def faq():
    return render_template('faq.html', title="FAQ", stylesheet='faq')

@app.route('/ressources')
def ressources():
    global files
    files = [   ]
    explore_path(os.path.join("static", "ressources"))
    
    return render_template('ressources.html', title="Ressources", stylesheet='ressources', files=files)

@app.route('/presentation', methods=['GET'])
def presentation():
    files_n_titles = creates_pages()
    
    if request.args.get("page") in [file[1] for file in files_n_titles]:
        file = f'/pages/{[file[0] for file in files_n_titles if file[1] == request.args.get("page")][0]}'
        return render_template('presentation.html', is_arg=True, title=request.args.get("page"), stylesheet='presentation', file_name=file)
    
    return render_template('presentation.html', is_arg=False, title='Présentation', stylesheet='presentation', files_n_titles=files_n_titles)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
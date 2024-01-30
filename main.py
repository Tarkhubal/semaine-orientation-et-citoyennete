import os

from flask import Flask, render_template, request, redirect, jsonify
from custom_md_to_html import *

port = 20054

app = Flask(__name__)

global files
files = []

global allowed_ips
allowed_ips = [i.replace("\n", "") for i in open("allowed_ips.txt", "r", encoding="utf-8").readlines() if i not in ("\n", "\t")]

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


@app.route('/writers')
def index_writers():
    if request.remote_addr in allowed_ips:
        return redirect("/writers/editor")
    return render_template('/writers/index.html', title="Accès en tant qu'écrivain", stylesheet="index")


@app.route('/writers/editor')
def writers_editor():
    if request.remote_addr in allowed_ips:
        return render_template('/writers/editor.html', title="Editeur de pages", stylesheet="writers")
    return render_template('/writers/index.html', title="Accès en tant qu'écrivain", stylesheet="index")


@app.route('/api/v1/writers/check_pass')
def _api_v1_writers_check_pass():
    global allowed_ips

    if request.args.get("pswd") == "root":
        if request.remote_addr not in allowed_ips:
            allowed_ips.append(request.remote_addr)
            open("allowed_ips.txt", "w", encoding="utf-8").writelines(allowed_ips)
        
        print("Access granted for", request.remote_addr)
        print(allowed_ips)
        return redirect("/writers/editor")
    elif request.remote_addr in allowed_ips:
        return redirect("/writers/editor")
    else:
        print("Non-authorized access", request.remote_addr)
        return redirect("/")


@app.route('/api/v1/custom_md/to_html', methods=['GET', 'POST'])
def _api_v1_custom_md_to_html():
    if request.remote_addr not in allowed_ips:
        return jsonify({"error_code": 403, "description": "Forbidden"})
    
    if request.method == 'POST':
        # Assurez-vous que la requête est de type JSON
        if request.is_json:
            data = custom_md_to_html(string=str(request.get_json()["text"]))
            return jsonify({"error_code": 200, "description": "Success", "data": f"{data[1]}<br>{data[0]}"})

        return jsonify({"error_code": 400, "description": "Bad Request"})

    # Si la méthode est GET, vous pouvez gérer cela ici si nécessaire
    return jsonify({"error_code": 405, "description": "Method Not Allowed"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
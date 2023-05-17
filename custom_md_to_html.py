import os

def custom_md_to_html(md_link: str):
    """Converts a markdown file into HTML and returns it as a string and the title of the page."""
    md_lines = open(md_link, "r", encoding="utf-8").readlines()
    html = ""
    
    for line in md_lines:
        if line.startswith("<<-- "):
            continue
        if line.startswith("# "):
            title = line[2:-1]
            if html == "" or html == "<br>":
                continue
            else:
                html += f"<h1>{line[2:]}</h1>"
                continue
        elif line.startswith("## "):
            html += f'<h2>{line[3:]}</h2>'
            continue
        elif line.startswith("### "):
            html += f"<h3>{line[4:]}</h3>"
            continue
        elif line.startswith("#### "):
            html += f"<h4>{line[5:]}</h4>"
            continue
        elif line.startswith("##### "):
            html += f"<h5>{line[6:]}</h5>"
            continue
        
        elif line.startswith("img:["):
            img, alt = line[5:-2].split("]{")
            html += f"<img src='/{img}' alt='Image de : {alt}'>"
            html += f"<p class='img_sub'>{alt}</p>"
            continue
        
        elif line.startswith("link:["):
            link, text = line[6:-2].split("]{")
            html += f"<a href='{link}'>{text}</a>"
            continue
        
        elif line == "\n":
            if html.endswith("<br>"):
                continue
            else:
                html += "<br>"
                continue
        
        else:
            html += f'<p>{line}</p>'
            continue
    
    return html, title

def creates_pages() -> int:
    """Creates the pages in the /static/pages/ folder and return the number of pages created and a list of tuples containing the name of the file and the title of the page."""
    files_n_titles = []
    for page in os.listdir("./pages"):
        if page.endswith(".md"):
            html, title = custom_md_to_html("./pages/" + page)
            page_name = page[:-3] + ".html"
            
            html_file = open("./templates/pages/" + page_name, "w", encoding="utf-8")
            html_file.write(html)
            html_file.close()
            
            files_n_titles.append((page_name, title))
    
    return files_n_titles
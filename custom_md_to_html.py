import os


# colors
colors = {
    "red": "#ff0000",
    "green": "#00ff00",
    "blue": "#0000ff",
    "yellow": "#ffff00",
    "purple": "#ff00ff",
    "cyan": "#00ffff",
    "white": "#ffffff",
    "black": "#000000",
    "gray": "#808080",
    "grey": "#808080",
    "orange": "#ffa500",
    "brown": "#a52a2a",
    "pink": "#ffc0cb",
    "gold": "#ffd700",
    "silver": "#c0c0c0",
    "bronze": "#cd7f32",
    "indigo": "#4b0082",
    "violet": "#ee82ee",
    "magenta": "#ff00ff",
    "lime": "#00ff00",
    "olive": "#808000",
    "teal": "#008080",
    "navy": "#000080",
    "maroon": "#800000",
    "crimson": "#dc143c",
    "coral": "#ff7f50",
    "salmon": "#fa8072",
    "beige": "#f5f5dc",
    "ivory": "#fffff0",
    "khaki": "#f0e68c",
    "lavender": "#e6e6fa",
    "plum": "#dda0dd",
    "snow": "#fffafa",
    "tan": "#d2b48c",
    "wheat": "#f5deb3",
    "azure": "#f0ffff",
    "bisque": "#ffe4c4",
    "chocolate": "#d2691e",
    "fuchsia": "#ff00ff",
    "gainsboro": "#dcdcdc",
    "ghostwhite": "#f8f8ff",
    "honeydew": "#f0fff0",
    "indianred": "#cd5c5c",
    "lavenderblush": "#fff0f5",
    "lawngreen": "#7cfc00",
    "lemonchiffon": "#fffacd",
    "lightblue": "#add8e6",
    "lightcoral": "#f08080",
    "lightcyan": "#e0ffff",
    "lightgoldenrodyellow": "#fafad2",
    "lightgray": "#d3d3d3",
    "lightgrey": "#d3d3d3",
    "lightgreen": "#90ee90",
    "lightpink": "#ffb6c1",
    "lightsalmon": "#ffa07a",
    "lightseagreen": "#20b2aa",
    "lightskyblue": "#87cefa",
    "lightslategray": "#778899",
    "lightslategrey": "#778899",
    "lightsteelblue": "#b0c4de",
    "lightyellow": "#ffffe0",
    "mediumaquamarine": "#66cdaa",
    "mediumblue": "#0000cd",
    "mediumorchid": "#ba55d3",
    "mediumpurple": "#9370db",
    "mediumseagreen": "#3cb371",
    "mediumslateblue": "#7b68ee",
    "mediumspringgreen": "#00fa9a",
    "mediumturquoise": "#48d1cc",
    "mediumvioletred": "#c71585",
    "midnightblue": "#191970",
    "mintcream": "#f5fffa",
    "mistyrose": "#ffe4e1",
    "moccasin": "#ffe4b5",
    "oldlace": "#fdf5e6",
    "olivedrab": "#6b8e23",
    "orangered": "#ff4500",
    "orchid": "#da70d6",
    "palegoldenrod": "#eee8aa",
    "palegreen": "#98fb98",
    "paleturquoise": "#afeeee",
    "palevioletred": "#db7093",
    "papayawhip": "#ffefd5",
    "peachpuff": "#ffdab9",
    "peru": "#cd853f",
    "powderblue": "#b0e0e6",
    "rosybrown": "#bc8f8f",
    "royalblue": "#4169e1",
    "saddlebrown": "#8b4513",
    "seagreen": "#2e8b57",
    "seashell": "#fff5ee",
    "sienna": "#a0522d",
    "skyblue": "#87ceeb",
    "slateblue": "#6a5acd",
    "slategray": "#708090",
    "slategrey": "#708090",
    "springgreen": "#00ff7f",
    "steelblue": "#4682b4",
    "thistle": "#d8bfd8",
    "tomato": "#ff6347",
    "turquoise": "#40e0d0",
    "whitesmoke": "#f5f5f5",
    "yellowgreen": "#9acd32"
}

def custom_md_to_html(md_link: str = None, string: str = None):
    """Converts a custom markdown file into HTML and returns it as a string and also get the title of the page."""
    md_lines = []
    if md_link is not None:
        md_lines = open(md_link, "r", encoding="utf-8").readlines()
    else:
        for line in string.split("\n"):
            md_lines.append(line + "\n")
            # print(line)
    
    html = ""
    global colors
    
    for line in md_lines:
        for loop in range(line.count(":color:")):
            color = line.split(":color:")[1].split("::-")[0]
            if color in colors.keys():
                line = line.replace(f":color:{color}::-", f"<span style='color: {colors[color]};'>")
            else:
                line = line.replace(f":color:{color}::-", f"<span>")
        
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
            if not img.startswith("/") and not img.startswith("http"):
                img = f"/{img}"

            html += f"<img src='{img}' alt='Image de : {alt}'>"
            html += f"<p class='img_sub'>\u2014\u0020{alt}</p>"
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
    
    html = html.replace("**-", "<strong>").replace("-**", "</strong>")
    html = html.replace("_-", "<em>").replace("-_", "</em>")
    html = html.replace("~~-", "<del>").replace("-~~", "</del>")
    html = html.replace("```-", "<code>").replace("-```", "</code>")
    html = html.replace("^^-", "<sup>").replace("-^^", "</sup>")
    html = html.replace(",,-", "<sub>").replace("-,,", "</sub>")
    html = html.replace("==-", "<mark>").replace("-==", "</mark>")
    html = html.replace("++-", "<ins>").replace("-++", "</ins>")
    html = html.replace("<<--", "<!--").replace("-->>", "-->")
    
    html = html.replace("**/-", "**-").replace("-/**", "-**")
    html = html.replace("_/-", "_-").replace("-/_", "-_")
    html = html.replace("~~/-", "~~-").replace("-/~~", "-~~")
    html = html.replace("```/-", "```-").replace("-/```", "-```")
    html = html.replace("^^/-", "^^-").replace("-/^^", "-^^")
    html = html.replace(",,/-", ",,-").replace("-/,,", "-,,")
    html = html.replace("==/-", "==-").replace("-/==", "-==")
    html = html.replace("++/-", "++-").replace("-/++", "-++")
    html = html.replace("<</--", "<<--").replace("--/>>", "-->>")
    
    html = html.replace("-:color", "</span>").replace(":/:-", "::-").replace(":color/:", ":color:").replace("-:/color", "-:color")
    
    return html, title

def creates_pages() -> int:
    """Creates the pages in the /static/pages/ folder and return the number of pages created and a list of tuples containing the name of the file and the title of the page."""
    files_n_titles = []
    for page in os.listdir("./pages"):
        if page.endswith(".md") or page.endswith(".txt"):
            html, title = custom_md_to_html("./pages/" + page)
            if page.endswith(".md"):
                cut = 3
            else:
                cut = 4
            
            page_name = page[:-cut] + ".html"
            
            html_file = open("./templates/pages/" + page_name, "w", encoding="utf-8")
            html_file.write(html)
            html_file.close()
            
            files_n_titles.append((page_name, title))
    
    return files_n_titles
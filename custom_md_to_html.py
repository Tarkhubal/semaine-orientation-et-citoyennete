def custom_md_to_html(md_link: str):
    """Converts a markdown file into HTML and returns it as a string."""
    md_lines = open(md_link, "r").readlines()
    html = ""
    
    for line in md_lines:
        if line.startswith("# "):
            html += f"<h1>{line[2:]}</h1>"
            continue
        if line.startswith("## "):
            html += f"<h2>{line[3:]}</h2>"
            continue
        if line.startswith("### "):
            html += f"<h3>{line[4:]}</h3>"
            continue
        if line.startswith("#### "):
            html += f"<h4>{line[5:]}</h4>"
            continue
        if line.startswith("##### "):
            html += f"<h5>{line[6:]}</h5>"
            continue
        
        if line.startswith("img:["):
            img, alt = line[5:-2].split("]{")
            html += f"<img src='{img}' alt='{alt}'>"
            html += f"<p class='img_sub'>{alt}</p>"
            continue
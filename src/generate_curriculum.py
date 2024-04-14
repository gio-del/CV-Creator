import json

import pdfkit
from jinja2 import Environment, FileSystemLoader


def main():
    with open('data/curriculum.json', 'r') as f:
        personal_info = json.load(f)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('curriculum.html')

    rendered_content = template.render(personal_info)

    with open('temp_cv.html', 'w') as f:
        f.write(rendered_content)

    pdfkit.from_file('temp_cv.html', 'output/cv.pdf')

    import os
    os.remove('temp_cv.html')

    print("CV generated successfully!")


if __name__ == "__main__":
    main()

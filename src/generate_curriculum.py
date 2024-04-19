import json
import os

import pdfkit
from jinja2 import Environment, FileSystemLoader

def main():
    for file in os.listdir('data'):
        if file.endswith('.json'):
            with open(f'data/{file}', 'r') as f:
                personal_info = json.load(f)

            env = Environment(loader=FileSystemLoader('templates'))
            template = env.get_template('curriculum.html')

            rendered_content = template.render(personal_info)

            with open('temp_cv.html', 'w') as f:
                f.write(rendered_content)

            if not os.path.exists('output'):
                os.makedirs('output')

            pdfkit.from_file('temp_cv.html', f'output/{file.replace(".json", ".pdf")}',
                             options={'page-size': 'Letter', 'margin-top': '0.75in', 'margin-right': '0.75in',
                                      'margin-bottom': '0.75in', 'margin-left': '0.75in'})

            # os.remove('temp_cv.html')

            print(f"CV for {file.replace('.json', '')} generated successfully!")

if __name__ == "__main__":
    main()

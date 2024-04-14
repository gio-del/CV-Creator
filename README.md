# CV-Creator

## Description

This project is a simple CV generator that takes a JSON file as input and generates a PDF file with the CV.

## Usage

Update the `src/data/curriculum.json` file with your personal information and run the following commands:

Note: This project requires `wkhtmltopdf` to be installed on your system. You can download it from [here](https://wkhtmltopdf.org/downloads.html).

### With Poetry

```bash
poetry install
poetry run python src/generate_curriculum.py
```

The generated CV will be saved in the `src/output/cv.pdf` file.
# CV-Creator

## Usage

Note: This project requires `wkhtmltopdf` to be installed on your system. You can download it from [here](https://wkhtmltopdf.org/downloads.html).

Update the `src/data/curriculum.json` file with your personal information and run the following commands:

```bash
pip install -r requirements.txt
cd src
python generate_curriculum.py
```

The generated CV will be saved in the `src/output/cv.pdf` file.
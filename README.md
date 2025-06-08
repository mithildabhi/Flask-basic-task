
# Flask Projects

This repository contains two simple Flask-based web applications:

## 1️⃣ Flask Blog Page

A blog page application where users can view different blog posts and a blog feed fetched from an external API.

### Features

- View homepage that redirects to the blog page
- View multiple blog posts (read1, read2, read3)
- Dynamic blog feed fetched from an external API
- Basic routing with Flask

### Files

- `main.py` (blog): The main Flask application file for the blog.
- `templates/read.html`: The main blog page template.
- `templates/read1.html`, `templates/read2.html`, `templates/read3.html`: Templates for individual blog posts.
- `templates/blog.html`: Template to display blog feed fetched from the external API.


## 2️⃣ Flask Gender and Age Guessing App

A simple Flask application that uses the Genderize and Agify APIs to guess the gender and age of a person based on their name and country.

### Features

- Accepts `name` and `country` as GET parameters.
- Uses the [Genderize API](https://genderize.io/) to guess gender and its probability.
- Uses the [Agify API](https://agify.io/) to guess the age.
- Displays the result on a simple HTML page.

### Files

- `main.py` (guessing): The main Flask application file for the guessing app.
- `templates/guess.html`: The template for displaying the results.

1. Clone the repository:

```bash
git clone https://github.com/mithildabhi/Flask-basic-task.git
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

4. Install dependencies:

```bash
pip install flask requests
```

---

## License

MIT License

---

Happy coding! 🚀

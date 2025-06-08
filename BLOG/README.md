
# Flask Blog Page

This is a simple Flask-based blog page project. The project allows users to view different blog posts and a blog feed using an external API.

## Features

- View a homepage that redirects to the blog page
- View multiple blog posts (read1, read2, read3)
- Dynamic blog feed fetched from an external API
- Basic routing with Flask

## Files

- `main.py`: The main Flask application file.
- `templates/read.html`: The main blog page template.
- `templates/read1.html`, `templates/read2.html`, `templates/read3.html`: Templates for individual blog posts.
- `templates/blog.html`: Template to display blog feed fetched from the external API.

## Prerequisites

- Python 3.x
- `pip` package manager

## Installation

1. Clone this repository:

```bash
git clone https://github.com/mithildabhi/Flask-basic-task.git
cd BLOG
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

4. Install required dependencies:

```bash
pip install flask requests
```

## Running the Application

```bash
python main.py
```

The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## API

The blog page fetches posts dynamically from this API:

```
https://api.npoint.io/02b306e01cfc087922d9
```

## Customization

- To update the blog feed, change the API URL in `main.py`:

```python
blog_url = "https://api.npoint.io/02b306e01cfc087922d9"
```

## License

MIT License

---

Happy blogging! 🚀

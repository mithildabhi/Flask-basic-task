
# Flask Gender and Age Guessing App

This is a simple Flask application that uses the Genderize and Agify APIs to guess the gender and age of a person based on their name and country.

## Features

- Accepts `name` and `country` as GET parameters.
- Uses the [Genderize API](https://genderize.io/) to guess gender and its probability.
- Uses the [Agify API](https://agify.io/) to guess the age.
- Displays the result on a simple HTML page.

## Files

- `main.py`: The main Flask application file.
- `templates/guess.html`: The template for displaying the results.

## Prerequisites

- Python 3.x
- `pip` package manager

## Installation

1. Clone this repository:

```bash
git clone https://github.com/mithildabhi/Flask-basic-task.git
cd GUESS AGE AND GENDER
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

## Usage

- Navigate to `/guess` and provide `name` and `country` as query parameters.
- Example URL: `http://127.0.0.1:5000/guess?name=prince&country=IN`

## API Used

- [Genderize API](https://genderize.io/)
- [Agify API](https://agify.io/)

## License

MIT License

---

Happy guessing! 🚀

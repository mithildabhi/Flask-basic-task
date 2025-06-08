import requests
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('guess'))

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    name = request.args.get('name', 'prince')
    country = request.args.get('country', 'IN')
    params = {"name": name, "country_id": country}

    gender_response = requests.get("https://api.genderize.io/", params=params)
    gender_data = gender_response.json()
    gender = gender_data.get("gender")
    probability = gender_data.get("probability")

    age_response = requests.get("https://api.agify.io/", params=params)
    age_data = age_response.json()  
    age = age_data.get("age")

    return render_template("guess.html", name=name, gender=gender, probability=probability, age=age)


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Use your actual IP address here

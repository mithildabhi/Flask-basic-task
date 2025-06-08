from flask import Flask
from flask import render_template, request, redirect, url_for
app = Flask(__name__)
import requests

@app.route('/')
def hello_world():
    return redirect("/blog")

@app.route('/blog', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect(url_for('index'))
    return render_template("read.html")


@app.route('/blog/post/1')
def post1():
    return render_template("read1.html")
@app.route('/blog/post/2')
def post2():
    return render_template("read2.html")
@app.route('/blog/post/3')
def post3():
    return render_template("read3.html")

@app.route('/blog-guess')
def blog():
    blog_url = "https://api.npoint.io/02b306e01cfc087922d9" # Replace with the actual URL of your blog API from npoint.io
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)
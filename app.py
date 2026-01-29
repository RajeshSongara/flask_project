from flask import Flask,render_template

posts =[
    
    {
        'author':'corey schafer',
        'title':'blog post 1',
        'content':'first post content',
        'date_posted':'apirl 20 ,2018'
    },
    {
        'author':'Rajesh',
        'title':'blog post 2',
        'content':'secound post content',
        'date_posted':'apirl 21 ,2018'
    },
]


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title='about')


if __name__ == "__main__":
    app.run(debug=True)

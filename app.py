from flask import Flask,render_template
from forms import RegistrationForm,LoginForm  

app.config['SECRETY_KEY']='ff8f51fd787ce470b89e5a9a832ab1d4'


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

@app.route("/register")
def register():
    form=RegistrationForm()
    return render_template("register.html",title='register',form=form)

@app.route("/login")
def login():
    form=LoginForm()
    return render_template("login.html",title='login',form=form)



if __name__ == "__main__":
    app.run(debug=True)

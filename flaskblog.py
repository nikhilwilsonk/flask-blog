from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm

'''
env method
export FLASK_APP=flaskblog.py
flask run
export FLASK_DEBUG=1
flask run now runs in debug mode
'''
app = Flask(__name__)##__name__ means name of the module; to look for static file and templates

app.config['SECRET_KEY']='85c597fcbad01a63ac800b858ac97f27'

posts=[
    {
        'author':'corey',
        'title':'blog1',
        'content':'content of blog 1',
        'date_posted':'11/03/25'
    },
    {
        'author':'nikhil',
        'title':'blog2',
        'content':'content of blog 2',
        'date_posted':'10/03/25'
    },
]
@app.route("/")
@app.route("/home")#to add one more route to this page
def home():
    # return "<p>Hello, World!</p>"
    # return '''
    # <!doctype html>
    # <html></html>
    # '''
    return render_template('home.html',posts=posts)#by passing posts, we will have access to the variables

@app.route("/about")
def about_page():
    # return "<p>this is the about page</p>"
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register_page():
    # return "<p>this is the about page</p>"
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login_page():
    # return "<p>this is the about page</p>"
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@blog.com' and form.password.data =='password':
            flash(f'You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Log In unsuccessful! Please check username and password','danger')
            #no return because it will fall to the login page
    return render_template('login.html',title='Login',form=form)

'''
this condition is only when run with python directly here
if we import it from somewhere else, this will not run
'''

if __name__=='__main__':
    app.run(debug=True) #now will debug



# Routing is the mechanism of mapping the URL directly to the code that creates the webpage.
# It helps in better management of the structure of the webpage and increases the performance of
# the site considerably and further enhancements or modifications become really straight forward.
# In python routing is implemented in most of the web frame works. We will see the examples from flask web
# framework in this chapter.

from flask import Flask, url_for, abort, redirect

app = Flask(__name__)


@app.route('/index')
def indexPage():
    return 'Dashboard fetched..'

@app.route('/login')
def loginPage():
    return 'Login page fetched..'

@app.route('/error')
def errorPage():
    return redirect(url_for('indexPage'))

@app.route('/profile')
def profilePage():
    return 'Profile page fetched..'

@app.route('/errorLogin/<string:userId>')
def invalidLogin(userId):
    abort(401,'Error found with user ID : ' + userId)

@app.route('/mobile/<string:id>')
def fetchMobile(id):
    return id + ' mobile record fetched'

if __name__ == '__main__':
    app.run()

with app.test_request_context():
    print(url_for('index'))
    print(url_for('index', _external=True))
    print(url_for('login'))
    print(url_for('login', next='index'))
    print(url_for('profile', username='Tutorials Point'))

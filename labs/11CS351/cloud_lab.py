import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
	"""Connects to the specific database."""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv


def init_db():
	"""Creates the database tables."""
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()


def get_db():
	"""Opens a new database connection if there is none yet for the
current application context.
"""
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
	"""Closes the database again at the end of the request."""
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()


def check_db(usn, passw):
	db = get_db()
	real_pwd = db.execute('select pass from login where usn =? ',[usn])
	return real_pwd == passw


def add_entry(usn,passw):
    db = get_db()
    db.execute('insert into login (pass, usn) values (?, ?)',
                 [usn, passw])
    db.commit()


@app.route("/")
def index():
	return app.send_static_file('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == 'POST':
		usn = request.form['usn']
		passw = request.form['password']
		usn.encode('ascii','ignore')
		passw.encode('ascii','ignore')
		print usn,type(usn),passw,type(passw)
		add_entry(usn,passw)
		flag = check_db(usn)
		#close_db()
		if flag != True:
		#emulating a db lookup for pwd, must replace later
			return "Incorrect Password"

		session['username'] = usn

		return redirect(url_for('homepage'))

	if 'username' in session:
		return redirect(url_for('homepage'))

	return app.send_static_file('login.html')

@app.route("/homepage")
def homepage(): 
	return render_template('homepage.html', uname=session.get('username', ''))

@app.route("/logout")
def logout():
	# remove the username from the session if its there
	session.pop("username", None)
	return redirect(url_for("index"))


if __name__ == '__main__':
	init_db()
	app.run()

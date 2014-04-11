from sqlite3 import dbapi2 as sqlite3
from werkzeug import secure_filename
from flask import Flask
from flask import request, session, redirect, url_for, escape, render_template, flash, g, abort
from contextlib import closing
import os

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Load default config and override config from an environment variable
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'tmp/cloudlab.db'),
	DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config.from_object(__name__)


def connect_db():
	"""Connects to the specific database."""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv
'''
def init_db():
	"""Creates the database tables."""
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

'''
def get_db():
	"""
	Opens a new database connection if there is none yet for the
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


@app.route("/")
def index():
	return app.send_static_file('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == 'POST':
		usn = request.form['usn']
		passw = request.form['password']

		if check_user(usn, passw):
			session['username'] = usn
			return redirect(url_for('homepage'))
		
		else:
			return redirect(url_for('index'))

	if 'username' in session:
		return redirect(url_for('homepage'))
		
	return app.send_static_file('login.html')



def check_user(usn, pwd):
	db_con = get_db() 
	cur = db_con.cursor()
	cur.execute("SELECT password from login where usn=?", [usn])
	res = cur.fetchone()
	if not res: 
		return False
	else:
		return pwd == res['password']
	


@app.route("/homepage")
def homepage(): 
	return render_template('homepage.html', uname=session.get('username', ''))

@app.route("/logout")
def logout():
	# remove the username from the session if its there
	session.pop("username", None)
	return redirect(url_for("index"))


@app.route('/upload', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['prog']
		f.save('/home/karki/Desktop/PESIT/software_engineering/CloudLab/uploads/'+secure_filename(f.filename))
		return redirect(url_for("homepage"))


if __name__ == "__main__":
	#db_con = sqlite3.connect('tmp/cloudlab.db')
	#db_con.row_factory = sqlite3.Row
	#g.sqlite_db = db_con
	app.run()

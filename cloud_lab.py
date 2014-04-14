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
@app.route("/index")
def index():
	#return app.send_static_file('index.html')
	if session.get('teacher', None):
		return redirect(url_for('manage'))
	if session.get('userid', None):
		return redirect(url_for('homepage'))
	return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == 'POST':
		usn = request.form['usn']
		passw = request.form['password']
		teach = 'teacher' in request.form
		print "teacher : " , teach

		if check_user(usn, passw, teach):
			session['userid'] = usn
			session['teacher'] = 'teacher' in request.form
			
		else: #if login failed
			return redirect(url_for('index'))

	#if the person is logged in
	if 'userid' in session:
		if session.get('teacher',None): #it's a teacher
			return redirect(url_for('manage'))

		else: #it's a student
			return redirect(url_for('homepage'))
		
	#return app.send_static_file('login.html')
	return render_template('login.html') #user not logged in


@app.route("/manage", methods = ['GET'])
def manage():
	if session.get('teacher',None): #it's a teacher
		db_con = get_db() 
		cur = db_con.cursor()

		cur.execute("SELECT * from teacher_lab where tid=?", [session['userid']])
		res = cur.fetchone()
		res = res['lab']

		cur.execute("SELECT usn from student_lab where lab=?", [res])
		usns = cur.fetchall()
		usns = map(lambda x : x['usn'], usns)

		return render_template('manage.html', usns=usns)

	return render_template('not_auth.html')


def check_user(id, pwd, is_teacher):
	db_con = get_db() 
	cur = db_con.cursor()

	if is_teacher:
		cur.execute("SELECT password from teacher_login where tid=?", [id])
	else :
		cur.execute("SELECT password from student_login where usn=?", [id])

	res = cur.fetchone()

	if not res: 
		return False
	else:
		return pwd == res['password']
	


@app.route("/homepage")
def homepage(): 
	if not session.get('userid', None):
		return render_template('not_auth.html')

	if session.get('teacher', None):
		return redirect(url_for('manage'))
	return render_template('homepage.html', uname=session.get('userid', ''))

@app.route("/logout")
def logout():
	# remove the username from the session if its there
	session.pop("userid", None)
	session.pop("teacher", None)
	return redirect(url_for("index"))


@app.route('/upload', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['prog']
		f.save('/home/karki/Desktop/PESIT/software_engineering/CloudLab/uploads/'+secure_filename(f.filename))
		return redirect(url_for("homepage"))


if __name__ == "__main__":
	app.run()

from flask import Flask
from flask import request, session, redirect, url_for, escape, render_template

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def index():
	return app.send_static_file('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == 'POST':
		usn = request.form['usn']
		passw = request.form['password']

		if passw != usn:
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


if __name__ == "__main__":
	app.run()

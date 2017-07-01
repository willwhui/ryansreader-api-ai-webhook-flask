from flask import Flask, request, render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

@app.route('/ryansreader', methods=['GET', 'POST'])
def ryansreader():
	list = [
		{'speech': 'Webhook: I\'m sorry. My responses are limited. You must ask the right questions.', 'displayText': 'Webhook: I\'m sorry. My responses are limited. You must ask the right questions.'}
    ]
	return jsonify(list)

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run('0.0.0.0', port=443, ssl_context='adhoc')

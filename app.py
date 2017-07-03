from flask import Flask, request, render_template
from flask import jsonify
from flask import json

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
    data = 'This is a sample response from your webhook!'
    response = app.response_class(
        response=json.dumps({"speech": data, "displayText": data}),
        status=200,
        mimetype='application/json'
    )
    return response
    #return jsonify({"speech": response, "displayText": response})

if __name__ == '__main__':
    # only usefull when this moudle directly runed like " python3 app.py"
    app.run(host='0.0.0.0', port=80)
    # app.run('0.0.0.0', port=443, ssl_context='adhoc')

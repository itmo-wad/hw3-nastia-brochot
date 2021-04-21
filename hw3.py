from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

password = "password"

@app.route('/static/<path:path>')
def image(path):
    return app.send_static_file(path)

@app.route('/', methods=['GET', 'POST'])
def login():
    username = "nastia"
    error = None
    if request.method == 'POST':
        if request.form['username'] != username or request.form['password'] != password:
            error = 'Invalid Credentials. Please try again.'
        else:
            return "You are connected"
    return render_template('login.html', error=error)


@app.route('/cabinet', methods=["GET", "POST"])
def cabinet():
    global password
    if request.method == "GET":
        return render_template("cabinet.html", password=password)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
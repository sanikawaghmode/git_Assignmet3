from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.secret_key = "flasklab"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "" or password == "":
            flash("Username and Password are required!")
        elif username == "admin" and password == "admin123":
            flash("Login Successful!")
        else:
            flash("Invalid Username or Password!")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
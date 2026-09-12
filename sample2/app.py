from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.secret_key = "flasklab"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if (name == "" or email == "" or username == "" or
                password == "" or confirm_password == ""):
            flash("All fields are required!")
        elif password != confirm_password:
            flash("Password and Confirm Password do not match!")
        else:
            flash("Registration Successful!")

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
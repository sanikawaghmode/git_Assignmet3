from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "flasklab"

@app.route('/age', methods=['GET', 'POST'])
def age():

    if request.method == 'POST':

        name = request.form['name']
        birth_year = request.form['birth_year']

        if name == "" or birth_year == "":
            flash("Please enter all details!")

        else:
            current_year = 2026
            age = current_year - int(birth_year)

            flash("Name: " + name + ", Age: " + str(age))

    return render_template('age.html')


if __name__ == '__main__':
    app.run(debug=True)
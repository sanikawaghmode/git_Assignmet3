from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.secret_key = "flasklab"


@app.route('/event', methods=['GET', 'POST'])
def event():

    if request.method == 'POST':

        name = request.form['name']
        mobile = request.form['mobile']
        event_name = request.form['event_name']

        if name == "" or mobile == "" or event_name == "":
            flash("All fields are required!")

        else:
            flash("Registration Successful! Name: " + name +
                  ", Mobile: " + mobile +
                  ", Event: " + event_name)

    return render_template('event.html')


if __name__ == '__main__':
    app.run(debug=True)
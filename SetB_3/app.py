from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():

    if request.method == 'POST':

        temp = float(request.form['temp'])
        choice = request.form['choice']

        if choice == 'C':
            result = (temp * 9/5) + 32
            unit = "Fahrenheit"

        else:
            result = (temp - 32) * 5/9
            unit = "Celsius"

        return render_template('temp.html',
                               temp=temp,
                               result=result,
                               unit=unit)

    return render_template('temp.html')


if __name__ == '__main__':
    app.run(debug=True)
    
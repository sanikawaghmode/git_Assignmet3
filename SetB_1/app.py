from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/electricity', methods=['GET', 'POST'])
def electricity():

    if request.method == 'POST':

        name = request.form['name']
        consumer_no = request.form['consumer_no']
        units = int(request.form['units'])

        if units <= 100:
            bill = units * 5

        elif units <= 200:
            bill = 100 * 5 + (units - 100) * 7

        else:
            bill = 100 * 5 + 100 * 7 + (units - 200) * 10

        return render_template('bill.html',
                               name=name,
                               consumer_no=consumer_no,
                               units=units,
                               bill=bill)

    return render_template('bill.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/employee', methods=['GET', 'POST'])
def employee():
    if request.method == 'POST':
       
        return render_template('employee.html',
                                emp_id = request.form['emp_id'],
                                name = request.form['name'],
                                department = request.form['department'],
                                designation = request.form['designation']
                                )
                               

    return render_template('employee.html')


if __name__ == '__main__':
    app.run(debug=True)
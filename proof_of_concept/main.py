from flask import Flask, request, render_template
from solver import trajectory_calculator
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

    # if request.method == 'GET':
    #     velocity = request.values.get('velocity', type=float)
    #     angle = request.values.get('angel', type=float)
    #     h, total_length, total_time = None, None, None
    #     try:
    #         h, total_length, total_time = trajectory_calculator(
    #             velocity, angle)
    #         apply_alert = False
    #     except TypeError:
    #         print('not the right input')
    #         apply_alert = True

    # return render_template('index.html', h=h, total_length=total_length, total_time=total_time, apply_alert=apply_alert)


@app.route('/', methods=['POST'])
def calculate():
    error = None
    if request.method == 'POST':
        if request.form['velocity'] and request.form['angle']:
            velocity = request.values.get('velocity', type=float)
            angle = request.values.get('angle', type=float)
            h, total_length, total_time = trajectory_calculator(
                velocity, angle)
            return render_template('index.html', h=h, total_length=total_length, total_time=total_time ,error=error)
        else:
            error = 'the input must be an integer or a float number'
            return render_template('index.html',error=error)
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # return render_template('login.html', error=error)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',)

from flask import Flask, request, render_template
from solver import trajectory_calculator
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


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


if __name__ == '__main__':
    app.debug = True
    app.run()

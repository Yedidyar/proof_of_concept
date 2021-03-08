from flask import Flask, request, render_template
from solver import trajectory_calculator

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        velocity = request.values.get('velocity', type=int)
        angle = request.values.get('angel', type=int)
        h, total_length, total_time = trajectory_calculator(velocity,angle)
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
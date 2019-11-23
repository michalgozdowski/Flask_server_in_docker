from flask import Flask, jsonify, render_template
import yaml

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/app/api/v1/info', methods=['GET'])
def get_tasks():
    data = {'version': '0.1', 'author': 'Misiek'}
    return jsonify(data)


with open('config/config.yml') as file_handler:
    port = yaml.load(file_handler.read()).get('PORT', 7000)


app.run(debug=True, port=port, host='0.0.0.0')


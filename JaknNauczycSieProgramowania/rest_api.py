from flask import Flask

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return 'to jest test'


app.run(port=3000)

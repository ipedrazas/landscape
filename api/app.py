from flask import Flask

# Configuration
GRAPH_DATABASE = 'http://neo4j:7474/db/data/'

app = Flask(__name__)


@app.route("/version")
def version():
    return 'Landscape v0.0.1'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

from flask import Flask
from flask import request
from flask.ext.cors import CORS
from flask import jsonify
from model import Base, Person, Application, Component
import json

# Configuration
GRAPH_DATABASE = 'http://neo4j:7474/db/data/'

app = Flask(__name__)
cors = CORS(app)


@app.route("/version")
def version():
    return 'Landscape v0.0.2'


# curl -H "Content-Type: application/json" -X POST
# -d '{"source":"kJM65aOgVGqZjQ4f", "target": "QvDgoCy7OJmBxNS9",
# "rel": "USES", "target_label": "Application"}'
# http://localhost:5000/people/rels

@app.route("/links", methods=['POST'])
def add_link():
    pjson = json.loads(request.data)
    source = Base.find_by_id(pjson.get('source_label'), pjson.get('source'))
    if source:
        if pjson.get('rel') in Base.rels:
            res = source.create_rels(
                pjson.get('target'),
                pjson.get('target_label'),
                pjson.get('rel'))
            if res:
                return jsonify({'result': "Ok"}), 200
            else:
                return jsonify({'result': "relationship exists"}), 409
        else:
            return jsonify({'result': "relationship not allowed"}), 201
    return jsonify({'result': "Source not found"}), 404


@app.route("/people/rels", methods=['GET'])
def get_people_rels():
    return jsonify({'people_rels': Person.rels})


@app.route("/people", methods=['GET'])
def get_people():
    return jsonify({'people': Base.find_all('Person')})


# curl -H "Content-Type: application/json" -X POST -d '{"name":"Ergo"}'
# http://localhost:5000/people
@app.route("/people", methods=['POST'])
def add_people():
    pjson = json.loads(request.data)
    person = Person(pjson.get('name'))
    person.save()
    return jsonify({'result': "Ok"})


@app.route("/applications", methods=['POST'])
def new_application():
    pjson = json.loads(request.data)
    app = Application(pjson.get('name'))
    app.save()
    return jsonify({'result': "Ok"})


@app.route("/applications", methods=['GET'])
def get_applications():
    return jsonify({'applications': Base.find_all('Application')})


@app.route("/links/<app_id>", methods=['GET'])
def get_children(app_id):
    return jsonify({'parent': app_id, 'children': Base.find_children(app_id)})


@app.route("/components", methods=['POST'])
def new_component():
    pjson = json.loads(request.data)
    app = Component(pjson.get('name'))
    app.save()
    return jsonify({'result': "Ok"})


@app.route("/components", methods=['GET'])
def components():
    return jsonify({'components': Base.find_all('Component')})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

from py2neo import Graph, Node, Relationship
import os


url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474')
graph = Graph(url + '/db/data/')


class Resource:
    def __init__(self, name):
        self.name = name

    def add_resource(self):
        user = Node("Resource", name=self.name)
        graph.create(user)

    def add_relationship(self, resource, label):
        rel = Relationship(self, label, resource)
        graph.create(rel)

    def find(self):
        resource = graph.find_one("Resource", "name", self.name)
        return resource

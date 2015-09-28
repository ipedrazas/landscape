from py2neo import authenticate, Graph, Node, Relationship
import os
from utils import short_id

host = os.environ.get('NEO_HOST', 'neo4j')
port = os.environ.get('NEO_PORT', 7474)
user = os.environ.get('NEO_USER', 'neo4j')
password = os.environ.get('NEO_PASSWORD', 'password')
url = 'http://' + host + ":" + str(port) + '/db/data/'

authenticate(host + ":" + str(port), user, password)

graph = Graph(url)


class Base(object):
    rels = ["BELONGS", "SUPPORTS", "ADMINISTERS", "USES", "IS_PART"]

    def __init__(self, name, type, id=None):
        self.name = name
        self.type = type
        if id:
            self.node_id = id
        else:
            self.node_id = short_id(16)

    def save(self):
        base = Node(self.type, name=self.name, node_id=self.node_id)
        graph.create(base)

    def add_relationship(self, resource, label):
        rel = Relationship(self, label, resource)
        graph.create(rel)

    @staticmethod
    def find_by_id(type, id):
        obj = graph.find_one(
            label=type, property_key="node_id", property_value=id)
        print obj
        if obj:
            node = obj
            return Base(node['name'], type, node['node_id'])

    @staticmethod
    def find_all(label):
        res = graph.cypher.execute(
            "MATCH (n:" + label + ") RETURN n, n.node_id, n.name")
        elements = []
        for entry in res:
            node = entry[0]
            elements.append(
                {'name': node['name'], 'id': node['node_id'], 'type': label})
        return elements

    @staticmethod
    def find_children(elem_id):
        res = graph.cypher.execute(
            "match (n{node_id: '" + elem_id + "'}) -[r] -(m) return n,r,m")
        elements = []
        subgraph = res.to_subgraph()
        rels = subgraph.relationships
        for rel in rels:
            node = rel.start_node
            target = rel.end_node
            elements.append({
                'source_name': node['name'],
                'source_id': node['node_id'],
                'rel': rel.type,
                'target_name': target['name'],
                'target_id': target['node_id']
            })
        return elements

    def create_rels(self, target, target_label, relationship):
        source_elem = graph.find_one(
            label=self.type,
            property_key="node_id",
            property_value=self.node_id)
        if source_elem:
            target_elem = graph.find_one(
                label=target_label,
                property_key="node_id",
                property_value=target)
            if target_elem:
                # if len(list(graph.match(
                #     start_node=source_elem,
                #     end_node=target_elem,
                #     rel_type=relationship
                # ))) > 0:
                #     return False
                rel = Relationship(source_elem, relationship, target_elem)
                graph.create(rel)
                return True
        return False


class Person(Base):
    def __init__(self, name):
        Base.__init__(self, name, "Person")

    def __str__(self):
        return 'name:' + self.name + ', id:' + self.node_id


class Application(Base):
    def __init__(self, name):
        Base.__init__(self, name, "Application")


class Resource(Base):
    def __init__(self, name):
        Base.__init__(self, name, "Resource")


class Component(Base):
    def __init__(self, name):
        Base.__init__(self, name, "Component")


class Provider(Base):
    def __init__(self, name):
        Base.__init__(self, name, "Provider")


class Environment(Base):
    def __init__(self, name):
        Base.__init__(self, name, "Environment")

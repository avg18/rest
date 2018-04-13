#/usr/bin/env --utf-8--

import uuid
import logging
import re

from datetime import datetime 

URI = 'http://localhost:9090/v1.0'

logger = logging.getLogger(__name__)

class Document(object):
    def __init__(self, name, beschreibung = None, version = 0):
        self.id = uuid.uuid4()
        self.version = version
        self.name = name
        self.timestamp = datetime.now()
        self.beschreibung = beschreibung
    
    def __str__(self):
        return f'{self.id}: {self.beschreibung}'

    def JSON_Container(self):
        con = {}
        con['id'] = self.id
        con['name'] = self.name
        con['timestamp'] = self.timestamp
        con['description'] = self.beschreibung
        con['version'] = self.version
        con['links'] = [{'rel': 'self', 'href':f'{URI}/documents/{self.id}'},
                        {'rel': 'self.description', 'href':f'{URI}/documents/description/{self.id}'} ]
        return con

###
# HATEAOS
###
def JSON_description(container, _id):
    con = {}
    con['description'] = container[_id]['description']
    con['links'] = [{'rel': 'self', 'href':f'{URI}/documents/description/{_id}'}, 
                    {'rel': 'self.document', 'href':f'{URI}/documents/{_id}'}]
    return con

###
# CONTROLLER
##

def valid_uuid(uuid):
    regex = re.compile('^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)
    match = regex.match(uuid)
    return bool(match)

# memory-only Dokumenten Sammlung
DOC = {}

def get_documents():
    return list(DOC.values())

def get_document(id):
    
    if not valid_uuid(id):
        return ('Not found', 404) 

    _id = uuid.UUID(id)
    doc = DOC.get(_id)

    return doc or ('Not found', 404) 

def get_descriptions():
    ids = list(DOC.keys())
    return [JSON_description(DOC,_id) for _id in ids]

def get_description(id):
    _id = uuid.UUID(id)
    return JSON_description(DOC,_id)

def post_document(document):
    logger.info(document)
    add_document(document['name'],document['description'])
    
def add_document(name, beschreibung=None, version = 0):
    doc_item = Document(name, beschreibung, version)
    logger.info(doc_item)
    DOC[doc_item.id]= doc_item.JSON_Container()
    
if __name__ == '__main__':
    print(Document('Important Document'))
    print(Document('Important Document'))



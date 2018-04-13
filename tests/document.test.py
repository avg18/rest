import sys
sys.path.append('E:/00_AVG-Workspace/03-Dev/32-Abgabe1/2_REST')

from documents.document import *
from documents.doc_mock import dummy

import uuid


URI = 'http://localhost:9090/v1.0'

def JSON_description(container, _id):
    con = {}
    con['description'] = container[_id]['description']
    con['links'] = [{'rel': 'self', 'href':f'{URI}/documents/description/{_id}'}, 
                    {'rel': 'self.document', 'href':f'{URI}/documents/{_id}'}]
    return con
dummy()
ids = list(DOC.keys())

des = 

print(des)
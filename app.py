#/usr/bin/env --utf-8--


import connexion
import logging 

logging.basicConfig(level=logging.INFO)

app = connexion.FlaskApp(__name__, port=9090, specification_dir='apis/')
app.add_api('doc-api.yaml', arguments={'title': 'Intranet - important Docs'})

if __name__ == '__main__':
    
    from documents import doc_mock
    doc_mock.dummy()
    app.run()
    
    



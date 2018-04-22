# AVG REST

RESTful API for dummy book shelf.

# Techstack

Python = 3.6 mit connexion für Swagger integration.
Api Dokumentation: SWAGGER
Tests: Tavern


## Prerequisites

Install Conda: https://conda.io/miniconda.html

## Installing

just one out of the two following options is required:

**rest-environment**
````
 $ conda env create -f environment-rest.yml
````

**or just libraries:** (Tests wont work)
````
Note: <> denotes changes to be made
 $ conda create --name <env-name> --file requirements.txt
````



## Run
Run app.py in environment. 

# API

````
http://localhost:9090/v1.0/ui/

````

# Tests

````
$ py.test test.tavern.yaml -v
````
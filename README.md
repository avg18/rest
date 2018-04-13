# AVG REST

RESTful API for dummy book shelf.

## Prerequisites

Install Conda: https://conda.io/miniconda.html

## Installing

just one out of the two following options is required:

**rest-environment**
````
 $ conda env create -f environment-rest.yml
````

**or just libraries:** (API tests wont work)
````
Note: <> denotes changes to be made
 $ conda create --name <env-name> --file requirements.txt
````



## Run
Run app in in the environment. 

# API

````
http://localhost:9090/v1.0/ui/

````

# Tests

````
$ py.test test.tavern.yaml -v
````
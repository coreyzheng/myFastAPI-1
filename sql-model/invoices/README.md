# Running on terminal with a specified port
$ fastapi dev fastapi_invoices.py --host 0.0.0.0  --port 83


# Dockerization of sqllite_invoices.py
1, add & edit the entrypoint.sh & Docker file 
2, build the docker image: $ docker build -t fastapi_invoices . 
3, check the docker image: $ docker images 
4, removing a docker image: $ docker rmi -f <image-id, ie. 9673e30911a0> 
5, run the docker image: $ docker run -p 83:83 fastapi_invoices; 
6, or run it in the background with a name: $ docker run -d --name docker-fastapi_invoices -p 83:83 fastapi_invoices; 
7, open a browser window and connect to: http://0.0.0.0:83

# Reference
1 https://sqlmodel.tiangolo.com/databases/#a-server-database 
2 https://fastapi.tiangolo.com/advanced/templates/#template-url_for-arguments

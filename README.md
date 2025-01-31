# Github

echo "# myFastAPI" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/yaoyaow21/myFastAPI.git
git push -u origin main




# Python

https://github.com/fastapi/fastapi

* python -m venv .venv
$ py -m venv .venv

$ .venv\Scripts\Activate.ps1

$ cd app
$ pip install "fastapi[standard]"

$ fastapi dev main.py

# Docker
$ pip freeze > requirements.txt
$ docker build -t fastapi-demo .
$ docker run -d --name d-fastapi-demo -p 80:80 fastapi-demo 
* open a web browser and connect to URL: http://localhost/docs

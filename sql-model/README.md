# demo projects of FastAPI and SQL Model
* \products 
*   a sub folder of the fastapi-product microservice
* \customers    
*   a sub folder of the fastapi-customer microservice
* \invoices
*   a sub folder of the fastapi-invoice microservice

# Reference
1 https://sqlmodel.tiangolo.com/databases/#a-server-database 
2 https://fastapi.tiangolo.com/advanced/templates/#template-url_for-arguments

# Intro to Python & mySQL 
* Update .zshrc with the python v3.13 path
$ cd ~ 
$ ls -l -a
$ vim .zshrc
# add export PATH="/opt/homebrew/bin/python3:$PATH"
$ source .zshrc

Remove python v3.8.9 symlink
$ cd ~ 
$ sudo rm -rf /Library/Frameworks/Python.framework/Versions/3.8.9
# list the broken symlink
$ ls -l /usr/local/bin | grep '../Library/Frameworks/Python.framework/Versions/3.8.9'
# to remove the broken symlink
$ cd /usr/local/bin
$ ls -l /usr/local/bin | grep '../Library/Frameworks/Python.framework/Versions/3.8.9' | awk '{print $9}' | tr -d @ | xargs rm

Create a Virtual Environment for Python v3.13
$ cd <your-project>
$ python -m venv .venv13
# to activate the venv on Linus or Mac OS
$ source .venv13/bin/activate

$ pip install "fastapi[standard]"

$ pip install sqlmodel

$ pip freeze > requiements.txt

$ python3 -m pip install --upgrade pip

Reference
#1 https://sqlmodel.tiangolo.com/databases/#a-server-database
#2 https://fastapi.tiangolo.com/advanced/templates/#template-url_for-arguments

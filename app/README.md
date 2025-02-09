# this is the extended test app

* refer to: https://fastapi.tiangolo.com/tutorial/testing/?h=test#extended-fastapi-app-file

* initialize the test environment
$ cd \app
$ pip install "fastapi[standard]"
$ pip install httpx
$ pip install starlette
$ pip install pytest

* run the test cases; expect all passing:
$ pytest

* modify line 24 in main.py from 'if x_token != fake_secret_token:' to 
* 'if x_token == fake_secret_token:';
* re-run the test, expect one failure

* modify line 25 in test-main.py from 'response = client.get("/items/baz" .. ' to
* 'response = client.get("/items/bar'.
* re-run the test, then the response code = 200 so line 26 will fail. 

* re-establish the environment by re-installing the requitements 
$ pip install -r requirements.txt

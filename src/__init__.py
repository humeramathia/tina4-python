#
# Tina4 - This is not a 4ramework.
# Copy-right 2007 - current Tina4
# License: MIT https://opensource.org/licenses/MIT
#
import os
import sqlite3

from tina4_python import Migration
from tina4_python.Template import Template
from tina4_python.Debug import Debug
from tina4_python.Router import get
from tina4_python.Router import post
from tina4_python.Database import Database


dba1 = Database("sqlite3:test.db", "username", "password")
dba2 = Database("firebird.driver:localhost:d:\\tmp\\ZOO.FDB", "sysdba", "masterkey")


rows = dba2.fetch("select * from zoo")
print("FIRST", rows.to_json(), rows.columns, rows.error)

rows = dba2.fetch("select * from zoo where id = ? and name = ?", [1, "ZOO 1"], 1)
print("SECOND", rows[0], rows.columns, rows.error)

rows = dba1.fetch("select * from test")
print("THIRD", rows)


dba1.close()
dba2.close()


dba = sqlite3.connect("test.db")
Migration.migrate(dba)

@get("/env")
async def env(request, response):
    Debug("Api GET")
    env_variables = os.environ

    return response(env_variables)


# This is a simple example of a GET request
# This will be available at http://localhost:port/example

@get("/example")
async def example(request, response):
    # Add your code here
    message = "This is an example of a GET request"
    return response(message)


@get("/capture")
async def capture_get(request, response):
    # Add your code here
    token = tina4_python.tina4_auth.get_token({"data": {"formName": "capture"}})
    print(token)
    html = Template.render_twig_template("somefile.twig", {"token": token})
    return response(html)


@post("/capture")
async def capture_post(request, response):


    return response(request.body)


# This is an example of parameterized routing
# This will be available at http://localhost:port/YOURNAME/YOURSURNAME?id=YOURID
@get("/names/{name}/{surname}")
async def example(request, response):
    Debug("Api GET")
    print('Params', request.params)
    name = request.params['name']
    surname = request.params['surname']

    # check if id is present
    if "id" in request.params:
        id = request.params['id']
    else:
        id = "No id provided"

    message = f"Hello {name} {surname} with id {id}"
    return response(f"{message}")


# This is an example of a POST request
# This will be available at http://localhost:port/api/generate
# You can test this using Postman
@post("/api/generate")
async def post_me(request, response):
    req = "NA"
    if request.body is not None:
        req = request.body

    Debug(f"POST: {req}")
    return response(req)





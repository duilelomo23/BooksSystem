from flask import Flask, g, json
from flask.json.provider import DefaultJSONProvider
import todos.apis
import users.apis
import books.apis
from datetime import datetime, date
import pymysql

#app instance
app = Flask("todo_system")
app.secret_key = 'my_secret_key'


#開啟config.json
with open('./config.json') as f:
    cfg = json.load(f)
    app.config.update(cfg)


# 每次request 建立G物件.cusor  response g消失
@app.before_request
def before_request_func():
    def get_cursor():
        if g.get("_cursor", None) == None:
            conn=pymysql.connect(host=app.config['mysql']['host'], \
                                port=app.config['mysql']['port'], \
                                user=app.config['mysql']['user'], \
                                password=app.config['mysql']['password'], \
                                db=app.config['mysql']['db'], \
                                charset=app.config['mysql']['charset'])
                                
            g._cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return g._cursor
    g.cursor = get_cursor

    
@app.teardown_request
def teardown_request_func(exc):
    cur = g.get("_cursor", None)
    if cur != None:
        if exc != None:
            cur.connection.rollback()
        cur.connection.close()


#route
app.register_blueprint(todos.apis.blueprint, url_prefix = "/users")
app.register_blueprint(users.apis.blueprint, url_prefix = "/users")
app.register_blueprint(books.apis.blueprint, url_prefix = "/books")




#jsonify() customize convert
class UpdatedJSONProvider(DefaultJSONProvider):
    def default(self, o):
        if isinstance(o, (date,datetime)):
            return o.isoformat()
        # elif isinstance(o, (bytes)):
        #     print(struct.unpack('?',o)[0])
        #     return struct.unpack('?',o)[0]
        return super().default(o)
app.json = UpdatedJSONProvider(app)
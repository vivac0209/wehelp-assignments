from flask import *
import mysql.connector
import pymysql
from flask import Blueprint
from AllRoutes.routes import app2

app=Flask(__name__) 
app.register_blueprint(app2)

app.secret_key="qqqqq"
@app.route("/")
def index():
    return render_template("index.html")

app.run(debug=True)

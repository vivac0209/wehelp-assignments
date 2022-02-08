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

app.run(port=3000)

# #處理路徑 /singin
# @app.route("/singin",methods=["POST"])
# def singin():
#     handle =request.form["handle"]
#     pws =request.form["pws"]
    
#     sqlFoundHandle =  "SELECT * FROM `member` WHERE`username`= '%s'" % handle
#     cursor.execute(sqlFoundHandle)
#     handleResult = cursor.fetchone()
#     print(handleResult)
    
#     # sqlFoundPws =  "SELECT * FROM `member` WHERE`password`= '%s'" % pws
#     # cursor.execute(sqlFoundPws)
#     # pwsResult = cursor.fetchone()
#     # cursor.reset()
#     # print(pwsResult)
#     if handle =="" or pws =="":
#         return redirect("/error?message=帳密輸入空值",)
#     if handleResult !=None:
#         pwsResult = handleResult[3]
#         print(pwsResult)
#         if pws == pwsResult:
#             session["memberName"] = handle
#             cursor.reset()
#             return redirect("/member")
#         else:
#             cursor.reset()
#             return redirect("/error?message=帳號密碼輸入錯誤",)
#     cursor.reset()
#     return redirect("/error?message=找不到帳號",)

# @app.route("/member")
# def member():
#     if "memberName" in session:
#         loginHandle = session["memberName"]
#         sqlFoundName =  "SELECT * FROM `member` WHERE`username`= '%s'" % loginHandle
#         cursor.execute(sqlFoundName)
#         NameResult = cursor.fetchone()
       
#         return render_template("member.html",handle=NameResult[1])
#     else:
#         return redirect("/")

# @app.route("/error")
# def error():
#     message = request.args.get("message","發生錯誤")
#     tipMessage = "請輸入帳號、密碼"
#     if message == "帳密輸入空值":
#         return render_template("error.html",message="帳密輸入空值")
#     else:
#         return render_template("error.html",message=message)

# @app.route("/singout")
# def singout():
#     del session["memberName"]
#     return redirect("/")



from flask import *
import mysql.connector
import pymysql
import password as pwd
from flask import Blueprint

import json

db = mysql.connector.connect(
  host="localhost",
  user = "root",
  password = pwd.password,
  database = "website",
  )
cursor = db.cursor(buffered=True)

print("連線成功")

app2=Blueprint("app2",__name__,static_folder="static",template_folder="templates")

###########################   week7 
# 要求一：
@app2.route("/api/members", methods=['GET'])
def query():
    username = request.args.get("username")
    # print(username)

    sqlFoundName =  "SELECT * FROM `member` WHERE`username`= '%s'" % username
    cursor.execute(sqlFoundName)
    NameResult = cursor.fetchone()
    # print(NameResult)
    data={}
    if NameResult:
        # print("ok")
        # 新增到dict
        memberID = NameResult[0]
        memberName = NameResult[1]
        memberUserName = NameResult[2]
        data["id"]= memberID
        data["name"]= memberName
        data["username"]= memberUserName
        # print(data)
        # memberData=jsonify (data)
        print(data)

        return json.dumps({"data":data})
    else:
        return json.dumps({"data":None})

#要求三
@app2.route("/api/member",methods=["POST"])
def update():
    updateName = request.get_json()
    newName = updateName["name"]
    if newName == "":
        return "輸入空值"
    
    #先抓舊的username
    oldNameHandle = session["memberName"]
    # print(oldNameHandle)
    if oldNameHandle == "":
        return json.dumps({"error":True})
    else:
        sqlActionUpdate =  "UPDATE `member` SET `name`=%s WHERE `username`=%s"
        nameList=(newName,oldNameHandle)
        cursor.execute(sqlActionUpdate,nameList)
        db.commit()
        session["memberName"]=newName
        return json.dumps({"ok":True})
        

############################################# 

# 處理路徑 /singup
@app2.route("/singup",methods=["POST"])
def singup():
    name = request.form["nickname"]
    handle = request.form["username"]
    pws = request.form["pws"]
    
    #在資料庫查找帳號有沒有被註冊過

    # 選擇member表格
    # sqlAction = MySQL指令 去搜尋帳號
    sqlActionQuery =  "SELECT * FROM `member` WHERE`username`= '%s'" % handle
    cursor.execute(sqlActionQuery)
    result = cursor.fetchone()
    # print(result)

    if name =="" or handle =="" or pws =="":
        return redirect("/error?message=帳密輸入空值")

    if result != None:
        cursor.reset()
        return redirect("/error?message=帳號已經被註冊")
    
    else:
        sqlActionAdd = "INSERT INTO `member` (name,username,password) VALUES (%s,%s,%s)"
        sqlValue = (name,handle,pws)
        cursor.execute(sqlActionAdd,sqlValue)
        db.commit()
        session["memberName"] = handle
        cursor.reset()
        return redirect("/")

# 處理路徑 /singim
@app2.route("/singin",methods=["POST"])
def singin():
    handle =request.form["handle"]
    pws =request.form["pws"]
    
    sqlFoundHandle =  "SELECT * FROM `member` WHERE`username`= '%s'" % handle
    cursor.execute(sqlFoundHandle)
    handleResult = cursor.fetchone()
    # print(handleResult)
    
    # sqlFoundPws =  "SELECT * FROM `member` WHERE`password`= '%s'" % pws
    # cursor.execute(sqlFoundPws)
    # pwsResult = cursor.fetchone()
    # cursor.reset()
    # print(pwsResult)
    if handle =="" or pws =="":
        return redirect("/error?message=帳密輸入空值",)
    if handleResult !=None:
        pwsResult = handleResult[3]
        # print(pwsResult)
        if pws == pwsResult:
            session["memberName"] = handle
            cursor.reset()
            return redirect("/member")
        else:
            cursor.reset()
            return redirect("/error?message=帳號密碼輸入錯誤",)
    else:
        cursor.reset()
        return redirect("/error?message=找不到帳號",)

#處理路徑 /member
@app2.route("/member")
def member():
    if "memberName" in session:
        loginHandle = session["memberName"]
        sqlFoundName =  "SELECT * FROM `member` WHERE`username`= '%s'" % loginHandle
        cursor.execute(sqlFoundName)
        NameResult = cursor.fetchone()
        cursor.reset()
        return render_template("member.html",handle=NameResult[1])
    else:
        return redirect("/")

#處理路徑 /error
@app2.route("/error")
def error():
    message = request.args.get("message","發生錯誤")
    tipMessage = "請輸入帳號、密碼"
    if message == "帳密輸入空值":
        return render_template("error.html",message="帳密輸入空值")
    else:
        return render_template("error.html",message=message)


#處理路徑 /singout
@app2.route("/singout")
def singout():
    del session["memberName"]
    return redirect("/")

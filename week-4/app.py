from flask import Flask, request,redirect,render_template
from flask import session

app=Flask(__name__,static_folder="static", static_url_path="/") 

app.secret_key="qqqqq"
@app.route("/")
def index():
    return render_template("index.html")


#處理路徑 /singin
@app.route("/singin",methods=["POST"])
def singin():
    handle =request.form["handle"]
    pws =request.form["pws"]
    
    if handle =="test" and pws =="test":
        session["memberName"] = handle
        return redirect("/member")
    elif handle =="" or pws =="":
        return redirect("/error?message=帳密輸入空值",)
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")


@app.route("/member")
def member():
    if "memberName" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    message = request.args.get("message","發生錯誤")
    tipMessage = "請輸入帳號、密碼"
    if message == "帳密輸入空值":
        return render_template("error.html",message=tipMessage)
    else:
        return render_template("error.html",message=message)
    
@app.route("/singout")
def singout():
    del session["memberName"]
    return redirect("/")

app.run(port=3000)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>會員首頁</title>
    <style>
        .header{
            color:white; 
            background: rgb(76, 52, 231);
            height: 30%;
        }
        .header h1{
            text-align:center;
            padding: 20px;
        }
        .singup{
            text-align:center;
        }
        .singup h2{
            font-weight: bold;
        }
        .singup button{
            margin-top: 10px;
        }
        .login{
            text-align:center;
        }
        .login button{
            margin-top: 10px;
        }
        .login h2{
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>歡迎光臨 請註冊登入系統</h1>
    </div>
    <div class="singup">
        <h2>註冊帳號</h2><br>
        <form action="/singup" method="POST">
            姓名 <input type="text" name="nickname"><br>
            帳號 <input type="text" name="username"><br>
            密碼 <input type="text" name="pws"><br>
            <button>註冊</button>
        </form>
        
    </div>
    <div class="login">
        <h2>登入系統</h2><br>
        <form  action="/singin" method="POST">
            帳號 <input type="text" name="handle"><br>
            密碼 <input type="password" name="pws"><br>
            <button>登入</button>
        </form>
    </div>
    
</body>
</html>


//查詢會員資料
let button = document.getElementById("queryButton");
let memberData = document.getElementById("queryResult");

button.addEventListener('click',function(){
    let username =document.getElementById("queryUsername").value;
    let members_url = `http://127.0.0.1:5000/api/members?username=`+ username;


    fetch(members_url,{})
        .then((response)=> {
            return response.json();
        })
        .then((jsonData)=>{
            // console.log(jsonData);
            
            if (jsonData.data != null){
                let name=jsonData.data.name;
                let username=jsonData.data.username;
                
                memberData.textContent= `${name}` + `(${username})`;
                
            } else if (jsonData.data ===null){
                memberData.textContent= "查無資料";
            }
        })
        // .catch((error)=>{
        //     console.log("連線出現錯誤")
        // })
})


//更新會員姓名
let updateButton = document.getElementById("updateButton");
let updateResult = document.getElementById("updateResult");
updateButton.addEventListener('click',function(){
    let updateUsername =document.getElementById("updateUsername").value;
    let update_url = "http://127.0.0.1:5000/api/member";

    fetch(update_url,{
        method:'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "name":updateUsername
        })
    })
        .then((response)=> {
            return response.json();
        })
        .then((data)=>{
            if (data.ok){
                updateResult.textContent= "更新成功";
            }
            else {
                updateResult.textContent= "更新失敗";
            }
        })
        // .catch((error)=>{
        //     console.log("連線出現錯誤")
        // })
})

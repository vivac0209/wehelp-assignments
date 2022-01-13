


function getData() {
   let req = new XMLHttpRequest();
   req.open("get","https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json",true);
   req.send();
   req.onload = function () {
      let data = JSON.parse(this.responseText);
      // console.log(data.result.results[0].stitle);
      
      add(data);
      // filterIamge(data);
      // splittest(data);

   }
}

getData();


//抓好文字存到陣列
   // let txtNode = [];
   // let files = [];
   // for (let i = 0; i<8; i++){
   //    let txt = `${data.result.results[i].stitle}`;
   //    txtNode.push(txt);
   //    let images1 = data.result.results[i].file;
   //    let firstUrl ='https'+ images1.split('https')[1];
   //    files.push(firstUrl);
   // }


function add(data){
   let a = 1;
   while (j = 0,j<8){
      if (a <= 8){
         let txtstitle = document.createElement('div');
         let pic = document.createElement('img');
         let title = document.createElement('p');
         document.querySelector(".boxArea").appendChild(txtstitle);
         txtstitle.setAttribute('class',`box`);

         let txt = `${data.result.results[a].stitle}`;
         title.textContent = (txt);

         let images = data.result.results[a].file;
         pic.src ='https'+ images.split('https')[1];
         txtstitle.appendChild(pic);
         txtstitle.appendChild(title);
         a++;
      } else{
         return;
      }
      j++;
   }
}

//抓網址用 分割字串
// function splittest(data){
//    let files = [];
//    for (let j=0; j<8; j++){
//       let images1 = data.result.results[j].file;
//       //console.log(images1);
//       let firstUrl ='https'+ images1.split('https')[1];
//       // console.log(firstUrl);
//       files.push(firstUrl);
//    }
//    // console.log(files);
// }

//抓圖片網址 正規表達式
// function filterIamge(data){
//    for (let i = 0; i<8; i++){
//       let images = data.result.results[i].file;
//       // console.log(typeof(images));
//       // console.log(images);
//       const reg = /(http(s?):)([/|.|\w|\s|-])*\.(?:jpg|gif|png|JPG)/
//       let x1= images.match(reg);
//       console.log(x1[0]);
//    }
   

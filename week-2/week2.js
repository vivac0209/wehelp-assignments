console.log("要求一：函式與流程控制")
function calculate(min, max){
    let sum = 0;
    const data = [];
    for (let i=min; i<max+1;i++){
        data.push(i);
    }
    //console.log(data);
    data.forEach(function (item) {
        sum+=item;
    })
    console.log(sum);
}

calculate(1, 3) 
calculate(4, 8)

console.log("要求二：Python 字典與列表、JavaScript 物件與陣列")


function avg(data){
    const c = data["employees"]
    let sum = 0;
    c.forEach(function (item,index) {
        sum+=item["salary"]; 
    })
    console.log(sum/c.length);
}

avg({
    "count":3,
    "employees":[
        {
        "name":"John",
        "salary":30000
        },
        {
        "name":"Bob",
        "salary":60000
        },
        {
        "name":"Jenny",
        "salary":50000
        }
        ]
});


console.log("要求三：找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。")

function maxProduct(nums){
    let max = [];
    for (let i =0; i < nums.length; i++){
        for (let j = i+1; j < nums.length; j++){
            max.push(nums[i]*nums[j]);
        }
    }
    const len = max.length;
    let max_value = max[len-1]
    for (let i = 0; i < len; i++){
        if (max[i]>max_value ){
            max_value = max[i]
        }
    }
    console.log(max_value);
}
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([-1, -2, 0])

console.log("要求四 ( 請閱讀英文 )：演算法");

function twoSum(nums, target){
    for (let i =0; i < nums.length; i++){
        for (let j = i+1; j < nums.length; j++){
            if (nums[i]+nums[j] == target){
                let result_txt = `show [${[i,j]}] because nums${i}+nums${j} is ${target}`;
                return result_txt;
            }
        }
    }
}

let result=twoSum([2, 11, 7, 15], 9);
console.log(result);

console.log("要求五 ( Optional )：演算法");
function maxZeros(nums){
    let max_time = [];
    let index_time = 0;
    nums.forEach(function(item){
        if (item == 0){
            index_time +=1;
            max_time.push(index_time);
        }else {
            index_time = 0;
            max_time.push(0);
        }
    })
    let max_result = Math.max.apply(null, max_time);
    console.log(max_result);
}
    
maxZeros([0, 1, 0, 0]);
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]);
maxZeros([1, 1, 1, 1, 1]);
maxZeros([0, 0, 0, 1, 1]);

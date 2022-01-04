print("要求一：函式與流程控制")

def calculate(min, max):
    sum = 0
    for x in range(min,max+1):
        sum+=x
    print(sum)

calculate(1, 3) 
calculate(4, 8) 

print("要求二：Python 字典與列表、JavaScript 物件與陣列")

def avg(data):

    salary = []

    for i in data["employees"]:
        salary.append(i)

    c = len(salary)
    total = 0
    for j in salary:
        total+=j["salary"]
    print(total/c)

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
})

print("要求三：找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。")

def maxProduct(nums):
    max = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            max.append(nums[i]*nums[j])
    
    max_value = 0
    for x in max:
        if max_value == 0 or x > max_value:
            max_value = x
    print(max_value)


maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([-1, -2, 0])

print("要求四 ( 請閱讀英文 )：演算法")

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                result_txt = "show {} because nums{}+nums{} is {}".format([i,j],i,j,target)
                return result_txt

result = twoSum([2, 11, 7, 15], 9)
print(result)

print("要求五 ( Optional )：演算法")

def maxZeros(nums):
    max_time = 0
    index_time = 0
    for i in nums:
        if i == 0:
            index_time += 1
            max_time = max(max_time, index_time)
        else:
            index_time = 0    
    print(max_time)

maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])
maxZeros([0, 0, 0, 1, 1])

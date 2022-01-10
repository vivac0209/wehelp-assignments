from typing import Pattern
import urllib.request as request
import json
import re
import csv

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data =json.load(response)           # 利用json 模組處理 json資料格式

all = data["result"]["results"]
a= []
with open("data.csv", mode="w",encoding="utf-8-sig",newline='') as file:
    for i in all:
        test = i["file"]
        l = re.compile(r'(https?://[^, "]*?\.(?:jpg|png|jpeg|JPG))')
        m = l.search(test)
        url = m.group()
        total = "{},{},{},{},{}\n".format(i["stitle"],i["address"][4:8],i["longitude"],i["latitude"],url)
        # total = i["stitle"]+","+ i["address"][4:8]+","+i["longitude"],i["latitude"]+","+ url
        print(total)
        # print(type(total))
        file.write(total)
        

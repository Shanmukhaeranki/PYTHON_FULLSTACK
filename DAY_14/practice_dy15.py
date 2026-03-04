
"""
#read a txt file
with open("sample.txt","r")as file:
    content=file.read()
    print(content)

#append txt file
with open("sample.txt","a")as file:
    
    file.write("\nfile oprations\n exceptional handling")    

#write in a txt file
with open ("sample.txt","w")as file:
    file.write("hello codegnan")


#read csv files

import csv
with open ("sample.csv","r")as file:
   data=csv.reader(file)
   for row in data:
       print(row[1])
  
#append in csv file
import csv
with open("sample.csv","a",newline="\n")as file:
    data=csv.writer(file)
    data.writerow(["5","chakri","pfs"])
    data.writerow(["6","jaya","pfs"])

    
#create new excel

import csv
with open("products.csv","w",newline="")as file:
    data=csv.writer(file)
    data.writerow(["product_ids","product_name","price"])
    data.writerow(["1","laptop","60k"])
    data.writerow(["2","Iphone","90k"])
    data.writerow(["3","chair","10k"])
    data.writerow(["4","headphones","10k"])
    data.writerow(["5","airpods","20k"])  

#read new excelfile
import csv
with open("products.csv","r")as file:
    data=csv.reader(file)
    for i in data:
        print(i)



#write json file


import json
with open ("demo.json","w")as file:
    data=[
    	{"id":"1","name":"shannu","batch":"pfs"},
	{"id":"2","name":"tagore","batch":"pfs"},
	{"id":"3","name":"saaketh","batch":"jfs"},
	{"id":"4","name":"nikhil","batch":"pfs"},
   
	
        ]
    json.dump(data,file,indent=2)
    print("data saved succesfully")



#read json file
import json
with open ("demo.json","r")as file:
    data=json.load(file)
    print(data)
 """


#append data in json
    
import json
with open ("demo.json","r")as file:
    data=json.load(file)
data.append({"id":"5","name":"chakri","batch":"pfs"})
with open("demo.json","w")as file:
    json.dump(data,file,indent=4)


























































































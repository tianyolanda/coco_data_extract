
# @Time    : 2018/1/18 10:46  
# @Author  : He Hangjiang  
# @Site    :   
# @File    : 根据目标图片id筛选图片.py  
# @Software: PyCharm  
  
import json  
import os  
import shutil
  
nameStr = []  
  
with open("COCO_train_oo3.json","r+") as f:  
    data = json.load(f)  
    print("read ready")  
  
for i in data:
    imgName = 'COCO_train2014_'+'000000' + str(i["filename"]) + ".jpg"  
    nameStr.append(imgName)  
  
nameStr = set(nameStr)  
print(nameStr)  
print(len(nameStr))  
  
# path = "/home/ogai1234/datasets/coco/train2014/"
path = "/home/ogai1234/datasets/coco/oo1/"
# delete from this path  
# for file in os.listdir(path):  
#      if(file not in nameStr):  
#         os.remove(path+file)  

# copy the file in new path2
for file in os.listdir(path):  
     if(file in nameStr):  
        # shutil.copyfile(path+file,path2+file) 
        os.remove(path+file)
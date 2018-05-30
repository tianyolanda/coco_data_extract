import json

# className = {
#     1:'person',
#     16:'bird',
#     17:'cat',
#     21:'cow',
#     18:'dog',
#     19:'horse',
#     20:'sheep',
#     5:'aeroplane',
#     2:'bicycle',
#     9:'boat',
#     6:'bus',
#     3:'car',
#     4:'motorbike',
#     7:'train',
#     44:'bottle',
#     62:'chair',
#     67:'dining table',
#     64:'potted plant',
#     63:'sofa',
#     72:'tvmonitor'
# }
className = {
    # 1:'person',
    # 2: 'bicycle',
    # 3: 'car',
    # 4:'motorcycle',
    5:'airplane',
    # 6:'bus',
    7:'train',
    # 8:'truck',
    9:'boat',
    17:'cat',
    # 18:'dog'
    19:'horse',
    20:'sheep',
    21:'cow',
    22:'elephant',
    23:'bear',
    24:'zebra',
    25:'giraffe',
    36:'snowboard',
    38:'kite',
    41:'skateboard',
    42:'surfboard',
    67:'dining table',
    59:'pizza',
    35:'skis',
    44:'bottle',
    46:'wine glass',
    47:'cup',
    48:'fork',
    49:'knife',
    50:'spoon',
    51:'bowl',
    52:'banana',
    53:'apple',
    54:'sandwich',
    55:'orange',
    56:'broccoli',
    57:'carrot',
    58:'hot dog',
    60:'donut',
    61:'cake'



}

# classNum = [1,2,3,4,5,6,7,9,16,17,18,19,20,21,44,62,63,64,67,72]
classNum = [5,7,9,17,19,20,21,22,23,24,25,36,38,41,42,67,59,35,44,46,47,48,49,50,51,52,53,54,55,56,57,58,60,61]
def writeNum(Num):
    with open("COCO_train_oo2.json","a+") as f:
        f.write(str(Num))

# with open("instances_val2014.json","r+") as f:
#     data = json.load(f)
    # annData = data["annotations"]
    # print(annData[0])
    # for x in annData[0]:
    #     if(x == "image_id"):
    #         print(type(x))
    #         print(x+ ":" + str(annData[0][x]))
    #     if (x == "image_id" or x == "bbox" or x == "category_id"):
    #         print(x + ":" + annData[0][x])
    #     if (x == "image_id" or x == "bbox" or x == "category_id"):
    #         print(x+ ":" + annData[0][x])

# with open("test.json","w") as f:
#     json.dump(annData, f, ensure_ascii=False)

inputfile = []
inner = {}
##向test.json文件写入内容
with open("instances_train2014.json","r+") as f:
    allData = json.load(f)
    data = allData["annotations"]
    print(data[1])
    print("read ready")

for i in data:
    if(i['category_id'] in classNum):
        inner = {
            "filename": str(i["image_id"]).zfill(6),
            "name": className[i["category_id"]],
            "bndbox":i["bbox"]
        }
        inputfile.append(inner)
inputfile = json.dumps(inputfile)
writeNum(inputfile)
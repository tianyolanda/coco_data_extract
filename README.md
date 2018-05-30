# coco_data_extract
extract particular catalogs images and annotations from  COCO data-set

- parse1.py: extract the catalogs you want form 'instances_train2014.json', save to 'COCO_train_oo2.json'
- parse2.py: according to the image name in 'COCO_train_oo2.json', copy the included image from 'path' to 'path2'. Note that the image name must be 'COCO_train2014_'+'000000' + 'some 6 length numbers'
- parse3.py: extract the annotation information from 'COCO_train_oo2.json', change and save as PASCAL VOC format '.xml' format for each image.

All the path and file name in this code need to change.

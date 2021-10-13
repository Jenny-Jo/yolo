# yolo 경로 수정해야 함
%cd C:/Users/coco7/yolov5
%run train.py --img 640 --batch 8 --epochs 50 --data C:/dataset/yz_tile_resize_split_blur/data.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --name results --device 0
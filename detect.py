from IPython.display import Image
import os
# yolo 경로 수정해야 함
%cd C:/Users/coco7/yolov5

# test할 이미지 경로도 따로 지정해줘야 함.
# weights 경로는 학습할 때마다 매번 달라져서 매번 고쳐줘야 함.
test_img_path = test_img_list[1]
!python detect.py --weights ./runs/train/results21/weights/best.pt --img 416 --conf 0.5 --source {test_img_path}

from glob import glob
import yaml
import zipfile



# 데이터셋 경로 설정
root='C:/dataset/yz_tile_resize_split_blur'
zip_file=zipfile.ZipFile(root+'.zip')
zip_file.extractall()

# 데이터셋 별로 경로를 변수에 저장하기
train_img_list = glob(root+'/train/images/*.jpg')
test_img_list = glob(root+'/test/images/*.jpg')
val_img_list = glob(root+'/valid/images/*.jpg')

# print(len(train_img_list), len(test_img_list), len(val_img_list))


# 데이터셋 경로를 메모장에 담아 저장하기.
with open('./train.txt','w') as f:
    f.write('\n'.join(train_img_list)+'\n')

with open('./val.txt','w') as f:
    f.write('\n'.join(val_img_list)+'\n')


with open('./test.txt','w') as f:
    f.write('\n'.join(test_img_list)+'\n')

# 데이터 yaml 파일에 넣을 데이터셋 경로를 정의한 dictionary 만들기
temp = {}
temp['path']= root
temp['train']=root+'/train.txt'
temp['val']= root+'/valid.txt'
temp['test']=root+'/test.txt'
temp['nc'] ='1'
temp['names']=['A']
# print(temp)

# yaml file 열어서 dictionary 적어두기
with open('./data.yaml','w') as f:
    yaml.dump(temp,f)

from multiprocessing import Pool
import os
import time
from PIL import Image

def get_file_path(path):
    img_paths = []
    dirs = os.listdir(path)
    #print(dirs)
    for file_dir in dirs:
        file_path = os.path.join(path, file_dir)
        #print(file_path)
        img_paths.append(file_path)
    return img_paths

def test_map(file_name):
    print(file_name)

def resize_image(file_name):
    print("resize_image")
    print(file_name)
    try:
        #image process block
        '''
        img = Image.open(file_name)
        new_img = img.rotate(90)
        new_img.save(file_name)
        '''
    except:
        print(file_name)
#single 21.43
#multi 6.48
if __name__ == '__main__':
    start = time.time()
    path = 'D:/zbw/Train2_test1/'
    img_paths = get_file_path(path)
    print(img_paths)
    pool = Pool()
    pool.map(resize_image, img_paths)
    pool.close()
    pool.join()
    '''
    单进程
    res = map(resize_image, img_paths)
    #Python3 返回迭代器，之后需要遍历才能得到结果
    #Python2 未尝试
    for i in res:
        print(i)
    '''
    end = time.time()
    print(end - start)
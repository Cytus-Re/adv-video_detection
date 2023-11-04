import torch
import os
import numpy as np
import cv2



def convert(rgb_tensor):
    yuv_data = np.empty((32, 336, 224), dtype=np.uint8)
    for i in range(32):
        rgb_data_scaled = (np.array(rgb_tensor * 255)).astype(np.uint8)
        yuv_data[i]  = cv2.cvtColor(rgb_data_scaled[i], cv2.COLOR_RGB2YUV_I420)
    return yuv_data


dst = './yuv'
clas = ['adv', 'clean'] # ['Double', 'Single']
for cla in clas:
    idx = 0
    save_path = os.path.join(dst, cla)
    for src in os.listdir(f'./{cla}'):
        src = os.path.join(f'./{cla}/{src}', 'none/data.pth')
        # print(src)
        if(os.path.exists(src)):
            data = torch.load(src)['adv_images']
            data = torch.squeeze(data)
            # print(data.shape)
            data = data.permute(1, 2, 3, 0)
            # print(data.shape)
            yuv_data = convert(data)
            with open(f'{save_path}/{idx}.yuv', 'wb') as f:
                yuv_data.tofile(f)
            print(f'write file {save_path}/{idx}.yuv')
            idx += 1
        else:
            print(f'{src}不存在')

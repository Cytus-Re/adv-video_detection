import os
x265_path = r'D:\Lab\En-Decode\tools\x265\x265.exe' # windows
width, height = 224, 224
root_yuv_folder = r'./yuv'
dst_folder = r'./h265'

clas = ['adv', 'clean']
for cla in clas:
    src_yuv_folder = os.path.join(root_yuv_folder, cla)
    dst_h265_folder = os.path.join(dst_folder, cla)
    if not os.path.exists(dst_h265_folder):
        os.mkdir(dst_h265_folder)
    src_yuv_list = list(os.listdir(src_yuv_folder))
    src_yuv_num = len(src_yuv_list)

    gop_size = 4
    qp_value = 30

    for i, src_yuv_name in enumerate(src_yuv_list):
        if not src_yuv_name.endswith('.yuv'):
            continue
        video_name = src_yuv_name[:src_yuv_name.find('.yuv')]
        src_yuv_path = f'{src_yuv_folder}/{src_yuv_name}'
        output_h265_filename = f'{video_name}.h265'
        output_h265_file_path = f'{dst_h265_folder}/{output_h265_filename}'
        command = f'{x265_path} --input {src_yuv_path} --fps 32 --input-res {width}x{height} --rect --amp --keyint {gop_size} --min-keyint {gop_size} --bframes 0 --qp {qp_value} -o {output_h265_file_path}'
        print(f'({i+1}/{src_yuv_num}) {command}')
        os.system(command)
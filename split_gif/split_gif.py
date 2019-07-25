import PIL.Image as Image
import os


def gif_split(path):
    # ############################
    # 这部分用于建立一个文件夹，以便存放拆解的图片
    save_path = path[:-4]
    try:
        os.mkdir(save_path)
    except:
        pass
    # ############################
    img = Image.open(path)
    try:
        i = 0
        while True:
            print('正在拆解第{}帧...'.format(i))
            img.seek(i)
            img.save('{}/'.format(save_path) + str(i) + '.bmp')
            i += 1
    except:
        pass
    return save_path, i


if __name__ == '__main__':
    path = 'hehe.gif'
    save_path, i = gif_split(path)
    print('拆解完成，共得到{}张图片。所属文件:{}'.format(i, save_path))

from PIL import Image

matrix = (14, 16)  # 14rows, 16cols 块型矩阵表述大小

with open('img.jpg', 'rb') as f:
    image = Image.open(f, 'r')
    assert isinstance(image, Image.Image)

    block_size = (image.size[0] / matrix[1], image.size[1] / matrix[0])
    # mage.width/matrix.col , image.height / matrix.row
    # block_size 是先宽后高
    print(block_size)

    x = block_size[0] / 2  # 其实是blocksize的一半
    y = block_size[1] / 2  # 从每个矩阵快中间开始算
    pxs = []
    # 竖着取样呢，
    while x < image.width:
        while y < image.height:
            px = image.getpixel((x, y))
            if px[0] + px[1] + px[2] > 460:
                pxs.append(0)
            else:
                pxs.append(1)
            y += block_size[1]
        y = 4
        x += block_size[0]
    print('竖取样结果')
    print(pxs)
#==========================================================
    pys = []
    x = block_size[0] / 2  # 其实是blocksize的一半
    y = block_size[1] / 2
    while y < image.height:
        while x < image.width:
            px = image.getpixel((x, y))
            if px[0] + px[1] + px[2] > 460:  # 认为是亮色，亮色取0，深色取1
                pys.append(0)
            else:
                pys.append(1)
            x += block_size[0]
        x = 4
        y += block_size[1]
    print("横取样结果")
    print(pys)

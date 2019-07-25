import base64

html_head = 'data:image/jpeg;base64,'

with open('base64.txt', 'r') as f:
    base64_str = f.read()
b_all = base64.b64decode(base64_str)
key = b_all[6:10].decode()

if key == 'JFIF':
    with open('output.jpg', 'wb') as f:
        f.write(b_all)
    with open('output.html', 'w') as f:
        html_all = '<img src="' + html_head + base64_str + '">'
        print(html_all)
        f.write(html_all)

else:
    # 不知道啥类型文件
    with open('output.unknown', 'wb') as f:
        f.write(b_all)

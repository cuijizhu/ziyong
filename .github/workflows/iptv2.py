import os
import requests
import re

# 用于下载并转换文件的函数
def download_and_convert(url):
    r = requests.get(url)
    r.raise_for_status()

    content = r.text
    lines = content.split('\n')
    formatted_lines = []

    # 忽略 '#EXTM3U' 开头的行
    lines = [line for line in lines if not line.startswith('#EXTM3U')]

    for i in range(0, len(lines) - 1, 2):
        match = re.search('"(.*?)",', lines[i])
        if match:
            name = match.group(1)
            link = lines[i + 1].strip()
            formatted_lines.append(f"{name},{link}")

    return '\n'.join(formatted_lines)


m3u_links = [
    'https://raw.githubusercontent.com/iptv-org/iptv/master/streams/kr.m3u',
    'https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/IPTV.m3u',
    'https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/bestv.m3u'
]

# 如果 iptv2.txt 存在，删除它
if os.path.exists('iptv2.txt'):
    os.remove('iptv2.txt')

# 从 gxtv.txt 复制内容到 iptv2.txt
with open('gxtv.txt', 'r') as f1, open('iptv2.txt', 'w') as f2:
    f2.write(f1.read())

# 下载并转换每个 m3u 文件，然后追加到 iptv2.txt
for link in m3u_links:
    filename = os.path.basename(link)
    name, _ = os.path.splitext(filename)
    formatted_content = download_and_convert(link)
    with open('iptv2.txt', 'a') as f:
        f.write(formatted_content + '\n')

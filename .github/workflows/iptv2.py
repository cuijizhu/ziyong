import requests
import re

# 您要抓取的直播源链接
links = [
    "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/kr.m3u",
    "https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/IPTV.m3u",
    "https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/bestv.m3u",
]

def process_link(link):
    genre = link.split('/')[-1].split('.')[0] # 获取文件名作为genre
    content = requests.get(link).text.splitlines()
    new_content = []
    for i in range(0, len(content)-1, 2): # 每两行为一个单元进行处理
        if content[i].startswith('#EXTINF'): # 确保此行是正确的信息行
            # 使用正则表达式提取频道名和频道链接
            channel_name = re.search(r',(.*)', content[i]).group(1)
            channel_link = content[i+1]
            new_content.append(','.join([genre, channel_name, channel_link]))
    return new_content

# 将已有的文件内容读入
with open('gxtv.txt', 'r') as f:
    old_content = f.read().splitlines()

# 处理新的直播源链接并与旧的内容合并
new_content = []
for link in links:
    new_content += process_link(link)
total_content = old_content + new_content

# 将合并后的内容保存为新的文件
with open('iptv2.txt', 'w') as f:
    for line in total_content:
        f.write(line+'\n')

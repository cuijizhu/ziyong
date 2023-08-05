import requests
import re

def download_and_convert(url):
    r = requests.get(url)
    r.raise_for_status()

    content = r.text
    lines = content.split('\n')
    formatted_lines = []

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

# 下载和转换所有m3u链接的内容
merged_content = ""
for link in m3u_links:
    formatted_content = download_and_convert(link)
    merged_content += formatted_content + '\n'

# 将合并后的内容保存到iptv2.txt文件
with open('iptv2.txt', 'w') as f:
    f.write(merged_content)

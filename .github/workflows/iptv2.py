import requests
import re
import os

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

# Copy content from gxtv.txt to iptv2.txt
with open('gxtv.txt', 'r') as f1, open('iptv2.txt', 'w') as f2:
    f2.write(f1.read())

# Download and convert each m3u file, then append to iptv2.txt
for link in m3u_links:
    filename = os.path.basename(link)
    name, _ = os.path.splitext(filename)
    formatted_content = download_and_convert(link)
    with open('iptv2.txt', 'a') as f:
        f.write(name + ',#genre#\n' + formatted_content + '\n')

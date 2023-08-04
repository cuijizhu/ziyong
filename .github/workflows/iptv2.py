import requests
import re

def download_and_convert(url, filename):
    r = requests.get(url)
    r.raise_for_status()

    content = r.text
    lines = content.split('\n')
    formatted_lines = []
    genre = url.split('/')[-1].replace('.m3u', '')
    formatted_lines.append(f"{genre},#genre#\n")

    for i in range(0, len(lines) - 1, 2):
        match = re.search('"(.*?)",', lines[i])
        if match:
            name = match.group(1)
            link = lines[i + 1].strip()
            formatted_lines.append(f"{name},{link}\n")
    
    with open(filename, 'a') as f:
        f.write('\n'.join(formatted_lines))

# Copy content from gxtv.txt to iptv2.txt
with open('gxtv.txt', 'r') as f1, open('iptv2.txt', 'w') as f2:
    f2.write(f1.read())

# The list of m3u file links to download and convert
m3u_links = [
    'https://raw.githubusercontent.com/iptv-org/iptv/master/streams/kr.m3u',
    'https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/IPTV.m3u',
    'https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/bestv.m3u'
]

for link in m3u_links:
    download_and_convert(link, 'iptv2.txt')

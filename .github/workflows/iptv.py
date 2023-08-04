import requests

def parse_m3u(m3u_url):
    response = requests.get(m3u_url)
    lines = response.text.strip().split('\n')
    parsed_entries = []

    for i in range(len(lines)):
        if lines[i].startswith('#EXTINF:-1'):
            name = lines[i].split('tvg-id="')[-1].split('",')[1].strip()
            url = lines[i + 1].strip()
            parsed_entries.append(f"{name},{url}")
    
    return parsed_entries

m3u_urls = [
    "https://raw.githubusercontent.com/cuijizhu/clash/main/gxtv.m3u",
    "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/kr.m3u",
    "https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/bestv.m3u",
    "https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/IPTV.m3u"
]

output = "iptv.txt"

with open(output, 'w', encoding='utf-8') as outfile:
    for i, url in enumerate(m3u_urls):
        filename = url.split('/')[-1].split('.m3u')[0]
        genre = '#genre#'
        outfile.write(f"{filename},{genre}\n")
        parsed_entries = parse_m3u(url)
        for entry in parsed_entries:
            outfile.write(entry + "\n")

print("转换完成！请查看iptv.txt文件。")

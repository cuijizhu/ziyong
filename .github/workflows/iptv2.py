import requests
import re

URLS = [
    "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/kr.m3u",
    "https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/IPTV.m3u",
    "https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/bestv.m3u"
]

def extract_channels(content):
    lines = content.split("\n")
    channels = []
    
    for i in range(len(lines)):
        if lines[i].startswith("#EXTINF"):
            parts = lines[i].rsplit(",", 1)  # 使用rsplit从右边分隔一次，这样就能获取最后一个逗号后面的内容
            if len(parts) == 2:
                name = parts[1].strip()  # 这就是频道名称
                url = lines[i + 1].strip()
                channels.append(f"{name},{url}")
    return channels

def main():
    all_channels = []

    for url in URLS:
        response = requests.get(url)
        all_channels.extend(extract_channels(response.text))

    with open("gxtv.txt", "r") as file:
        existing_channels = file.readlines()

    with open("iptv2.txt", "w") as file:
        for channel in all_channels:
            file.write(channel + "\n")
        for channel in existing_channels:
            file.write(channel)

if __name__ == "__main__":
    main()

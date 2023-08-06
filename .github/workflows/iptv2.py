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
            match = re.search(r'(?<="|,)[^",]+(?="|,)', lines[i])
            if match:
                name = match.group()
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

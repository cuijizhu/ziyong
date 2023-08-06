import requests

URLS = [
    ("https://raw.githubusercontent.com/iptv-org/iptv/master/streams/kr.m3u", "韩国IPTV,#genre#"),
    ("https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/IPTV.m3u", "4K/8K,#genre#"),
    ("https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/bestv.m3u", "百事通,#genre#")
]

def extract_channels(content, genre):
    lines = content.split("\n")
    channels = [genre]  # 把类型作为第一行加入

    for i in range(len(lines)):
        if lines[i].startswith("#EXTINF"):
            parts = lines[i].rsplit(",", 1)
            if len(parts) == 2:
                name = parts[1].strip()
                url = lines[i + 1].strip()
                channels.append(f"{name},{url}")
    return channels

def main():
    all_channels = []

    with open("gxtv.txt", "r") as file:
        existing_channels = [line.strip() for line in file if line.strip()]
        all_channels.extend(existing_channels)

    for idx, (url, genre) in enumerate(URLS):
        response = requests.get(url)
        if idx > 0:  # 如果不是第一个链接，添加一个空行来区分
            all_channels.append('')
        all_channels.extend(extract_channels(response.text, genre))

    with open("iptv2.txt", "w") as file:
        for channel in all_channels:
            file.write(channel + "\n")

if __name__ == "__main__":
    main()

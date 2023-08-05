import requests

# 从给定的URL获取直播源内容
def get_m3u_content(url):
    response = requests.get(url)
    return response.text

# 将直播源内容转换成指定格式
def convert_to_iptv2_format(m3u_content):
    lines = m3u_content.splitlines()
    converted_lines = []

    for i in range(0, len(lines), 2):
        info_line = lines[i].split(' tvg-id="', 1)[1].split('",', 1)[1].strip()
        url_line = lines[i+1].strip()
        converted_lines.append(f"{info_line},{url_line}")

    return '\n'.join(converted_lines)

# 将转换后的内容保存到iptv2.txt文件
def save_to_iptv2_file(content):
    with open('iptv2.txt', 'w') as file:
        file.write(content)

# 主函数
def main():
    urls = [
        'https://raw.githubusercontent.com/iptv-org/iptv/master/streams/kr.m3u',
        'https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/IPTV.m3u',
        'https://raw.githubusercontent.com/Ftindy/IPTV-URL/main/bestv.m3u'
    ]

    merged_content = ""
    for url in urls:
        m3u_content = get_m3u_content(url)
        converted_content = convert_to_iptv2_format(m3u_content)
        merged_content += converted_content + '\n'

    save_to_iptv2_file(merged_content)

if __name__ == "__main__":
    main()

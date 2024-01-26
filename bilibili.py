from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from bs4 import BeautifulSoup

# Edge浏览器驱动程序的路径
edgedriver_path = r'G:\python\edgedriver_win64\msedgedriver.exe'

# 创建Edge浏览器的WebDriver对象
driver = webdriver.Edge(service=Service(edgedriver_path))

# 目标网页的URL，替换uid，暂时不想写加页数
url = 'https://space.bilibili.com/1136087954/video'

# 打开
driver.get(url)

# 等待页面加载完成
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'small-item')))

# 使用WebDriver解析网页内容
html = driver.page_source

# 关闭浏览器
driver.quit()

# 解析网页内容
soup = BeautifulSoup(html, 'html.parser')

# 找标签
video_items = soup.find_all('li', class_='small-item fakeDanmu-item')

# 存储爬取的视频数据
video_data = []

# 遍历
for item in video_items:
    # 获取视频链接
    link = item.find('a', class_='cover')['href']

    # 获取播放量和日期
    meta = item.find('div', class_='meta')
    play = meta.find('span', class_='play').find('span').text
    time = meta.find('span', class_='time').text

    # 构造视频数据字典
    video = {
        'link': link,
        'play': play,
        'time': time
    }

    # 将视频数据添加到列表中
    video_data.append(video)

# 将视频数据保存为JSON文件,这里替换地址
output_file = 'G:/python/demo/videos.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(video_data, f, ensure_ascii=False, indent=4)

print(f"视频数据已保存到文件：{output_file}")

import json
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

edgedriver_path = r'G:\python\edgedriver_win64\msedgedriver.exe'

# 读取前一个json文件的视频数据
input_file = r'G:\python\demo\videos.json'
with open(input_file, 'r', encoding='utf-8') as f:
    video_data = json.load(f)

# 创建Edge浏览器的WebDriver对象
driver = webdriver.Edge(service=Service(edgedriver_path))

# 遍历视频数据
for video in video_data:
    # 获取视频链接
    link = 'https:' + video['link']

    # 打开视频链接
    driver.get(link)

    # 等待页面加载完成
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tag-link')))

    # 使用WebDriver解析网页内容
    html = driver.page_source

    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(html, 'html.parser')

    # 找到全部的标签
    tags = soup.find_all('a', class_='tag-link')

    # 提取标签文本
    tag_list = [tag.text for tag in tags]

    # 将标签列表添加到视频数据中
    video['tags'] = tag_list

# 关闭浏览器
driver.quit()

# 打印爬取的视频数据
for video in video_data:
    print('视频链接:', video['link'])
    print('播放量:', video['play'])
    print('发布日期:', video['time'])
    print('标签:', video['tags'])
    print('---')

# 将更新后的视频数据保存为JSON文件
output_file = r'G:\python\demo\videos_with_tags.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(video_data, f, ensure_ascii=False, indent=4)

print(f"视频数据已保存到文件：{output_file}")

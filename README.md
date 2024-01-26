# Reptile
基于selenium的b站up主视频数据爬虫，爬地址，跟播放量，日期，还有tag作为运营工具用，
先运行第一个Python文件，如果出现要登录的话，就在这段
driver.get(url)
#这个是要加的代码，加这个代码记得要在上面导入import time 这个模块
time.sleep(30)
# 等待页面加载完成
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'small-item')))

抓完这个json文件就运行第二个爬虫，抓视频的tag
补充，自己下载浏览器驱动

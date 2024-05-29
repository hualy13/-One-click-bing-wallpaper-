import os
import requests
from bs4 import BeautifulSoup
import ctypes
from PIL import Image
from io import BytesIO
import time
import sys

# 定义一个结构体，用于设置窗口状态
class HWND(ctypes.Structure):
    _fields_ = [("handle", ctypes.c_void_p)]

# 获取当前窗口的句柄
handle = HWND(ctypes.windll.kernel32.GetConsoleWindow())

# 隐藏窗口
ctypes.windll.user32.ShowWindow(handle.handle, 0)

max_retries = 10
retry_count = 0
sleep_time = 60  # 1分钟

# 获取当前脚本文件的目录
current_directory = os.path.dirname(os.path.abspath(__file__))

while retry_count < max_retries:
    try:
        # 发送HTTP请求获取网页内容
        url = "https://www.todaybing.com/"
        response = requests.get(url)
        response.raise_for_status()  # 确保请求成功

        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, "html.parser")

        # 找到下载链接的<a>标签
        download_link = soup.find("a", {"class": "text-white btn btn-sm btn-primary"})

        # 如果找到了元素，则提取链接属性
        if download_link:
            download_url = download_link.get("href")
            print("下载链接:", download_url)

            # 下载图片
            response = requests.get(download_url)
            response.raise_for_status()  # 确保下载成功

            # 将图片内容保存到内存中
            img = Image.open(BytesIO(response.content))

            # 定义保存地址为png格式，保存到当前目录
            save_path = os.path.join(current_directory, "todaybing_wallpaper.png")
            img.save(save_path, "PNG")
            print("图片已保存为", save_path)

            # 设置为桌面背景
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, save_path, 3)
            print("已将图片设置为桌面背景")

            # 如果代码成功执行，则跳出循环
            break

        else:
            print("未找到相关的元素")

        retry_count += 1
        print(f"第 {retry_count} 次尝试失败，等待 {sleep_time} 秒后再尝试...")
        time.sleep(sleep_time)

    except Exception as e:
        print("出现错误:", e)
        retry_count += 1
        print(f"第 {retry_count} 次尝试失败，等待 {sleep_time} 秒后再尝试...")
        time.sleep(sleep_time)

# 关闭当前窗口
sys.exit()

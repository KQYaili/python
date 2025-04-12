# 包
# 包是含有__init__.py的文件
import math
import os
import random
import threading
import time
from timeit import timeit, Timer
import re

# def outer(fn):
#     def inner(name):
#         print(f"{name}登陆....")
#         print("hh")
#         return fn(name)  # Ensure fn returns a value
#     return inner
#
# def deco(fn):
#     def inner(name):
#         result = fn(name)
#         return f"{name}" + result  # Ensure concatenation is done with strings
#     return inner
#
# @deco
# @outer
# def send(name):
#     return "Hello World"
#
# print(send("linablog"))


# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# func("linablog", "aaa", name='kwargs')
# with open('test.txt','w+') as f:
#     f.write('hello world')
#     f.write("initlog")
#     print(f.read())
#     print(f.close())
#     print(f)
# print(f.close())
# with open("C:\\Users\\51392\\Pictures\\60142aeba0a2c938b33f78a88758d646.jpg",'rb') as file:
#     img=file.read()
#     print(img)
# import os
# os.rename('test.txt','test2.txt')
# os.remove('test2.txt')
# import os
# print(os.getcwd())
# print(os.listdir())
# from collections.abc import Iterable
# from turtle import st
#
#
# def factorial(n):
#
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(998))
#
# print(isinstance('123',Iterable))
# def sing():
#     print(f"sing子进程编号：{os.getpid()},父进程编号：{os.getppid()}")
#     print("唱歌")
# def dance():
#     print(f"dance子进程编号：{os.getpid()},父进程编号：{os.getppid()}")
#     print()
#
# if __name__ == '__main__':
#     p1=threading.Thread(target=sing)
#     p2=threading.Thread(target=dance)
#     p1.start()
#     p2.start()
# import threading
# import time
#
# def task1():
#     print("任务 1 开始")
#     time.sleep(2)  # 模拟耗时操作
#     print("任务 1 结束")
#
# def task2():
#     print("任务 2 开始")
#     time.sleep(1)  # 模拟耗时操作
#     print("任务 2 结束")
#
# # 创建线程
# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)
#
# # 启动线程
# t1.start()
# t2.start()
#
# # 等待线程 t1 执行完成
# t1.join()
# print("主线程：任务 1 已完成")
#
# # 等待线程 t2 执行完成
# t2.join()
# print("主线程：任务 2 已完成")
#
# print("主线程：所有线程已完成")
# import threading
#
# def print_numbers():
#     for i in range(5):
#         print(i, end=" ")
#
# # 创建线程
# t = threading.Thread(target=print_numbers)
#
# # 启动线程
# t.start()
#
# # 等待线程完成
# # t.join()
#
# print("\n线程完成后，继续执行主线程")
# import threading
# import time
#
# def long_task():
#     print("长任务开始")
#     time.sleep(5)  # 模拟耗时操作
#     print("长任务结束")
#
# # 创建线程
# t = threading.Thread(target=long_task)
# t.start()
#
# # 等待最多 2 秒
# t.join(timeout=2)
# print("主线程：不再等待，继续执行")
# import numpy as np
# import matplotlib.pyplot as plt
# def python_sum(n):
#     a=[i**2 for i in range(n)]
#     b=[i**3 for i in range(n)]
#     ab_sum=[]
#     for i in range(n):
#         ab_sum.append(a[i]+b[i])
#     return ab_sum
# print(python_sum(10))
# def numpy_sum(n):
#     a=np.arange(n)**2
#     b=np.arange(n)**3
#     return a+b
# print(numpy_sum(10))
# res=re.math('[a-zA-Z','Hello')
# print(res.group)
# import numpy as np
# print(np.arange(0, 11, 2))
# from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
#
# app = Flask(__name__)
# app.secret_key = '<KEY>'
# @app.route('/')
# def index():
#     return "<p>hello world</p>"
# if __name__=='__main__':
#     app.run(debug=True)
# import numpy as np
# def compute_error_for_line_given_points(b,w,points):
#     totalError = 0
#     for point in points:
#         x=point[0]
#         y=point[1]
#         totalError+=(w*x+b-y)**2
#     return totalError/float(len(points))
# def step_gradient(b,w,points,learning_rate):
#     b_gradient=0
#     w_gradient=0
#     N=float(len(points))
#     for point in points:
#         x=point[0]
#         y=point[1]
#         b_gradient+=2*(w*x+b-y)
#         w_gradient+=2*x*(w*x+b-y)
#     new_b=b-b_gradient*learning_rate/N
#     new_w=w-w_gradient*learning_rate/N
#     return new_b,new_w
# def gradient_descent(b,w,points,learning_rate,num_iterations):
#     for i in range(num_iterations):
#         b,w=step_gradient(b, w, np.array(points), learning_rate)
#     return b,w
# def run():
#     points=np.genfromtxt('data.csv',delimiter=',')
#     learning_rate=0.0001
#     initial_b=0
#     initial_w=0
#     num_iterations=1000
#     print("Starting gradient descent at b={0},w={1},error={2}"
#           .format(initial_b,initial_w,
#                   compute_error_for_line_given_points(initial_b,initial_w,points))
#           )
#     print("Running...")
#     b,w=gradient_descent(initial_b,initial_w,points,learning_rate,num_iterations)
#     print("After {0} iterations, b={1},w={2},error={3}"
#           .format(num_iterations,b,w,compute_error_for_line_given_points(b,w,points))
#           )
# if __name__ == '__main__':
#     run()
# t = int(input())
# for i in range(t):
#     n = int(input())
#     print(bool(n % 2))
# import os
# print(os.name)
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys  # 输入框回车
# from selenium.webdriver.common.by import By  # 与下面的2个都是等待时要用到
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, TimeoutException  # 异常处理
# from selenium.webdriver.chrome.options import Options
# import re
# import os
#
#
# class NetEaseCloud(object):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
#              AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
#
#     def __init__(self):
#         pass
#         # self.download_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
#
#     def get_html(self, request_url):  # 得到页面的html
#         try:
#             response = requests.get(request_url, headers=NetEaseCloud.headers, timeout=20)
#             if response.status_code == 200:
#                 return response
#         except TimeoutError:
#             print("请求超时！")
#             return None
#         except Exception as er:
#             print("其他错误：", er)
#             return None
#
#     def get_id(self):
#         try:
#             song_id = wait.until(
#                 EC.presence_of_all_elements_located(
#                     (By.XPATH, '//body/div[@class="g-bd"]/div/div[2]/div[2]/div/div/div[*]/div[2]/div/div/a')))
#             title = wait.until(
#                 EC.presence_of_all_elements_located(
#                     (By.XPATH, '//body/div[@class="g-bd"]/div/div[2]/div[2]/div/div/div[*]/div[2]/div/div/a/b')))
#             author = wait.until(
#                 EC.presence_of_all_elements_located(
#                     (By.XPATH, '//body/div[@class="g-bd"]/div/div[2]/div[2]/div/div/div[*]/div[4]/div/a')))
#             ids = []
#             titles = []
#             authors = []
#             num = 1
#             print("为你找到以下内容".center(30, '*'))
#             print("序号     ", "歌名                              ", "         歌手", "        歌曲链接")
#             for i in range(0, len(song_id)):
#                 try:
#                     ids.append(song_id[i].get_attribute("href"))  # 这儿是歌曲的id
#                     titles.append(title[i].get_attribute('title'))  # 这是歌名
#                     authors.append(author[i].get_attribute('textContent'))  # 这是歌手
#                     print(num, "     ", titles[i], "     ", authors[i], "    ", ids[i])
#                     num += 1
#                 except:
#                     pass
#             # print("没到这儿吗")
#             is_index = int(input("\n选择下载序号>>").strip())
#             if is_index < 0:
#                 print("您已取消该歌曲的下载")
#                 return None
#             song_id = re.compile('htt.*?id\=(\d+)').findall(ids[is_index - 1])[0]  # 将歌曲id匹配出来
#             song_name = titles[is_index - 1]
#             # print("正在下载......")
#             return song_id, song_name
#         except TimeoutException:
#             print("网络不佳，请重新下载")
#             return None
#         except NoSuchElementException:
#             print("没有找到相关资源QAQ")
#             return None
#         except Exception as er:
#             print("检测到异常错误，请重新下载： ", er)
#             return None
#
#     def download(self, song_id, song_name):
#         # song_id, song_name = NetEaseCloud.get_id()
#         download_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)  # 歌曲下载的接口
#         try:
#             song_html = self.get_html(download_url)  # 访问下载页
#             song_data = song_html.content  # 得到下载页的html.content(即歌曲数据的字节)
#         except TimeoutError:
#             print("检测到网络异常\n退出网易云音乐下载")
#             return
#         except:
#             print("检测到异常\n退出网易云音乐下载")
#             return
#         try:
#             save_path = 'music/{}.mp3'.format(song_name)
#             true_path = os.path.abspath(save_path)  # 绝对路径
#             print("下载中......")
#             with open(save_path, 'wb') as f:
#                 try:
#                     f.write(song_data)
#                     print("{}已保存至{}".format(song_name, true_path))
#                 except Exception as er:
#                     print("写入失败：", er)
#         except Exception as err:
#             print("文件找不到目录music：", err)
#
#     def test(self, song_name):
#         songs_name = []
#         remove_str = ['/', '\\']
#         for name in song_name:
#             if name not in remove_str:
#                 songs_name.append(name)
#             else:
#                 name = '&'
#                 songs_name.append(name)
#         song_string = ''.join(songs_name)
#         return song_string
#
#     def net_ease_cloud_api(self):
#         print("\n", "{:30}".format("正在使用网易云音乐VIP下载器"))
#         try:
#             url = "https://music.163.com/#/search/m/?s=长安忆&type=1"
#             driver.get(url)
#         except:
#             print("网络连接异常！")
#             return  # 利用return阻断程序
#         try:
#             driver.switch_to.frame('g_iframe')
#             while True:
#                 name_tar = input("\n请输入歌名>>").strip()
#                 print("\n正在努力寻找资源.....")
#                 if name_tar == 'q':
#                     print("\n退出网易云音乐下载")
#                     break
#                 elif name_tar == '':
#                     continue
#                 else:
#                     try:
#                         input_box = wait.until(
#                             EC.element_to_be_clickable((By.XPATH, '//body/div[@class="g-bd"]/div/div/input')))
#                         input_box.clear()
#                         input_box.send_keys(name_tar)
#                         input_box.send_keys(Keys.ENTER)
#                     except NoSuchElementException:
#                         print("\n没有找到相关资源QAQ")
#                         return  # 设置阻断
#                     song_id, song_name = self.get_id()  # 此时的song_name可能含有字符/,写文件时会报路径错误，所以要想验证
#                     if song_id is None or song_name is None:
#                         break  # 这个None是用户不想下载时返回的
#                     else:
#                         song_name = self.test(song_name)  # 若含有/或者\则转化为&
#                         self.download(song_id, song_name)
#         except Exception as er:
#             print("检测到异常错误\n退出网易云音乐下载 ", er)
#
#
# if __name__ == '__main__':
#     net_API = NetEaseCloud()
#     print("{:^30}".format("欢迎使用VIP音乐破解"))
#     if not os.path.exists("./music"):
#         os.mkdir("./music/")
#     try:
#         chrome_options = Options()
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument('--disable-gpu')
#         driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
#         wait = WebDriverWait(driver, 15)
#     except Exception as e:
#         print("请先安装最新版Chrome浏览器!", e)
#     while True:
#         try:
#             net_API.net_ease_cloud_api()
#         except:
#             print("请检查输入是否符合规范")
import numpy as np

# x=np.array([
#     [1,2],
#     [3,4],
#     [5,6],
#     [7,8],
#     [9,10]
# ])
# y=x[[0,1,2],[0,1,0]]
# print(y)
# u = np.array([6, 5, 9, 65, 5, 9, 5, 6, 8, 5, 9, 3, 9, 6, 0, 5])
# ui, indices = np.unique(u, return_inverse=True)
# print(indices)
# print(ui)
# print(np.argsort(ui))
from matplotlib import pyplot as plt

# x = np.arange(-50, 50)
# y = x ** 2
# plt.plot(x, y, linewidth=5)
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.title("Square平方")
# plt.xlabel("x", fontsize=14)
# plt.ylabel("y", fontsize=14)
# plt.show()
# x = np.arange(-1000010, 10000010)
# y = x ** 2
# plt.plot(x, y)
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.title("Square平方")
# plt.show()
# times = ['2012/04/01', '2090/06/31', '2013/05/02', '2011/02/07', '2014/02/21']
# sales = np.random.randint(500, 2000, size=len(times))
# expenses = np.random.randint(300, 1500, size=len(times))
# plt.xticks(range(1, len(times), 2), rotation=45)
# plt.plot(times, sales, label='Sales')
# plt.plot(times, expenses, label='Expenses')
# plt.legend()
# plt.show()
# print(np.random.normal(100, 20, 100) < 50)
# 导入工具包
# import requests
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
# import numpy as np
#
# # 请求头
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
# # =============================================================================
# # 爬取一页
# # =============================================================================
# # 爬取的网址
# url = 'https://movie.douban.com/subject/25845392/comments?start=20&limit=20&status=P&sort=new_score'
#
# # 获取信息
# html = requests.get(url, headers=headers)
# # 获取内容
# data = html.text
# soup = BeautifulSoup(data, 'html.parser')
#
# # 信息
# # 用户
# names = soup.select('#comments > div > div.comment > h3 > span.comment-info > a')
# # 评级
# pingjis = soup.select('#comments > div > div.comment > h3 > span.comment-info')
# # 日期
# riqis = soup.select('#comments > div > div.comment > h3 > span.comment-info > span.comment-time')
# # 内容
# neirongs = soup.select('#comments > div > div.comment > p > span')
#
# # 空list
# lis = []
# for name, pingji, riqi, neirong in zip(names, pingjis, riqis, neirongs):
#     pingji_re = pingji.find_all('span')
#     lis.append([name.get_text(),
#                 pingji_re[1]['class'],
#                 pingji_re[1]['title'],
#                 riqi.get_text().strip(),
#                 neirong.get_text()])
#
# result1 = pd.DataFrame(lis, columns=['用户', '评级', '等级', '日期', '内容'])
# # print(result1)
# # =============================================================================
# # 利用循环结构爬取多页
# # =============================================================================
#
# url = ['https://movie.douban.com/subject/25845392/comments?start={}&limit=20&status=P&sort=new_score'.format(i) for i in
#        range(0, 500, 20)]
#
# lis2 = []
#
# for urli in url:
#     # 获取信息
#     html = requests.get(urli, headers=headers)
#     # 获取内容
#     data = html.text
#     soup = BeautifulSoup(data, 'html.parser')
#     # 用户
#     names = soup.select('#comments > div > div.comment > h3 > span.comment-info > a')
#     # 评级
#     pingjis = soup.select('#comments > div > div.comment > h3 > span.comment-info')
#     # 日期
#     riqis = soup.select('#comments > div > div.comment > h3 > span.comment-info > span.comment-time')
#     # 内容
#     neirongs = soup.select('#comments > div > div.comment > p > span')
#
#     for name, pingji, riqi, neirong in zip(names, pingjis, riqis, neirongs):
#         pingji_re = pingji.find_all('span')
#         lis2.append([name.get_text(),
#                      pingji_re[1]['class'],
#                      pingji_re[1]['title'],
#                      riqi.get_text().strip(),
#                      neirong.get_text()])
#     print('完成:', urli)
#     time.sleep(np.random.randint(5, 10))
#
# result2 = pd.DataFrame(lis2, columns=['用户', '评级', '等级', '日期', '内容'])
# # 写入excel
# frame = pd.DataFrame(result2)
# file = frame.to_csv('movie.csv')
# -*- coding: utf-8 -*-
# import pandas
# import jieba
# import re
#
# # loading data
# data = pandas.read_excel(
#     "C:\\Users\\Lenovo\\Documents\\comments.xlsx"
# )
#
# # 1.文本内容清洗，清楚特殊符号，用正则表达式
# pattern = r"[!\"#$%&'()*+,-./:;<=>?@[\\\]^_^{|}~—！，。？、￥…（）：【】《》‘’“”\s]+"
# re_obj = re.compile(pattern)
#
#
# def clear(text):
#     return re.sub(pattern, "", text)
#
#
# data['comment'] = data['comment'].apply(clear)
# print(data.head())
#
#
# def cut_word(text):  # 返回生成器
#     return jieba.cut(text)
#
#
# # 2.分词 用jieba来实现分词
# data['comment'] = data['comment'].apply(cut_word)
#
#
# # 3.停用词处理，这里我用的是中文停词用表（文末附）
#
#
# def get_stopword():  # 使用set
#     s = set()
#     with open('C:\\Users\\Lenovo\\Desktop\\cn_stopwords.txt', encoding='UTF-8') as f:
#         for line in f:
#             s.add(line.strip())
#     return s
#
#
# def remove_stopword(words):
#     return [word for word in words if word not in stopword]
#
#
# stopword = get_stopword()
# data['comment'] = data['comment'].apply(remove_stopword)
#
# # 4.词汇统计
# from itertools import chain
# from collections import Counter
#
# li_2d = data['comment'].tolist()
# # 将二维列表转换为一维
# li_1d = list(chain.from_iterable(li_2d))
# print(f'总词汇量：{len(li_1d)}')
# c = Counter(li_1d)
# print(f'不重复词汇量：{len(c)}')
# common = c.most_common(50)
# # print(common)
# import pandas as pd
# frame = pd.DataFrame(common)
# file = frame.to_csv('common11.csv')
# # 计算每个评论的用词数
# num = [len(li) for li in li_2d]
#
# import matplotlib.pyplot as plt
# # 绘制所有用户在评论时所用词汇书，绘制直方图
# # n, bins, patches = plt.hist(num, bins=20, alpha=0.5)
# # plt.yscale('log')
# # plt.show()
#
# # 生成词云图
# from wordcloud import WordCloud
# # 导入图像处理库
# import PIL.Image as image
# # 导入数据处理库
# import numpy as np
# import matplotlib.colors as colors  # 处理图片相关内容
# # 文末附颜色对照表
# colormaps = colors.ListedColormap(['#FF4500', '#FF7F50', '#FFD700'])
# # mask可以用PPT画自己想要的图形（我这里是用来“长津湖”的艺术字）
# mask1 = np.array(image.open('C:\\Users\\Lenovo\\Desktop\\aa.png'))
# wc = WordCloud(font_path="simsun.ttc", background_color="white",
#                mask=mask1, colormap=colormaps)
#
# img = wc.generate_from_frequencies(c)
# plt.figure(figsize=(15, 10))
# plt.imshow(img)
# plt.axis('off')
# plt.show()
# import ssl
# import string
# import urllib
# import urllib.request
# import urllib.parse
#
# from bs4 import BeautifulSoup
#
#
# def create_url(keyword: str, kind: str) -> str:
#     '''
#     Create url through keywords
#     Args:
#         keyword: the keyword you want to search
#         kind: a string indicating the kind of search result
#             type: 读书; num: 1001
#             type: 电影; num: 1002
#             type: 音乐; num: 1003
#     Returns: url
#     '''
#     num = ''
#     if kind == '读书':
#         num = 1001
#     elif kind == '电影':
#         num = 1002
#     elif kind == '音乐':
#         num = 1003
#     url = 'https://www.douban.com/search?cat=' + \
#         str(num) + '&q=' + keyword
#     return url
#
#
# def get_html(url: str) -> str:
#     '''send a request'''
#
#     headers = {
#         # 'Cookie': 你的cookie,
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
#         'Connection': 'keep-alive'
#     }
#     ssl._create_default_https_context = ssl._create_unverified_context
#
#     s = urllib.parse.quote(url, safe=string.printable)  # safe表示可以忽略的部分
#     req = urllib.request.Request(url=s, headers=headers)
#     req = urllib.request.urlopen(req)
#     content = req.read().decode('utf-8')
#     return content
#
#
# def get_content(keyword: str, kind: str) -> str:
#     '''
#     Create url through keywords
#     Args:
#         keyword: the keyword you want to search
#         kind: a string indicating the kind of search result
#             type: 读书; num: 1001
#             type: 电影; num: 1002
#             type: 音乐; num: 1003
#     Returns: url
#     '''
#     url = create_url(keyword=keyword, kind=kind)
#     html = get_html(url)
#     # print(html)
#     soup_content = BeautifulSoup(html, 'html.parser')
#     contents = soup_content.find_all('h3', limit=1)
#     result = str(contents[0])
#     return result
#
#
# def find_sid(raw_str: str) -> str:
#     '''
#     find sid in raw_str
#     Args:
#         raw_str: a html info string contains sid
#     Returns:
#         sid
#     '''
#     assert type(raw_str) == str, \
#         '''the type of raw_str must be str'''
#     start_index = raw_str.find('sid:')
#     sid = raw_str[start_index + 5: start_index + 13]
#     sid.strip(',')
#     return sid
#
#
# if __name__ == "__main__":
#     raw_str = get_content('看见', '读书')
#     print(find_sid(raw_str))
# import urllib.request
#
# import urllib.parse
#
# from bs4 import BeautifulSoup
#
# import time
#
# import jieba
#
# import wordcloud
#
# import crawler_tools
#
# def creat_url(num):
#
#     urls = []
#
#     for page in range(1, 20):
#
#         url = 'https://book.douban.com/subject/' + str(num)+'/comments/hot?p='+str(page)+''
#
#         urls.append(url)
#
#     print(urls)
#
#     return urls
#
# def get_html(urls):
#
#     headers = {
#
#         # 'Cookie': 你的cookie,
#
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
#
#         'Connection': 'keep-alive'
#
#     }
#
#     for url in urls:
#
#         print('正在爬取：'+url)
#
#         req = urllib.request.Request(url=url, headers=headers)
#
#         req = urllib.request.urlopen(req)
#
#         content = req.read().decode('utf-8')
#
#         time.sleep(10)
#
#     return content
#
# def get_comment(num):
#
#     a = creat_url(num)
#
#     html = get_html(a)
#
#     soupComment = BeautifulSoup(html, 'html.parser')
#
#     comments = soupComment.findAll('span', 'short')
#
#     onePageComments = []
#
#     for comment in comments:
#
#         # print(comment.getText()+'\n')
#
#         onePageComments.append(comment.getText()+'\n')
#
#     print(onePageComments)
#
#     f = open('数据.txt', 'a', encoding='utf-8')
#
#     for sentence in onePageComments:
#
#         f.write(sentence)
#
#     f.close()
#
# raw_str = crawler_tools.get_content('看见', '读书')
#
# sid = crawler_tools.find_sid(raw_str)
#
# print('sid:'+sid)
#
# get_comment(sid)
# -*- coding: utf-8 -*-
# @Author  : LuoXian
# @Date    : 2020/2/11 22:07
# Software : PyCharm
# version： Python 3.8
# @File    : demo.py
# import requests
# from bs4 import BeautifulSoup
# from wordcloud import WordCloud
# import jieba
# import matplotlib.pyplot as plt
# import time
#
# # 设置请求头，包含 User-Agent 和 Cookie
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
#     'Cookie': 'bid=random.sample(string.ascii_letters + string.digits, 11)'  # 请替换为你的实际 Cookie
# }
#
# # 获取指定页面的 HTML 内容
# def get_page_html(url):
#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#         return response.text
#     except requests.RequestException as e:
#         print(f"请求失败: {e}")
#         return None
#
# # 从 HTML 中解析评论内容
# def parse_comments(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     comment_items = soup.find_all('div', class_='comment-item')
#     comments = [item.find('span', class_='short').get_text(strip=True) for item in comment_items]
#     return comments
#
# # 爬取指定页数的评论
# def fetch_comments(book_id, pages=20, sort='score'):
#     all_comments = []
#     for page in range(pages):
#         start = page * 20
#         url = f"https://book.douban.com/subject/{book_id}/comments/?start={start}&limit=20&status=P&sort={sort}"
#         html = get_page_html(url)
#         if html:
#             comments = parse_comments(html)
#             all_comments.extend(comments)
#             print(f"已获取第 {page + 1} 页的评论，共 {len(comments)} 条。")
#         time.sleep(2)  # 避免请求过于频繁
#     return all_comments
#
# # 生成词云图
# def generate_wordcloud(text, output_image):
#     wordlist = jieba.lcut(text)
#     words = ' '.join(wordlist)
#     wordcloud = WordCloud(
#         font_path='msyh.ttc',  # 请确保字体文件存在，适用于显示中文
#         background_color='white',
#         width=800,
#         height=600,
#         max_words=200,
#         max_font_size=100
#     ).generate(words)
#     wordcloud.to_file(output_image)
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis('off')
#     plt.show()
#
# # 主函数
# def main():
#     book_id = '2567698'  # 《三体》的豆瓣图书ID
#     comments = fetch_comments(book_id, pages=20, sort='score')
#     if comments:
#         all_text = ' '.join(comments)
#         generate_wordcloud(all_text, '三体_词云.png')
#         print("词云图已生成并保存为 '三体_词云.png'。")
#     else:
#         print("未能获取到任何评论。")
#
# if __name__ == '__main__':
#     main()
# import os
# import re
# import time
# import requests as req
# import bs4
# from wordcloud import WordCloud
# from jieba import lcut
# from matplotlib.pyplot import imread
# from skimage import img_as_ubyte  # 用于处理图片为无符号整型
#
# # 加载中国地图作为词云背景
# mask = imread('img.png')
# mask = img_as_ubyte(mask)  # 将图片像素值转为无符号整型
#
# # 设置 HTTP Headers 模拟用户请求
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64)'
#                   'AppleWebKit/537.36(KHTML,like Gecko)'
#                   'Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.115'
# }
#
# # 豆瓣评论爬取与评分汇总
# page_nums = ['0', '20', '40']
# for page in page_nums:
#     url1 = 'https://book.douban.com/subject/1449351/comments/?start='
#     url2 = '&limit=20&status=P&sort=score'
#     url = url1 + page + url2
#
#     try:
#         # 请求评论页面
#         response = req.get(url, headers=headers)
#         response.raise_for_status()  # 如果状态码不是200，抛出异常
#         print(f"请求成功: {url}")
#         soup = bs4.BeautifulSoup(response.text, 'html.parser')
#
#         # 提取评论内容
#         comments = soup.find_all('span', 'short')
#         comment_list = [comment.text + '\n' for comment in comments]
#         with open('comment1.txt', 'a', encoding='utf-8') as f:
#             f.writelines(comment_list)
#
#         # 提取评分
#         star_pattern = re.compile('<span class="user-stars allstar(.*?) rating"')
#         star_list = star_pattern.findall(response.text)
#         total_score = sum(int(star) for star in star_list)
#         print(f"第 {int(page)//20 + 1} 页评分总和: {total_score}")
#
#         # 下载图片
#         img_dir = 'pictures'
#         os.makedirs(img_dir, exist_ok=True)
#         for idx, img in enumerate(soup.find_all('img')):
#             img_url = img.get('src')
#             try:
#                 img_response = req.get(img_url, timeout=10)
#                 img_response.raise_for_status()
#                 with open(f"{img_dir}/{int(page) + idx}.jpg", 'wb') as img_file:
#                     img_file.write(img_response.content)
#             except req.exceptions.RequestException as e:
#                 print(f"图片下载失败: {e}")
#         time.sleep(3)  # 控制请求频率
#
#     except req.exceptions.RequestException as e:
#         print(f"请求失败: {e}")
#
# # 生成词云
# with open('comment1.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
#
# word_list = lcut(text)
# word_cloud_text = ' '.join(word_list)
#
# wordcloud = WordCloud(
#     font_path='msyh.ttc',
#     mask=mask,
#     width=1000,
#     height=700,
#     background_color='white'
# ).generate(word_cloud_text)
#
# wordcloud.to_file('luxun_comment1_wordcloud.png')
# print("词云图生成完成！")
# a=input()
# cnt=0
# for i in range(len(a)):
#     j=i+1
#     while j<(len(a)):
#         cnt+=int((not bool(int(a[i]+a[j])%2)))
#         j+=1
# print(cnt)
# import pandas as pd
# # drinks=pd.read_csv('drinks.csv')
# # print(drinks.groupby('continent').wine_servings.count())
# # print(drinks.groupby('country').wine_servings.describe())
# # # print(drinks["continent", "beer_servings"].value_counts())
# # print(drinks.groupby('continent').spirit_servings.agg("mean"))
# s=pd.Series([1,2,3,4,5,6,7,8,9,10,'C',np.nan,'Python\t','    Java   '])
# print(s.str.len())
# print(s.str.strip())
# print(s)
# from flask import Flask, render_template, request, redirect, url_for
# app=Flask(__name__)
# @app.route('/')
# def index():
#     return "flask"
# if __name__ == '__main__':
#     app.run(debug=True)
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 设置NumPy打印选项以提高可读性
# np.set_printoptions(precision=3, edgeitems=5000, suppress=True)
#
# # 生成随机数据：100个点，每个点有2个坐标
# data = 2 * np.random.randn(100, 2) - 1
# print("生成的数据:\n", data)
#
# # 分离x和y坐标
# x, y = data[:, 0], data[:, 1]
#
# # 计算每个点到原点的距离的平方
# squared_distances = x**2 + y**2
#
# # 创建单位圆内和小圆内的掩码
# within_unit_circle = squared_distances < 1
# within_hole = squared_distances < 0.25  # 当前未使用
#
# print("在单位圆内的点的掩码:\n", within_unit_circle)
#
# # 生成均匀分布的随机数
# uniform_random = np.random.rand(10000)
# # 注意：打印大数组会导致输出混乱，建议只打印部分或摘要
# print("均匀随机数的前10个元素:\n", uniform_random[:10])
#
# # 创建子图：1行2列
# fig, axs = plt.subplots(1, 2, figsize=(12, 5))
#
# # 绘制单位圆内的散点图
# axs[0].scatter(
#     x[within_unit_circle],
#     y[within_unit_circle],
#     color='red',
#     alpha=0.6,
#     edgecolors='w'
# )
# axs[0].set_title('单位圆内的点')
# axs[0].set_xlabel('X轴')
# axs[0].set_ylabel('Y轴')
# axs[0].set_aspect('equal', 'box')
# axs[0].grid(True)
#
# # 绘制均匀随机数的直方图
# axs[1].hist(
#     uniform_random,
#     bins=20,
#     color='blue',
#     edgecolor='black',
#     alpha=0.7
# )
# axs[1].set_title('均匀随机数的直方图')
# axs[1].set_xlabel('值')
# axs[1].set_ylabel('频率')
# axs[1].grid(True)
#
# # 调整布局以优化间距
# plt.tight_layout()
#
# # 显示图形
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# d=np.random.rand(10)
# print(d)
# print(d<0.5)
# def can_find_odd_sum_triplet(n, arr):
#     odd_count = 0
#     even_count = 0
#
#     for num in arr:
#         if num % 2 == 1:
#             odd_count += 1
#         else:
#             even_count += 1
#
#     # 条件1: 至少有3个奇数
#     if odd_count >= 3:
#         return "YES"
#
#     # 条件2: 至少有1个奇数和2个偶数
#     if odd_count >= 1 and even_count >= 2:
#         return "YES"
#
#     return "NO"
#
#
# n = int(input())
# arr = []
# for i in range(n):
#     c = int(input())
#     arr[i] = c
# import re
# s='hello pyton'
# pattern='hello'
# v=re.match(pattern,s)
# print(v)
# print(v.group())
# print(v.span())
# import re
# pattern = '.'#匹配任意一个字符（除了\n）
# s='a'
# print('匹配字符a:',re.match(pattern,s))
# print(re.match(pattern,'\\n').group())
# import re
# print('------*匹配零次或多次--------')
# pattern='\d*' #0 次或多次
# s='123abc123'
# print('匹配 123abc：',re.match(pattern,s))
# Simplified visualization to ensure clear and proper representation
# import matplotlib.pyplot as plt
#
# # Data for users and works
# original_users = ["12345", "67890", "11111", "54321"]
# mapped_users = ["0", "1", "2", "3"]
# original_works = ["987", "654", "321", "100"]
# mapped_works = ["0", "1", "2", "3"]
#
# # Initialize figure and axes
# fig, ax = plt.subplots(figsize=(10, 6))
#
# # Plot user mappings
# for i, (orig, mapped) in enumerate(zip(original_users, mapped_users)):
#     ax.arrow(0.2, len(original_users) - i, 1, 0, head_width=0.1, head_length=0.1, fc='blue', ec='blue')
#     ax.text(0, len(original_users) - i, orig, va='center', ha='right', fontsize=10, color='blue')
#     ax.text(1.5, len(original_users) - i, mapped, va='center', ha='left', fontsize=10, color='blue')
#
# # Plot work mappings
# for i, (orig, mapped) in enumerate(zip(original_works, mapped_works)):
#     ax.arrow(3, len(original_works) - i, 1, 0, head_width=0.1, head_length=0.1, fc='green', ec='green')
#     ax.text(2.8, len(original_works) - i, orig, va='center', ha='right', fontsize=10, color='green')
#     ax.text(4.5, len(original_works) - i, mapped, va='center', ha='left', fontsize=10, color='green')
#
# # Add labels for sections
# ax.text(0.6, len(original_users) + 0.5, "User ID Mapping", fontsize=12, fontweight='bold', color='blue')
# ax.text(3.6, len(original_works) + 0.5, "Work ID Mapping", fontsize=12, fontweight='bold', color='green')
#
# # Adjust plot
# ax.set_xlim(-0.5, 5)
# ax.set_ylim(-0.5, max(len(original_users), len(original_works)) + 1)
# ax.axis("off")
#
# # Display plot
# plt.title("User and Work ID Mapping Visualization", fontsize=14, fontweight='bold', pad=20)
# plt.tight_layout()
# plt.show()
# Re-attempt to save the workflow diagram to a file
# Reattempt to draw the workflow diagram with more spacing adjustments
# import matplotlib.pyplot as plt
# import networkx as nx
#
# # Create a directed graph
# G = nx.DiGraph()
#
# # Add nodes and edges for each module
# G.add_edges_from([
#     # Module 1: Data Collection and Preprocessing
#     ("Input Data", "Data Cleaning & Processing"),
#     ("Data Cleaning & Processing", "Index Mapping"),
#     # Module 2: Model Training
#     ("Index Mapping", "Feature Extraction"),
#     ("Feature Extraction", "Model Selection"),
#     ("Model Selection", "Model Training"),
#     # Module 3: Recommendation Generation
#     ("Model Training", "Recall Stage"),
#     ("Recall Stage", "Ranking Stage"),
#     ("Ranking Stage", "Recommendation Results"),
#     # Module 4: User Interaction and Dynamic Update
#     ("Recommendation Results", "User Feedback"),
#     ("User Feedback", "Model Training"),
#     # Module 5: Model Update and Maintenance
#     ("Model Training", "Periodic Updates"),
#     ("User Feedback", "Cold Start Handling"),
# ])
#
# # Define layout
# pos = nx.spring_layout(G, seed=42)  # Fixed layout for consistency
#
# # Draw the graph
# plt.figure(figsize=(12, 8))
# nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=15)
# plt.title("Recommendation System Workflow", fontsize=16, fontweight='bold')
# plt.show()
# import matplotlib.pyplot as plt
# from matplotlib.patches import FancyArrowPatch
#
# # Create figure and axis
# fig, ax = plt.subplots(figsize=(12, 8))
# ax.axis('off')
#
# # Box helper function
# def add_box(x, y, width, height, text, fontsize=10, color="lightblue"):
#     rect = plt.Rectangle((x, y), width, height, color=color, ec="black", lw=1.5)
#     ax.add_patch(rect)
#     ax.text(x + width / 2, y + height / 2, text, ha='center', va='center', fontsize=fontsize, wrap=True)
#
# # Arrow helper function
# def add_arrow(start, end):
#     arrow = FancyArrowPatch(start, end, mutation_scale=20, color="black", linewidth=1.5)
#     ax.add_patch(arrow)
#
# # Add elements
# add_box(0.5, 6.5, 3, 1, "User Actions\n(Click/View/Rate)", fontsize=9)
# add_box(5, 6.5, 3, 1, "Data Collection\n(User Logs)", fontsize=9)
# add_box(9.5, 6.5, 3, 1, "Feature Engineering\n(Embedding/Index)", fontsize=9)
# add_box(9.5, 4, 3, 1, "Model Training\n(FM/Deep FM/LFM)", fontsize=9)
# add_box(9.5, 1.5, 3, 1, "Recommendation\nGeneration", fontsize=9)
# add_box(0.5, 1.5, 3, 1, "Feedback Loop\n(Model Evaluation)", fontsize=9)
#
# # Add arrows
# add_arrow((3.5, 7), (5, 7))
# add_arrow((8, 7), (9.5, 7))
# add_arrow((10.5, 6.5), (10.5, 5))
# add_arrow((10.5, 4), (10.5, 2.5))
# add_arrow((8.5, 2), (3.5, 2))
# add_arrow((3.5, 2.5), (3.5, 6.5))
#
# # Add titles and finalize
# plt.title("Recommendation System Workflow", fontsize=14)
# plt.show()
# f = open('test.txt', 'wb')
# while True:
#     buf = f.readline()
#     if not buf:
#         # 文件读完了
#         break
#     print(buf)
# f.write('你好'.encode())
# f.close()
# f = open('test.txt', 'rb')
# print(f.read().decode())
# f.close()
# file_name = input("Enter file name: ")
# f = open(file_name, 'rb')
# buffer = f.read()
# f.close()
# index = file_name.rfind('.')
# print(index)
# import multiprocessing
#
# def worker(shared_value, lock):
#     for _ in range(10):
#         with lock:
#             shared_value.value += 1
#             time.sleep(random.uniform(0, 2))
#         print(f"Worker: 进程id{multiprocessing.current_process().pid} + 父进程id{os.getppid()} + {shared_value.value}")
#         time.sleep(random.uniform(0, 2))
#     time.sleep(random.uniform(0, 2))
#
# if __name__ == "__main__":
#     # 创建一个共享的整数变量
#     shared_value = multiprocessing.Value('i', 0)
#     # 创建一个锁对象
#     lock = multiprocessing.Lock()
#
#     # 创建多个进程
#     processes = [multiprocessing.Process(target=worker, args=(shared_value, lock)) for _ in range(5)]
#
#     # 启动所有进程
#     for p in processes:
#         p.start()
#
#     # 等待所有进程完成
#     for p in processes:
#         p.join()
#
#     print(f"Final value: {shared_value.value}")
# 读取数据字段字符串并处理成列表
# data_str = """
# fnd17_oxlcxspebq, fnd17_shsoutbs,fnd17_oxlcxspebq, fnd28_value_05191q,
# fnd17_oxlcxspebq, fnd28_value_05192q,fnd17_oxlcxspebq,
# fnd28_value_05301q,fnd17_oxlcxspebq, fnd28_value_05302,fnd17_pehigh,
# fnd17_pelow,fnd17_priceavg150day, fnd17_priceavg200day,fnd17_priceavg150day,
# fnd17_priceavg50day,fnd17_priceavg200day, fnd17_priceavg50day,fnd17_pxedra,
# fnd17_tbea,fnd17_pxedra, fnd28_newa3_value_18191a,fnd17_pxedra,
# fnd28_newa3_value_18198a,fnd17_pxedra, fnd28_value_02300a,fnd17_pxedra,
# fnd28_value_05302,fnd17_pxedra, mdl175_ebitda,fnd17_pxedra, mdl175_pain
# """
#
# # 处理数据字符串，分割并去除首尾空白
# data_fields = [field.strip() for field in data_str.strip().replace('\n', '').split(',')]
#
# # 去重并保留原始顺序，同时过滤空字符串
# unique_fields = []
# seen = set()
# for field in data_fields:
#     if field and field not in seen:  # 确保非空且未重复
#         seen.add(field)
#         unique_fields.append(field)
#
# # 生成所有A和B的无序组合（A ≠ B）
# from itertools import combinations
#
# combinations_list = list(combinations(unique_fields, 2))
#
# # 统计总组合数
# count = len(combinations_list)
#
# # 生成所有Alpha表达式
# alpha_expressions = [
#     f"ts_regression(ts_zscore({a}, 500), ts_zscore({b}, 500), 500)"
#     for a, b in combinations_list
# ]
#
# # 输出结果
# print(f"总组合个数: {count}")
# for expr in alpha_expressions:
#     print(expr)
# import warnings
#
# warnings.filterwarnings("ignore")
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# plt.style.use('seaborn-v0_8')
# # 读取数据
# data = pd.read_csv('data.csv', index_col=0, parse_dates=True)
# # data.plot(figsize=(10, 12), subplots=True)
# #
# ret = np.log(data / data.shift(1)).dropna(inplace=True)
#
# # pd.plotting.scatter_matrix(ret, alpha=0.3, figsize=(10, 10), diagonal='kde')
# np.polyfit(ret['.SPX'], ret['.VIX'], 'o', deg=1)
# plt.show()
# from pylab import mpl
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# mpl.rcParams['axes.unicode_minus'] = False
# data=pd.read_csv('test.csv',index_col=0)
# data.head()
import requests
from requests.auth import HTTPBasicAuth
import time
import logging
import itertools
from typing import Generator, Dict, Optional

# 日志配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('alpha_generator.log'),
        logging.StreamHandler()
    ]
)


class SmartAlphaGenerator:
    def __init__(self, username: str, password: str):
        # API端点配置
        self.endpoints = {
            'auth': 'https://api.worldquantbrain.com/authentication',
            'data_fields': 'https://api.worldquantbrain.com/data-fields',
            'simulations': 'https://api.worldquantbrain.com/simulations'
        }

        # 高级参数配置
        self.generation_params = {
            'max_depth': 3,  # 表达式嵌套深度
            'status_timeout': 300,  # 状态检查超时（秒）
            'retry_delay': 60,  # 重试等待时间
            'rate_limit_buffer': 5  # 速率限制缓冲
        }

        # 增强的智能模板库（已修复括号和单位问题）
        self.template_library = [
            # 1. 修正后的多层级嵌套表达式
            "group_rank(ts_zscore(ts_mean({field}, {d}) * signed_power(ts_zscore(ts_delta(volume, {d}), 20), 0.5), 20), subindustry)",

            # 2. 添加时间窗口参数
            "quantile(ts_corr({field}, returns, {d}), 'gaussian') - zscore(market_cap)",

            # 3. 完整参数声明
            "group_neutralize(ts_regression({field}, ts_zscore(volume, {d}), {d}, rettype=6), sector)",

            # 4. 补全括号
            "winsorize(ts_rank({field}, {d}) * rank(-volume/adv20))",

            # 5. 标准化复合表达式
            "scale(ts_zscore({field}, {d}) + scale(ts_zscore(volume, {d})))",

            # 6. 完整协方差计算
            "ts_covariance({field}, returns, {d}) / ts_std_dev(volume, {d})"
        ]

        # 智能参数空间
        self.param_space = {
            'time_windows': [5, 10, 20, 30, 60, 90],
            'neutralization': ["SUBINDUSTRY", "INDUSTRY", "SECTOR", "MARKET"],
            'truncation_levels': [0.01, 0.02, 0.03, 0.05],
            'decay_factors': [0, 1, 3, 5]
        }

        # 初始化会话
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(username, password)
        self._verify_connection()

    def _verify_connection(self):
        """增强的认证验证"""
        try:
            resp = self.session.post(self.endpoints['auth'], timeout=15)
            resp.raise_for_status()
            rate_limit = resp.headers.get('X-RateLimit-Limit', 100)
            self.generation_params['rate_limit_buffer'] = max(5, int(rate_limit) * 0.1)
            logging.info("连接成功 | 速率限制: %s/小时", rate_limit)
        except Exception as e:
            logging.error("连接失败: %s", str(e))
            raise

    def _get_high_quality_fields(self) -> Generator[str, None, None]:
        """智能获取高质量数据字段"""
        params = {
            'region': 'USA',
            'delay': 1,
            'universe': 'TOP3000',
            'instrumentType': 'EQUITY',
            'dataset.id': 'analyst4',
            'type': 'MATRIX',
            'limit': 50,
            'sort': '-coverage,-userCount'  # 按覆盖率和使用频率排序
        }

        offset = 0
        while True:
            try:
                params['offset'] = offset
                resp = self.session.get(self.endpoints['data_fields'], params=params)
                data = resp.json()

                for field in data['results']:
                    # 智能过滤条件
                    if field['coverage'] >= 0.8 and field['userCount'] > 1000:
                        yield field['id']

                if len(data['results']) < 50:
                    break
                offset += 50
                time.sleep(1)  # 遵守API速率限制

            except Exception as e:
                logging.error("字段获取异常: %s", str(e))
                break

    def _generate_smart_configs(self) -> Generator[Dict, None, None]:
        """生成智能配置"""
        for field in self._get_high_quality_fields():
            for template in self._select_template(field):
                for params in self._param_combinations():
                    try:
                        print(self._render_template(template, params))
                        config = {
                            "type": "REGULAR",
                            "settings": {
                                "instrumentType": "EQUITY",
                                "region": "USA",
                                "universe": "TOP3000",
                                "delay": 1,
                                "decay": params['decay'],
                                "neutralization": params['neutralization'],
                                "truncation": params['truncation'],
                                "pasteurization": "ON",
                                "language": "FASTEXPR",
                                # 新增三个必填字段
                                "unitHandling": "VERIFY",
                                "nanHandling": "ON",
                                "visualization": False
                            },
                            "regular": self._render_template(template, params)
                        }
                        yield config
                    except KeyError as e:
                        logging.warning("模板渲染错误: %s", str(e))

    def _select_template(self, field: str) -> Generator[str, None, None]:
        """动态选择适合字段的模板"""
        # 根据字段特征选择模板（示例逻辑）
        if 'volume' in field:
            yield from [
                "ts_delta({field}, {d}) / ts_mean(volume, {d})",
                "ts_corr({field}, volume, {d})"
            ]
        elif 'price' in field:
            yield from [
                "group_rank(ts_mean({field},{d}))",
                "ts_zscore({field}, {d}) * market_cap"
            ]
        else:
            yield from self.template_library

    def _param_combinations(self) -> Generator[Dict, None, None]:
        """生成智能参数组合"""
        for combo in itertools.product(
                self.param_space['time_windows'],
                self.param_space['neutralization'],
                self.param_space['truncation_levels'],
                self.param_space['decay_factors'],
                self._get_high_quality_fields()  # 直接集成字段
        ):
            yield {
                'd': combo[0],
                'neutralization': combo[1],
                'truncation': combo[2],
                'decay': combo[3],
                'field': combo[4]  # 添加字段参数
            }

    def _render_template(self, template: str, params: Dict) -> str:
        """安全渲染模板（修复字段替换）"""
        try:
            return template.format(
                field=params['field'],  # 确保字段参数存在
                d=params['d'],
                decay=params.get('decay', 0)  # 可选参数提供默认值
            )
        except KeyError as e:
            logging.error("缺失关键参数: %s | 当前参数: %s", str(e), params)
            return ""

    def _submit_simulation(self, config: Dict) -> Optional[str]:
        """增强稳健性的任务提交"""
        for attempt in range(3):
            try:
                resp = self.session.post(
                    self.endpoints['simulations'],
                    json=config,
                    timeout=30
                )
                print(resp)
                # 添加响应内容检查
                if not resp.content:
                    logging.warning("空响应内容")
                    continue

                # 记录原始响应信息
                logging.debug(f"响应状态码: {resp.status_code}")
                logging.debug(f"响应头: {resp.headers}")
                logging.debug(f"响应体: {resp.text[:200]}")  # 记录前200字符

                # 处理429速率限制
                if resp.status_code == 429:
                    retry_after = int(resp.headers.get('Retry-After', self.generation_params['retry_delay']))
                    logging.info("速率限制 | 等待 %ds", retry_after)
                    time.sleep(retry_after)
                    continue

                # 处理认证失效
                if resp.status_code == 401:
                    logging.warning("认证失效，尝试重新认证")
                    self._verify_connection()
                    continue

                # 处理服务器错误
                if resp.status_code >= 500:
                    logging.warning("服务器错误 (HTTP %d)", resp.status_code)
                    time.sleep(5)
                    continue

                resp.raise_for_status()

                # 安全解析JSON
                try:
                    result = resp.json()
                    logging.debug("完整响应JSON: %s", result)
                except ValueError as e:
                    logging.error("JSON解析失败: %s | 原始内容: %s", str(e), resp.text[:200])
                    return None

                return resp.headers.get('Location')

            except requests.exceptions.RequestException as e:
                logging.warning("请求异常 (尝试 %d/3): %s", attempt + 1, str(e))
                time.sleep(2 ** attempt)

            except Exception as e:
                logging.error("未处理异常: %s", str(e))
                break

        return None

    def _monitor_simulation(self, location: str) -> bool:
        """增强的状态监控"""
        start_time = time.time()
        while time.time() - start_time < self.generation_params['status_timeout']:
            try:
                resp = self.session.get(location)
                data = resp.json()

                if data['status'] == 'COMPLETED':
                    logging.info("模型生成成功: %s", data.get('alpha'))
                    return True

                time.sleep(self.generation_params['rate_limit_buffer'])
            except Exception as e:
                logging.error("状态检查错误: %s", str(e))
                time.sleep(10)
        return False

    def generate(self):
        """主生成流程"""
        success_count = 0
        total_count = 0

        try:
            for config in self._generate_smart_configs():
                total_count += 1

                # 提交任务
                location = self._submit_simulation(config)
                if not location:
                    continue

                # 监控任务
                if self._monitor_simulation(location):
                    success_count += 1

                # 动态速率控制
                if total_count % 10 == 0:
                    time.sleep(self.generation_params['rate_limit_buffer'])

                # 进度报告
                if total_count % 50 == 0:
                    logging.info("进度报告 | 已提交: %d | 成功: %d (%.1f%%)",
                                 total_count, success_count,
                                 success_count / total_count * 100 if total_count else 0)

        except KeyboardInterrupt:
            logging.info("用户中断 | 最终报告: 成功 %d/%d", success_count, total_count)
        except Exception as e:
            logging.error("生成异常: %s", str(e))
        finally:
            logging.info("生成完成 | 成功率: %.1f%%",
                         success_count / total_count * 100 if total_count else 0)


if __name__ == "__main__":
    try:
        generator = SmartAlphaGenerator(
            username="513923907@qq.com",
            password="888888qq"
        )
        generator.generate()


    except Exception as e:
        logging.error("系统初始化失败: %s", str(e))

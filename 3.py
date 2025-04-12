import numpy as np
from matplotlib import pyplot as plt
import json
import pycharts
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts
from pyspark import SparkContext, SparkConf

# p = np.random.rand(10000)
# np.set_printoptions(precision=3, edgeitems=5000, suppress=True)
# plt.hist(p, bins=20, color='g', alpha=0.5,edgecolor='black')
# plt.show()
# N=10000
# times=100
# z=np.zeros(N)
# for i in range(times):
#     z+=np.random.rand(N)
# z/=times
# plt.hist(z, bins=20, color='m', alpha=0.5,edgecolor='k')
# plt.show()
# p=np.random.rand(3,4)
# print(p)
# print(np.sqrt(6*np.sum(1/np.arange(1,10000)**2)))
# def bagging(n,p):
#     s=0
#     for i in range(n//2+1,n+1):
#
#
# n=100
# x=np.arange(1,n,2)
# y=np.empty_like(x,dtype=float)
#
#
#
#
# for i,t in enumerate(x):
#     y[i]=bagging(t)

# data = [{'a': 'A', 'b': (2, 4), 'c': 3.0},{'a': '王大锤', 'b': (16, 13), 'c': 9.0},{'a': '赵啸虎', 'b': (89, 64), 'c': 3.0}]
# json_str = json.dumps(data,ensure_ascii=False)  # ensure_ascii=False 保证中文不乱码
# print(json_str) #列表转字典
# print(json.loads(json_str))
# print(json.dumps(data,indent=4,ensure_ascii=False))
# print(json.loads(json.dumps(data,ensure_ascii=False)))
# print(type(json_str))
# #字典转列表
# s='[{"a": "A", "b": [2, 4], "c": 3.0}, {"a": "王大锤", "b": [16, 13], "c": 9.0}, {"a": "赵啸虎", "b": [89, 64], "c": 3.0}]'
# print(json.loads(s))
# print(type(json.loads(s)))
# #json转{k-v}
# s='{"a": "A", "b": [2, 4], "c": 3.0}'
# print(json.loads(s))
# print(type(json.loads(s)))
# #  结论：json可以在不同的语言之间无缝转换
# line = Line()
# line.add_xaxis(['中国', '美国', '英国'])
# line.add_yaxis('GDP', [14, 13, 15])
# #设置全局配置
# line.set_global_opts(
#     title_opts=TitleOpts(title='世界各国GDP', subtitle='单位：万亿美元', pos_left='center', pos_bottom='1%'),
#     legend_opts=LegendOpts(),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True)
# )
#render方法将代码生成图像
# line.render()

# f_us = open("资料/可视化案例数据/折线图数据/美国.txt", 'r', encoding='utf-8')
# us_dat = f_us.read().replace("jsonp_1629344292311_69436(", "")
# us_dat = us_dat[:-2]
# us_dict = json.loads(us_dat)
# us_trend_data = us_dict['data'][0]['trend']
# f_jp = open("资料/可视化案例数据/折线图数据/日本.txt", 'r', encoding='utf-8')
# jp_dat = f_jp.read().replace("jsonp_1629350871167_29498(", "")
# jp_dat = jp_dat[:-2]
# jp_dict = json.loads(jp_dat)
# jp_trend_data = jp_dict['data'][0]['trend']
# f_in = open("资料/可视化案例数据/折线图数据/印度.txt", 'r', encoding='utf-8')
# in_dat = f_in.read().replace("jsonp_1629350745930_63180(", "")
# in_dat = in_dat[:-2]
# in_dict = json.loads(in_dat)
# in_trend_data = in_dict['data'][0]['trend']
# us_x_data = us_trend_data['updateDate'][:314]
# us_y_data = us_trend_data['list'][0]['data'][:314]
# jp_x_data = jp_trend_data['updateDate'][:314]
# jp_y_data = jp_trend_data['list'][0]['data'][:314]
# in_x_data = in_trend_data['updateDate'][:314]
# in_y_data = in_trend_data['list'][0]['data'][:314]
# line = Line()
# line.add_xaxis(us_x_data)
# line.add_yaxis('日本', jp_y_data)
# line.add_yaxis('印度', in_y_data)
# line.set_global_opts(
#     title_opts=TitleOpts(title='2020年美日印确诊人数对比折线图', subtitle='单位：人数', pos_left='center',
#                          pos_bottom='1%'),
#     legend_opts=LegendOpts(),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True)
# )
# line.render()
# conf = SparkConf().setAppName('test').setMaster('local[*]')
# sc = SparkContext(conf=conf)
# rdd = sc.parallelize([1, 2, 3, 4, 5])
# print(rdd.collect())
# sc.stop()
# conf = SparkConf().setAppName('test').setMaster('local[*]')
# sc = SparkContext(conf=conf)
# file_rdd=sc.textFile('orders.txt')
# json_str_rdd=file_rdd.flatMap(lambda x:x.split('|'))
# dict_rdd=json_str_rdd.map(lambda x:json.loads(x))
# city_with_money_rdd=dict_rdd.map(lambda x:(x['areaName'],int(x['money'])))
# city_result_rdd=city_with_money_rdd.reduceByKey(lambda x,y:x+y)


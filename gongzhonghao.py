#!/usr/bin/env python
# -*- coding:utf-8 -*-


import random
import time
import requests
import werobot
from werobot.replies import ArticlesReply, Article, ImageReply, TextReply, MusicReply

robot=werobot.WeRoBot(token='liuang123456')


# 订阅后的回复
@robot.subscribe
def subscribe():
    return "***欢迎关注公众号[愉快][愉快][愉快]***\n" \
           "***输入任意内容开始与我聊天！\n" \
           "***输入'博客'关注我的博客!\n" \
           "***输入'音乐'为小主送上舒缓的歌曲!\n"


# 关键字 博客 回复
@robot.filter('博客')
def blog(message):
    reply = ArticlesReply(message=message)
    article = Article(
        title="忧郁的炸酱面",
        description="我的个人博客",
        img="https://werobot.readthedocs.io/zh_CN/latest/_static/qq.png",
        url="https://www.jianshu.com/u/3c58aa6164de"
    )
    reply.add_article(article)
    return reply


# 用户发送图片
@robot.image
def blog(message,session):
    #print("msg", message.img)
    #print(type(message))
    #print(type(message.img))
    #print(message.__dict__)
    print("\n"+message.MediaId)
    changdu = str(len(session))
    session[changdu] = message.MediaId
    reply = ImageReply(message=message, media_id=message.MediaId)
    return reply


# 随机一首音乐
def music_data():
    music_list = [
            ['童话镇','陈一发儿','https://e.coka.la/wlae62.mp3','https://e.coka.la/wlae62.mp3'],
            ['都选C','缝纫机乐队','https://files.catbox.moe/duefwe.mp3','https://files.catbox.moe/duefwe.mp3'],
            ['精彩才刚刚开始','易烊千玺','https://e.coka.la/PdqQMY.mp3','https://e.coka.la/PdqQMY.mp3']
            ]
    num = random.randint(0,2)
    return music_list[num]


# 匹配 音乐 回复一首歌
@robot.filter('音乐')
def music(message):
    # reply = TextReply(message=message, content=music_data())
    # reply = MusicReply(message=message,source='https://www.kugou.com/song/#hash=D4EB517A405FCDF0286AA9A4487BBCE1&album_id=10409377')
    return music_data()
    # return reply

# 调用智能回复接口
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '43826fe7f1e74add804dd47cf2791228',    # Tuling Key，API的值
        'info': msg,    # 发出去的消息
        'userid': '441670',     # 用户名
    }
    r = requests.post(apiUrl, data=data).json()   # post请求
    return r.get('text')


# 文字智能回复
@robot.text
def replay(msg):
    print(msg.content)
    curtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    response = get_response(msg.content)
    print(
        curtime + '  公众号(机器人)' + ':' + response)
    return response


# 让服务器监听在 0.0.0.0:80
robot.config['HOST']='0.0.0.0'
robot.config['PORT']=80
robot.run()
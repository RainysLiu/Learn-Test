#!/usr/bin/env python
# -*- coding:utf-8 -*-


import random
import re
import time
import requests
import werobot
from bs4 import BeautifulSoup
from werobot.replies import ArticlesReply, Article, ImageReply, TextReply, MusicReply
from xpinyin import Pinyin


robot=werobot.WeRoBot(token='liuang123456')


# 订阅后的回复
@robot.subscribe
def subscribe():
    return "***欢迎关注公众号[愉快][愉快][愉快]***\n" \
           "***输入古诗文关键字检索古诗文！\n" \
           "***输入其他任意关键字与我聊天！\n" \
           "***输入'博客'关注我的博客!\n" \
           "***输入'音乐'为小主送上舒缓的歌曲!\n"


# 关键字 博客 回复
@robot.filter('博客')
def blog(message):
    reply = ArticlesReply(message=message)
    article = Article(
        title="忧郁的炸酱面",
        description="我的个人博客",
        img="https://cdn2.jianshu.io/assets/default_avatar/8-a356878e44b45ab268a3b0bbaaadeeb7.jpg?imageMogr2/"
            "auto-orient/strip|imageView2/1/w/120/h/120",
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


@robot.text
def replay(msg):
    print(msg.content)
    curtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # 寻找诗文
    poem, url = show_poem(msg.content)
    if not poem:
        # 若没有诗文,文字智能回复
        response = get_response(msg.content)
    else:
        if len(poem) > 200:
            poem = poem[:180] + '\n......\n' + url
        response = poem
    print(curtime + '  公众号(机器人)' + ':\n' + response)
    return response


def get_header():
    """
    获取头
    :return:
    """
    user_agent = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) "
        "Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) "
        "Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; ."
        "NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    ]
    # 随机获取一个浏览器
    rand_agent = random.choice(user_agent)
    # 拼装请求头
    return {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,images/webp,images/apng,*/*;q=0.8",
        "User-Agent": rand_agent,
    }


def get_gushi_url(name):
    """
    判断专题的页面是否存在
    :param url: url
    :return: 古诗专题url/False，名称/None
    """
    try:
        header = get_header()
        # print(name)
        name_len = len(name)

        # print(pinyin)
        if len(name) == 2:
            pinyin = Pinyin().get_pinyin(name).replace('-', '')
            url = 'https://so.gushiwen.org/gushi/%s.aspx' % pinyin
            response = requests.get(url, headers=header)
            # print(response.status_code)
            content = response.content.decode('utf8')
            # print(content)
            if '该网页不存在或存在错误' in content:
                # print('没有找到‘%s’相关古诗文专题！' % name)
                return False
            else:
                # print(url)
                return url
        else:
            rand_name = []
            for i in range(name_len-1):
                for y in range(i+1, name_len):
                    rand_name.append(name[i] + name[y])
            # print(rand_name)
            for r_name in rand_name:
                pinyin = Pinyin().get_pinyin(r_name).replace('-', '')
                # print(pinyin)
                url = 'https://so.gushiwen.org/gushi/%s.aspx' % pinyin
                response = requests.get(url, headers=header)
                # print(response.status_code)
                content = response.content.decode('utf8')
                # print(content)
                if '该网页不存在或存在错误' in content:
                    if r_name == rand_name[-1]:
                        # print('没有找到‘%s’相关古诗文专题！' % name)
                        return False
                    continue
                else:
                    # print(url)
                    su = BeautifulSoup(content, 'lxml')
                    title = su.find('div', class_='title').get_text().strip()
                    # print(title)
                    if name in title:
                        # print(name, url)
                        return url
                    else:
                        if r_name == rand_name[-1]:
                            # print('没有找到‘%s’相关古诗文专题！' % name)
                            return False
                        continue
    except:
        return False


def get_rand_span(url, cate_lable):
    """
    获取分类的列表
    :param url: 详情页url
    :return:分类的列表/None
    """
    try:
        response = requests.get(url, get_header())
    except:
        return None
    response.encoding='utf8'
    result = response.content
    su = BeautifulSoup(result, 'lxml')
    sonsdiv= su.find('div', class_="sons")
    # print(sonsdiv)
    catedivs = sonsdiv.find_all('div', class_=cate_lable)
    # print(catedivs)
    if len(catedivs) == 1:
        all_span = catedivs[0].find_all('span')
    else:
        rand_cate = random.choice(catedivs)
        all_span = rand_cate.find_all('span')
    rand_span = random.choice(all_span)
    # print(rand_span)
    return rand_span


def get_gushi(url):
    """
    获得古诗或者文章的详情页
    :param url: url
    :return: 古诗url返回的页面的BeautifulSoup对象格式/None
    """
    try:
        response = requests.get(url, headers=get_header())
    except:
        return None
    response.encoding = 'utf8'
    result = response.content
    su = BeautifulSoup(result, 'lxml')
    return su

def show_detail(span):
    """
    具体下载某篇文章或诗文
    :return: 无
    """
    tittle = span.get_text()
    tittle = re.findall('(.*?)\(.*?\)', tittle)[0].replace('/', '')
    detailurl = 'https://so.gushiwen.org' + span.find('a')['href']
    gushi = get_gushi(detailurl)
    age_author = gushi.find('p', class_='source').get_text()
    content = gushi.find('div', class_='contson').get_text()
    allcontent = tittle + '\n--' + age_author + '\n' + content
    allcontent = allcontent.replace('。', '。\n')
    return allcontent,detailurl


def find_poem(name):
    url = 'https://so.gushiwen.org/search.aspx?value=' + name
    response = requests.get(url, headers=get_header())
    response.encoding = 'utf8'
    result = response.content
    # print(context)
    if '未搜索到' in result.decode('utf8'):
        return False,None
    try:
        su = BeautifulSoup(result, 'lxml')
        sons = su.find('div', class_="sons")
        p = sons.find('div', class_="cont").find('p')
        title = p.get_text().strip()
        # print(title)
        if name not in title:
            return False,None
        url = 'https://so.gushiwen.org' + p.find('a')['href']
        gushi = get_gushi(url)
        age_author = gushi.find('p', class_='source').get_text()
        content = gushi.find('div', class_='contson').get_text()
        allcontent = title + '\n--' + age_author + '\n' + content
        allcontent = allcontent.replace('。', '。\n')
        # print(allcontent)
    except:
        return False,None
    return allcontent, url


def show_poem(name):
    """
    获取关键字古诗
    :return:无
    """
    # 查询并获取输入诗集名的目录页面url
    url = get_gushi_url(name)
    # print(url)
    # 如果找不到诗集，下载失败
    if not url:
        print('没有类型为"%s"古诗！' % name)
        poem, p_url = find_poem(name)
        if not poem:
            print('没有名为《%s》的古诗！' % name)
            return False, None
        else:
            return poem, p_url
    # 随机获取一首相关诗
    span = get_rand_span(url, "typecont")
    rand_poem, r_url = show_detail(span)
    # print(rand_poem)
    return rand_poem, r_url


# 让服务器监听在 0.0.0.0:80
robot.config['HOST']='0.0.0.0'
robot.config['PORT']=80
robot.run()


if __name__ == '__main__':
    pass
    # show_poem('爱情')
    # find_poem('长恨歌')
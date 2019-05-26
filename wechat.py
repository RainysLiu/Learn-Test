import itchat
import requests
import time


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '43826fe7f1e74add804dd47cf2791228',    # Tuling Key，API的值
        'info': msg,    # 发出去的消息
        'userid': '441670',     # 用户名
    }
    r = requests.post(apiUrl, data=data).json()   # post请求
    return r.get('text')


@itchat.msg_register(itchat.content.TEXT, itchat.content.CARD,itchat.content.PICTURE,itchat.content.NOTE)   # 用于接收来自朋友间的对话消息
def print_content(msg):
    print(msg)
    curtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if msg['FromUserName'] == '@39134b206677e6fa6cb6ec2689089acc095f155017f3eb8ffb9e8303e197a68c':
        print(curtime + '  ' + '我------>' + msg['User']['RemarkName'] + '(' + msg['User']['NickName'] + ')' + ':' + msg['Text'])
    else:
        print(curtime + '  ' + msg['User']['RemarkName'] + '(' + msg['User']['NickName'] + ')' + ':' + msg['Text'])
        response = get_response(msg['Text'])
        print(curtime + '  我(机器人)------>' +msg['User']['RemarkName'] + '(' + msg['User']['NickName'] + ')' + ':' + response)
        return response

# @itchat.msg_register([itchat.content.TEXT], isGroupChat=True) # 用于接收群里面的对话消息
# def print_content(msg):
#     curtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     print(curtime + '  ' + msg['User']['RemarkName'] + '(' + msg['User']['NickName'] + ')' + ':' + msg['Text'])
#     response = get_response(msg['Text'])
#     print(curtime + '  我(机器人):' + response)
#     return response


itchat.auto_login(hotReload=True)    # 通过微信扫描二维码登录itchat.run()

itchat.run()

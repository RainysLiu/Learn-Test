# encoding=utf8
import getpass
import re
import requests


def check_work_list():
    # 创建一个会话,往下的所有get-post请求都要使用s进行发送
    s = requests.Session()

    userid = input('输入你的工号:')
    # pwd= getpass.getpass("请输入你的密码:")
    pwd = input('请输入你的密码:')
    post_url = 'http://ics.chinasoftosg.com/login'
    formdata = {
        'userid': userid,
        'linkpage': '',
        'userName':userid,
        'j_username': userid,
        'password': pwd,
        'j_password': pwd,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Referer': 'http://ics.chinasoftosg.com/SignOnServlet',
    }

    # 登陆网站
    r = s.post(post_url, data=formdata, headers=headers)
    # print(r.status_code,type(r.status_code))
    res_header = r.headers
    if '登录系统失败' in r.text or res_header.get('Set-Cookie') is None:
        print('账号或密码输入错误,登陆失败!')
        return False
    Set_Cookie = res_header['Set-Cookie']
    print('%s登录成功!' % userid)

    # 从cookie中获取presuuid
    result = re.findall(r'portal_presuuid=([\d|a-z]+);', Set_Cookie)
    # print(result)
    portal_presuuid = result[0]

    # 进入登录后的页面
    get_url = 'http://ics.chinasoftosg.com/page?presuuid=%s'%portal_presuuid
    res = s.get(url=get_url)
    # print(res.status_code)
    # print(res.headers)

    print('正在为您查询打卡记录中，请稍等...')

    #进入考勤页面
    s.get(url='http://kq.chinasoftosg.com:8000/workAttendance/login',)
    get_url = 'http://kq.chinasoftosg.com:8000/workAttendance/loginAction'
    s.get(url=get_url, headers=headers)
    # print(res.status_code)
    # print(res.headers)

    # s.get(url='http://ics.chinasoftosg.com:8000/popnotify/?appname=kq_pop')

    # 查看个人打卡数据
    post_url = 'http://kq.chinasoftosg.com:8000/workAttendance/importsExamineAction_getImportsExamine'
    formdata = {
        'importsExamineVo.page': '1',
        'importsExamineVo.pagesize': '25',
    }
    r = s.post(post_url, data=formdata)
    # print(r.status_code)
    # print(r.text)

    all_info = r.json()['Rows']

    print("欢迎您，'%s'地区员工'%s'，您的打卡记录如下:" % (all_info[0]['belongOnwershipPlace'],all_info[0]['lastName']))

    print('*'*50)
    print('   日期','   早打卡','晚打卡')

    for info in all_info:
        print(info['showRecordDate'],
              info['showBeginTime'],
              info['showEndTime'])


if __name__ == '__main__':
    check_work_list()
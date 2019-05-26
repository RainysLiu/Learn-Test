import os
import random
import requests
from bs4 import BeautifulSoup
import re
import time
from xpinyin import Pinyin


class GuShiWen(object):
    """
      古诗文网操作类
    """
    def __init__(self):
        """
        初始化
        """
        # 浏览器标识集
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
        self.header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,images/webp,images/apng,*/*;q=0.8",
            "User-Agent": rand_agent,
        }

    def get_proxy_content(self):
        """
        获取代理ip
        :return:代理ip
        """
        with open('hosts.txt','r') as fp:
            content = fp.read().split('\n')
        return content

    def get_cate_div_list(self, url, cate_lable):
        """
        获取分类的列表
        :param url: 详情页url
        :return:分类的列表/None
        """
        try:
            response = requests.get(url, headers=self.header,)
        except:
            return None
        response.encoding='utf8'
        result = response.content
        su = BeautifulSoup(result, 'lxml')
        sonsdiv= su.find('div', class_="sons")
        # print(sonsdiv)
        catedivs = sonsdiv.find_all('div', class_=cate_lable)
        # print(catedivs)
        return catedivs

    def get_gushi(self, url):
        """
        获得古诗或者文章的详情页
        :param url: url
        :return: 古诗url返回的页面的BeautifulSoup对象格式/None
        """
        try:
            response = requests.get(url, headers=self.header)
        except:
            return None
        response.encoding = 'utf8'
        result = response.content
        su = BeautifulSoup(result, 'lxml')
        return su

    def get_gushi_url(self, name):
        """
        判断专题的页面是否存在
        :param url: url
        :return: 古诗专题url/False，名称/None
        """
        # print(name)
        name_len = len(name)

        # print(pinyin)
        if len(name) == 2:
            pinyin = Pinyin().get_pinyin(name).replace('-', '')
            url = 'https://so.gushiwen.org/gushi/%s.aspx' % pinyin
            response = requests.get(url, headers=self.header)
            # print(response.status_code)
            content = response.content.decode('utf8')
            # print(content)
            if '该网页不存在或存在错误' in content:
                print('没有找到‘%s’相关古诗文专题！' % name)
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
                response = requests.get(url, headers=self.header)
                # print(response.status_code)
                content = response.content.decode('utf8')
                # print(content)
                if '该网页不存在或存在错误' in content:
                    if r_name == rand_name[-1]:
                        print('没有找到‘%s’相关古诗文专题！' % name)
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
                            print('没有找到‘%s’相关古诗文专题！' % name)
                            return False
                        continue

    def get_guji_url(self, dirname):
        """
        判断史籍存在与否并返回目录页url
        :param dirname: 史籍名
        :return: 古籍目录页面url/False
        """
        url = 'https://so.gushiwen.org/search.aspx?value=' + dirname
        try:
            response = requests.get(url, headers=self.header)
        except:
            return None
        response.encoding = 'utf8'
        result = response.content
        # print(result)
        su = BeautifulSoup(result, 'lxml')
        div = su.find('div', class_="sonspic")
        # print(div)
        if div is None:
            print('没有找到"%s"相关史籍！' % dirname)
            return False
        find_p = div.find('div',class_='cont').find('p')
        find_name = find_p.find('b').get_text()
        if find_name != dirname:
            print('没有找到"%s"相关史籍！' % dirname)
            return False
        url = find_p.find('a')['href']
        # print(url)
        # print(find_name)
        url = 'https://so.gushiwen.org/' + url
        # print(url)
        return url

    def download_poem(self):
        """
        下载专题诗集
        :return:无
        """
        name = input('请输入要下载的古诗集专题名:')
        # 查询并获取输入诗集名的目录页面url
        url= self.get_gushi_url(name)
        # print(url)
        # 如果找不到诗集，下载失败
        if not url:
            print('下载诗集《%s》失败！' % name)
            return False
        # 创建路径准备下载
        if not os.path.exists(name):
            os.mkdir(name)
        # 将目录页面分解为大章节块
        cate_div_list = self.get_cate_div_list(url, "typecont")
        # 按章节进行下载
        self.download_cate(cate_div_list, name)

    def download_guji(self):
        """
        下载史籍
        :return: 无
        """
        name = input('请输入要下载史籍名:')
        # 查询并获取输入史籍名的目录页面url
        url = self.get_guji_url(name)
        # print(url)
        # 如果找不到史籍，下载失败
        if not url:
            print('下载史籍《%s》失败！' % name)
            return False
        # 创建路径准备下载
        if not os.path.exists(name):
            os.mkdir(name)
        # 将目录页面分解为大章节块
        cate_div_list = self.get_cate_div_list(url, "bookcont")
        # 按大章节进行下载
        self.download_cate(cate_div_list,name)

    def download_detail(self, gushilist, dir_name, catename = None):
        """
        具体下载某篇文章或诗文
        :return: 无
        """
        s = 1
        for x in gushilist:
            tittle = x.get_text()
            try:
                tittle = re.findall('(.*?)\(.*?\)', tittle)[0]
            except:
                pass
            detailurl = 'https://so.gushiwen.org' + x.find('a')['href']
            gushi = self.get_gushi(detailurl)
            age_author = gushi.find('p', class_='source').get_text()
            content = gushi.find('div', class_='contson').get_text()
            allcontent = tittle + '\n--' + age_author + '\n' + content
            if not catename:
                f = open(os.path.join('./' + dir_name, tittle + '.txt'), 'wb')
            else:
                f = open(os.path.join('./' + dir_name, catename, tittle + '.txt'), 'wb')
            f.write(allcontent.encode('utf8'))
            if catename:
                print('《%s》之《%s》第%d篇《%s》下载成功!!!' % (dir_name, catename, s, tittle))
            else:
                print('《%s》第%d篇《%s》下载成功!!!' % (dir_name, s, tittle))
            s += 1
        if catename:
            print('"%s"之----"%s"下载完成！----------------' % (dir_name, catename))
        time.sleep(2)

    def download_cate(self, cate_div_list, dir_name):
        """
        下载详情章节下的内容
        :return: 无
        """
        # print(cate_div_list)
        if len(cate_div_list) == 1:
            gushilist = cate_div_list[0].find_all('span')
            self.download_detail(gushilist, dir_name)
        else:
            for i in range(len(cate_div_list)):
                catediv = cate_div_list[i]
                catename = catediv.find('div',class_="bookMl").get_text()
                if not os.path.exists(os.path.join(os.path.dirname(__file__),dir_name,catename)):
                    os.mkdir(os.path.join(os.path.dirname(__file__),dir_name,catename))
                gushilist = catediv.find_all('span')
                self.download_detail(gushilist, dir_name, catename)
        print('下载《%s》成功！' % dir_name)

    def download(self):
        """
        选择要下载的类型进行下载
        :return: 无
        """
        choice = input('请选择你要下载的类型(1.史书 2.诗集),输入对应数字:')
        if choice == '1':
            self.download_guji()
        if choice == '2':
            self.download_poem()


if __name__ == '__main__':
    # 实例化古诗文对象
    gushiwen = GuShiWen()

    # 调用下载方法
    gushiwen.download()

    # ***************测试*******************************
    # gushiwen.get_gushi_url('小学古诗')
    # gushiwen.get_guji_url('元史')

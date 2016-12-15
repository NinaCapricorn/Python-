# coding=utf-8
import urllib2
import urllib
import cookielib
import json
import random


def post_https(base_url, url):
    '''
     :param base_url: 目的是获取抽奖post请求中的cookie信息
     :param url: 目的URL（抽奖url）
     :return: 返回奖品id
    '''
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    urllib2.urlopen(base_url)
    data = {}
    post_data = urllib.urlencode(data)
    rep = urllib2.Request(url, post_data)
    resp = urllib2.urlopen(rep)
    content = json.loads(resp.read())  # 转换成json字符串
    prize_id = content['data']['prize_id']  # 获取prize_id数据
    return prize_id


def pro_prize(list_price):
    '''
    :param list_price: 统计抽奖次数，为二维数组
    :return: 抽奖概率
    '''
    for j in range(0, len(list_price)):
        length = len(list_price[j])
        total_times = float(sum(list_price[j]))
        for i in range(0, length):
            list_price[j][i] /= total_times
            list_price[j][i] = round(list_price[j][i], 2)
        return list_price


def simulate_draw(base_url, draw_url, num, list_prize_id):
    '''
    :param base_url: base_url 目的为了获取cookie
    :param draw_url: 抽奖url
    :param num: 模拟num轮抽奖，每轮抽奖的次数(1, 1000)随机产生
    :param list_prize_id: 奖品id列表,例如 [1, 2, 3]
    :return: 返回抽奖次数列表，为二维数组
    '''
    prize_num = len(list_prize_id)
    list_total = [[0] * prize_num]*num  # 初始化抽奖次数
    for i in range(0, num):  # 执行num轮抽奖操作
        total = random.randint(1, 1000)  # 随机生成抽奖次数
        for j in range(1, total+1):
            prize_id = post_https(base_url, draw_url)
            for k in list_prize_id:
                if prize_id == k:
                    list_total[i][k-1] += 1
        print '第 ' + str(i) + ' 轮抽奖结束'
    return list_total


def main():
    draw_url = 'xxx'  # postUrl
    base_url = 'xxx'
    list_prize_id = [1, 2, 3, 4, 5, 6, 7, 8]  # 奖项id类别
    num = 1
    list_total = simulate_draw(base_url, draw_url, num, list_prize_id)
    res = pro_prize(list_total)
    print res


if __name__ == '__main__':
    main()

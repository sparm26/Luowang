import requests
from bs4 import BeautifulSoup
import wget
import os


def get_info(vol_num):
    try:
        url = "http://www.luoo.net/music/" + vol_num
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "lxml")
        titles = soup.select("a.btn-play")
        print("已获取第" + vol_num + "期歌单:")
        for title in titles:
            t = title.get_text()
            print(t)
    except:
        print("期数错误!!!")


def download_music(vol_num, download_num):
    try:
        down_url = "http://luoo-mp3.kssws.ks-cdn.com/low/luoo/radio" + vol_num + "/" + download_num + ".mp3"
        wget.download(down_url)
        wget.filename_from_url(down_url)
        print("正在下载落网" + vol_num + "期第" + download_num + "首歌曲")
        print("下载完成!")
    except:
        print("编号错误!!!")


def get_musicnum(vol_num):
    url = "http://www.luoo.net/music/" + vol_num
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    titles = soup.select("a.btn-play")
    music_nums = []
    for title in titles:
        t = title.get_text()[:2]
        music_nums.append(t)

    return music_nums


def download_all(vol_num, music_num):
    try:
        all_url = "http://luoo-mp3.kssws.ks-cdn.com/low/luoo/radio" + vol_num + "/" + music_num + ".mp3"
        wget.download(all_url)
        wget.filename_from_url(all_url)
        print("正在下载落网" + vol_num + "期第" + music_num + "首歌曲...")
        print("下载完成!")
    except:
        print("第" + music_num + "首歌曲下载失败")

if __name__ == "__main__":
    print("-------落网音乐下载-------")
    print("#######开始程序请'0'######")
    start = input()
    while start == "0":
        print("请输入期刊号:")
        vol_num = input()
        get_info(vol_num)
        print("请输入第" + vol_num + "期歌曲对应编号\n" + "*下载当期所有歌曲请输入'all'*")
        download_num = input()
        path = 'D:\\luowang\\' + vol_num
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)
        if download_num != "all":
            download_music(vol_num,download_num)
            print("指定歌曲下载任务已完成!")
        else:
            get_musicnum(vol_num)
            for music_num in get_musicnum(vol_num):
                download_all(vol_num,music_num)
            print("第" + vol_num + "期歌曲下载完成!")
        print("*继续下载请'0'*\n" + "#退出请回车#")
        start = input()
    print("-----------E N D----------")















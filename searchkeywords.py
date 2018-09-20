# -*- coding: utf-8 -*-
"""
@uthor: h.Shibao
date  : 2018/09/20
mail  : nokamiplace@gmail.com
"""
import requests
from bs4 import BeautifulSoup


def SpecifyWords(lst):
    """
    googleの検索エンジンに指定したリストワードを
    結合する。気が向いたらGoogle以外のエンジンを
    追加します。
    """
    url = 'https://www.google.co.jp/search?q='
    return url + '+'.join(lst)


def Parser(url):
    """
    引数として与えられたurlに対して
    構文解析を実施します。
    結果として検索順のサイトタイトルとurlを保持します。
    """
    ret = []
    
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    
    buf = soup.select(".r > a")
    
    for i, elem in enumerate(buf):
        
        dic = {}

        # 区切文字までの文字数インデックス算出
        index = elem.get("href").find("&")

        dic["index"] = i
        dic["title"] = elem.get_text()
        dic["url"]   = elem.get("href")[:index].replace("/url?q=", "")

        ret.append(dic)

    return ret

  
if __name__ == '__main__':
    keywords = ['DGB', 'マイニング']
    url = SpecifyWords(keywords)
    res = Parser(url)
    print(res)
    
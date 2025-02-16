#https://detail.tmall.hk/hk/item.htm?id=592801855548&spm=a211oj.20767644/ssrn.5673248570.d_tab1_item1.117841a8I3Ho5f&scm=1007.12144.81309.12722998_0_0&pvid=f9f984b6-b534-45b3-ab60-d6d18e96a4be&utparam=%7B%22x_hestia_source%22:%22gul_pc%22,%22x_object_type%22:%22item%22,%22x_hestia_subsource%22:%22gul_221696%22,%22x_mt%22:0,%22x_src%22:%22gul_pc%22,%22x_pos%22:1,%22wh_pid%22:221696,%22x_pvid%22:%22f9f984b6-b534-45b3-ab60-d6d18e96a4be%22,%22scm%22:%221007.12144.81309.12722998_0_0%22,%22x_object_id%22:592801855548,%22tpp_buckets%22:%222144
#这个商品的评论内容
import requests
import re
import time
#保存数据
import pandas as pd
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'referer':'https://detail.tmall.hk/hk/item.htm?id=592801855548&spm=a211oj.20767644/ssrn.5673248570.d_tab1_item1.117841a8I3Ho5f&scm=1007.12144.81309.12722998_0_0&pvid=f9f984b6-b534-45b3-ab60-d6d18e96a4be&utparam=%7B%22x_hestia_source%22:%22gul_pc%22,%22x_object_type%22:%22item%22,%22x_hestia_subsource%22:%22gul_221696%22,%22x_mt%22:0,%22x_src%22:%22gul_pc%22,%22x_pos%22:1,%22wh_pid%22:221696,%22x_pvid%22:%22f9f984b6-b534-45b3-ab60-d6d18e96a4be%22,%22scm%22:%221007.12144.81309.12722998_0_0%22,%22x_object_id%22:592801855548,%22tpp_buckets%22:%222144',
    #记得用自己的cookie去爬，最好延时时间越长越好，因为爬的快了会封ip
    'cookie':'t=aaed0e699eacd04f274304bed3a63c1b; lgc=; sn=; _tb_token_=0557effe3e03; cookie2=162a103cacd19bdf5a833d023d093433; cna=M/02IIx061YCAa+j/RB9Mxbg; xlly_s=1; mtop_partitioned_detect=1; _m_h5_tk=764843154ec263f69a3f11a989f062bc_1739600477235; _m_h5_tk_enc=617189b5762608d9c4d06429d6bdf852; dnk=ma_qiankun; uc1=pas=0&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie14=UoYdVFJBzR6uHg%3D%3D&cookie21=VFC%2FuZ9aiKcVcS5M9%2B3X; tracknick=%5Cu9A6Cno1; lid=%E9%A9%ACno1; _l_g_=Ug%3D%3D; unb=2334283880; cookie1=URp%2FkvaQVo43P5Qa9fbQ5ihKyOMVzLbz3hgSOqmF3ss%3D; login=true; wk_cookie2=1655953810a80f99ff1c975640967e8d; cookie17=UUtIEfnS87BS9w%3D%3D; _nk_=%5Cu9A6Cno1; sgcookie=E10085hMpkWs0ZIzRw7JIhkbmj9%2BqvNyynnQfEirHHt%2BL5MzL5Hik0j8dLKawTpW3x%2BasuJNzOz7Kuqm%2Bb278fJQo%2FIMtw%2FgFgiqcjCJY0T0ets%3D; cancelledSubSites=empty; sg=10e; csg=1ec4d7e0; wk_unb=UUtIEfnS87BS9w%3D%3D; tfstk=g_roKJbvCjO1VxP9wSo5WcsZ2IQxyLiIOWKK9DhFujlbvzhdPMXniRuRFWFLopVrGWn-4zHexShY9He8xrt3CJZRFDBSV8iIY1COXk27FDNLPGoUqKJqQ-ky427x0r5Y5-5OXGePzYiL31E-b7gKZvoEU2ky0tDEpBoEzHSVnvkpae-zT-WmGvtELXuEgjkiL3oEYWyVnvGqUfiw3bFUNo5qkauBWAdg0Y0o_8lue8EVL487ejYWP-NsTfSniH-UmYwA7Rgk4Gc4yyr-0u521my_k7kmjMvnnP2q4YVCf3izQ-zErkbpCXa03P30lLBSnu2gxA02gTcQ27qnPl59cbz0ckm8k_xtO2zYVVZRg3ma58n88SWeYX4qLgJHuFWgWHMVpo8BR4kjnfeHrNesGhjsVtXD7PgrhYSOntYBe4kjnfBcnFJozxMPX'
}

#创建一个空的数据表
df=pd.DataFrame()
for n in range(1,10):
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=592801855548&spuId=0&sellerId=2200657724895&order=3&currentPage='+str(n)+'&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvSpv8vWyvUvCkvvvvvjiWP2FO6j1bPFMUljivPmPZljYRnLzyQjYVRFc9tjDWdvhvmpvCI8osvvm2bL9CvvpvvhCv29hvCvvvMMGvvpvVvUCvpvvvmvhvLvvKV1%2BaA464d3ODN%2BFWdigqrADn9Wv7%2Bu6XwAq6D46X58t%2Bm7zU58TJ%2B3%2BI1jZ7%2Bu0OwkM6D40Xeut%2Bm7zhVuTJ%2B3%2BIsjZ7%2Bu6wjomgvpvIvvCvpvvvvvvvvhnCvvvC4pvvByOvvUhQvvCVB9vv9BQvvhXVvvmCj89Cvv9vvhh6wrZpJI9CvvOCvhE2gWAevpvhvvCCBUOCvvpv9hCv&needFold=0&_ksTS=1604647728169_1125&callback=jsonp1126'
    data = requests.get(url, headers=headers).text
    #设置延时，怕发现是爬虫，不容易触发反爬
    time.sleep(2)
    #请求
    data = requests.get(url, headers=headers).text
    #正则提取
    pat = re.compile('"rateContent":"(.*?)","fromMall"')
    # 按匹配规则找出评论来
    #extend函数是合并，findall匹配后的数据
    texts=[]
    texts.extend(pat.findall(data))
    df = df._append(texts, ignore_index=True)
#标题评论
#保存成excel格式
df.to_excel('韩国吕氏洗发水.xlsx')
print(df)

# coding=utf-8
import urllib
import urllib2,time,hashlib,json

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='
headers ={
    "Referer":"http://fanyi.youdao.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
    'Cookie':'OUTFOX_SEARCH_USER_ID=922262152@10.168.8.63; JSESSIONID=aaaxEgaYt1SCu8YDPfzdw; OUTFOX_SEARCH_USER_ID_NCOO=434003269.7171529; fanyi-ad-id=39535; fanyi-ad-closed=1; ___rl__test__cookies=1515470752400'
}

E = "fanyideskweb"
key = raw_input ("请输入需要翻译的内容:")
timenow = str(time.time()*1000)
O = "aNPG!!u6sesA>hBAW1@(-"
sign = hashlib.md5(E + key + timenow + O).hexdigest()

fromdata = {
    "i":key,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":E,
    "salt":timenow,
    "sign":sign,
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_CLICKBUTTION",
    "typoResult":"false",
}

data = urllib.urlencode(fromdata)
request = urllib2.Request(url,data=data,headers=headers)
response = urllib2.urlopen(request).read()
translation = json.loads(response)

print u'翻译的结果为：%s'%translation['translateResult'][0][0]['tgt']

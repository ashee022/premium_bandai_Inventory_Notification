import requests #파일 가저오기
from  bs4 import BeautifulSoup #파일 추출
import  datetime # 오늘날짜 구하기위
import telegram
import subprocess


now = str(datetime.datetime.now())
print(now)
#nalja = now[:4] + now[5:7] + now[8:10]
#print(nalja)

req = requests.get("https://www.bnkrmall.co.kr/premium/p_category.do")

#print(req.text)
soup = BeautifulSoup(req.text, "html.parser")
#print(soup)


pri_list=["../goods/detail.do?gno=57440"]


divtag = soup.find_all("div","list open fclear") #find 에서 find all 로 바꾸니 다나옴.
#print(divtag)

li2 = []

for i in divtag:
    li = i.find_all('p')
    #print(li)
    li2 = li2 + li

#print(li2)

info = ""
count = 0
for i in li2:
    info = info + i.text + "\n"
    count += 1

    if count % 3 == 0:
        info = info + "\n" # 3줄마다

info = now + "\n\n" + info
print(info)

#텔레그램.
to = "~~"#
bot = telegram.Bot(token = to)

#for i in bot.getUpdates():
#    print(i.message)

bot.send_message(5160104348, info)

subprocess.run("C:/Users/", shell=True) # 

'''
        to = ""##
        bot = telegram.Bot(token = to)

        #for i in bot.getUpdates():
        #    print(i.message)

        bot.send_message(5160104348, info) ##

    print("\n\n")


## 텔레그램
'''

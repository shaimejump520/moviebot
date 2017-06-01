from transitions.extensions import GraphMachine
import requests
import re
from bs4 import BeautifulSoup


def findtheater(path):
    response = requests.get(path)
    soup = BeautifulSoup(response.text,"html.parser")

    links=soup.find_all(attrs={"href": re.compile("/movie/f")})
    result=""
    moviename={}

    for n in range(0,len(links)):
        movietime={}
        moviename[n]=links[n].string
        if n!=0:
            if moviename[n]!=moviename[n-1]:
                result+=("\n"+moviename[n]+"\n")
        else:   
            result+=(moviename[n]+"\n")
        f=links[n].find_next(name="ul")
        f=f.find_next(name="ul")
        time=f.find_all(name="li")
        m=re.compile('\d\d：\d\d')
        i=0
        for i in range(len(time)):
            if m.match(time[i].text)!=None:
                result+=(time[i].text+" ")

    return result

def findtheater2(path):
    response = requests.get(path)
    soup = BeautifulSoup(response.text,"html.parser")

    links=soup.find_all(attrs={"href": re.compile("/movie/f")})
    result=""
    moviename={}

    for n in range(0,len(links)):
        movietime={}
        moviename[n]=links[n].string
        if n!=0:
            if moviename[n]!=moviename[n-1]:
                result+=(moviename[n]+"\n")
        else:
            result+=(moviename[n]+"\n")

        time=links[n].find_next(name="a",attrs={"class":"openbox"})
        movietime[0]=time.text
        i=1
        while time!=None:
            if time.find_next(name="li",attrs={"class":"theaterElse"}) is time.find_next(name="li"):
                break
            time=time.find_next(name="a")
            movietime[i]=time.text
            i=i+1

        for x in range(0,len(movietime)):
            result+=(movietime[x]+" ")
        result+="\n"

        
    return result


def findmoviename():
    response = requests.get("http://www.atmovies.com.tw/showtime/t06602/a06/")
    soup = BeautifulSoup(response.text,"html.parser")

    links=soup.find_all(attrs={"href": re.compile("/movie/f")})
    moviename={}
    moviename[0]=links[0].string

    for n in range(1,len(links)):
        for x in range(0,len(moviename)):
            if links[n].string==moviename[x]:
                break
            else:
                if x==(len(moviename)-1):
                    moviename[x+1]=links[n].string

        
    response = requests.get("http://www.atmovies.com.tw/showtime/t06607/a06/")
    soup = BeautifulSoup(response.text,"html.parser")

    links=soup.find_all(attrs={"href": re.compile("/movie/f")})

    for n in range(0,len(links)):
        for x in range(0,len(moviename)):
            if links[n].string==moviename[x]:
                break
            else:
                if x==(len(moviename)-1):
                    moviename[x+1]=links[n].string

    response = requests.get("http://www.atmovies.com.tw/showtime/t06608/a06/")
    soup = BeautifulSoup(response.text,"html.parser")

    links=soup.find_all(attrs={"href": re.compile("/movie/f")})

    for n in range(0,len(links)):
        for x in range(0,len(moviename)):
            if links[n].string==moviename[x]:
                break
            else:
                if x==(len(moviename)-1):
                    moviename[x+1]=links[n].string
    return moviename
def findmovietime(ordername):
    response = requests.get("http://www.atmovies.com.tw/showtime/t06602/a06/")
    soup = BeautifulSoup(response.text,"html.parser")

    links=soup.find_all(attrs={"href": re.compile("/movie/f")})
    result=""
    theater=0
    result+="南台影城\n"
    for n in range(0,len(links)):
        if links[n].string==ordername:

            f=links[n].find_next(name="ul")
            f=f.find_next(name="ul")
            time=f.find_all(name="li")
            m=re.compile('\d\d：\d\d')
            for i in range(len(time)):
                if m.match(time[i].text)!=None:
                    result+=(time[i].text+" ")
            result+="\n"


    response = requests.get("http://www.atmovies.com.tw/showtime/t06607/a06/")
    soup = BeautifulSoup(response.text,"html.parser")

    links=soup.find_all(attrs={"href": re.compile("/movie/f")})

    result+="新光影城\n"      
    for n in range(0,len(links)):
        if links[n].string==ordername:

            f=links[n].find_next(name="ul")
            f=f.find_next(name="ul")
            time=f.find_all(name="li")
            m=re.compile('\d\d：\d\d')
            for i in range(len(time)):
                if m.match(time[i].text)!=None:
                    result+=(time[i].text+" ")
            result+="\n"

    response = requests.get("http://www.atmovies.com.tw/showtime/t06608/a06/")
    soup = BeautifulSoup(response.text,"html.parser")

    links=soup.find_all(attrs={"href": re.compile("/movie/f")})

    result+="國賓影城\n"
    for n in range(0,len(links)):
        if links[n].string==ordername:

            f=links[n].find_next(name="ul")
            f=f.find_next(name="ul")
            time=f.find_all(name="li")
            m=re.compile('\d\d：\d\d')
            for i in range(len(time)):
                if m.match(time[i].text)!=None:
                    result+=(time[i].text+" ")
            result+="\n"

    return result

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '1'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == '2'
        
    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == '3'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'a'
        
    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == 'b'
        
    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == 'c'

    def is_going_to_state7(self, update):
        s=findmoviename()
        text = update.message.text
        for n in range(0,len(s)):
            if text==s[n]:
                return 1
        return 0

    def go_back_to_state1(self, update):
        text = update.message.text
        return text.lower() == '1'
        
    def go_back_to_state2(self, update):
        text = update.message.text
        return text.lower() == '2'
    
    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == '3'

    def go_back_to_user(self, update):
        text = update.message.text
        return text.lower() != None
	
    def is_going_to_default(self, update):
        text = update.message.text
        print(text)
        return ((text.lower() != '1')|
                (text.lower() != '2')|
                (text.lower() != '3'))

    def on_enter_user(self, update):
        update.message.reply_text("(1)影城(2)電影名稱(3)都要")


    def on_exit_user(self, update):
        print('Leaving user')

    def on_enter_state1(self, update):
        update.message.reply_text("(a)南台(b)新光(c)國賓")
        # self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')
    
    def on_enter_state2(self, update):
        # s=findmoviename()
        # update.message.reply_text("現正熱映中！")
        update.message.reply_text("請輸入電影名稱")

    def on_exit_state2(self, update):
        print('Leaving state2')
     
    def on_enter_state3(self, update):
        
        s="南台影城\n\n"
        s+=findtheater("http://www.atmovies.com.tw/showtime/t06602/a06/")
        s+="\n------------------------------------------------\n新光影城\n\n"
        s+=findtheater("http://www.atmovies.com.tw/showtime/t06607/a06/")
        s+="\n------------------------------------------------\n國賓影城\n\n"
        s+=findtheater("http://www.atmovies.com.tw/showtime/t06608/a06/")
        update.message.reply_text("各戲院電影時刻表如下"+s)
        update.message.reply_text("(1)查看影城(2)搜尋電影名稱(3)完成查詢")
        # self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        s=findtheater("http://www.atmovies.com.tw/showtime/t06602/a06/")
        update.message.reply_text("南台影城\n"+s)
        update.message.reply_text("(1)查看其他影城(2)直接搜尋電影名稱(3)完成查詢")

    def on_exit_state4(self, update):
        print('Leaving state4')
        
    def on_enter_state5(self, update):
        s=findtheater("http://www.atmovies.com.tw/showtime/t06607/a06/")
        update.message.reply_text("新光影城\n"+s)
        update.message.reply_text("(1)查看其他影城(2)直接搜尋電影名稱(3)完成查詢")

    def on_exit_state5(self, update):
        print('Leaving state5')
        
    def on_enter_state6(self, update):
        s=findtheater("http://www.atmovies.com.tw/showtime/t06608/a06/")
        update.message.reply_text("國賓影城\n"+s)
        update.message.reply_text("(1)查看其他影城(2)直接搜尋電影名稱(3)完成查詢")

    def on_exit_state6(self, update):
        print('Leaving state6')

    def on_enter_state7(self, update):
        text = update.message.text
        s=findmovietime(text)
        update.message.reply_text(s)
        update.message.reply_text("(1)直接查看影城(2)搜尋其它電影(3)完成查詢")

    def on_exit_state7(self, update):
        print('Leaving state7')

    def on_enter_state8(self, update):
        update.message.reply_text("感謝您的使用，請輸入任意訊息後再次查詢")

    def on_exit_state8(self, update):
        print('Leaving state8')    	

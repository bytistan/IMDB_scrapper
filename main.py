import requests
from bs4 import BeautifulSoup
import random 
import helper
from settings import *
import colorama

class Main:
    def __init__(self,country,tip):
        self.country = country
        self.tip = tip
        self.url = f"https://www.imdb.com/calendar/?ref_=rlm&region={country}&type={tip}"

    def send_request(self,url):
        UAS = helper.read_file("resources/user_agent.txt")
        user_agent = UAS[random.randrange(len(UAS))].replace("\n","")
        headers = {'user-agent': user_agent}
        return requests.get(url, headers=headers)

    def header_extraction(self,article):
        header = article.find("h3")
        if header:
            return header.text
        else:
            return None 

    def exctract_content(self,ul):

        all_data = []

        for li in ul.findAll("li"):
            img = li.find("img")
            if not img: break
            src = img["src"]
            if not src: break
            a = li.find("a")
            if not a: break
            title = a.text
            all_ul = li.findAll("ul") 
            if not all_ul:break
            data = self.extract_category_and_writer(all_ul)
            all_data.append({
                        "src":src,
                        "title":title,
                        "all_category":data[0],
                        "all_writer":data[1]
                    })
            return all_data
 
    def extract_category_and_writer(self,all_ul):
            data = {
                0:[], # Category
                1:[]  # Writer
            }

            for index,ul in enumerate(all_ul):
                for li in ul.findAll("li"):
                    span = li.find("span")
                    if span:
                        data[index].append(span.text)

            return data            

    def page_sorting(self,soup):

        all_data = {} 

        for article in soup.findAll("article"):
            date = self.header_extraction(article)
            if not date: break 
            ul = article.find("ul")
            if not ul: break
            all_data[date] = self.exctract_content(ul)

        return all_data

    def run(self):
        r = self.send_request(self.url)
        if r.status_code == 200:
            print(colorama.Fore.GREEN + "\n[+] Successfully connected to the site.")
            soup = BeautifulSoup(r.text,"html.parser")
            data = self.page_sorting(soup)
            helper.write_json(data,self.tip) 
            print(colorama.Fore.GREEN + f"[+] Data successfully extracted.\n[+] Path : data/{self.tip}.json\n")
        else:
            print(colorama.Fore.RED + f"[-] Status code : {r.status_code}")   
if __name__ == "__main__":
    country = input("[?] \_(*-*)_/ [US,RU ...] : ")
    tip = input("""
+-+-----------+
|1| mOvie     |
+-+-----------+     
|2| TV        |
+-+-----------+
|3| TV ePsido |
+-+-----------+

[?] \_(*-*)_/  : """)

    if tip not in [1,2,3] and len(country) != 2:
        print(colorama.Fore.RED + "\n[-] ERROR : ╭∩╮( •̀_•́ )╭∩╮")
    else:
        upcoming_page = Main(country,TIP[int(tip)])
        upcoming_page.run()

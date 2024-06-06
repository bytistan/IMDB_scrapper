import requests
from bs4 import BeautifulSoup
import random 
import helper
from settings import *
import colorama

class Main:
    def __init__(self,country,tip,img_flag):
        self.country = country
        self.tip = tip
        self.url = f"https://www.imdb.com/calendar/?ref_=rlm&region={country}&type={tip}"
        self.img_flag = img_flag

    def send_request(self,url):
        UAS = helper.read_file("resources/user_agent.txt")
        user_agent = UAS[random.randrange(len(UAS))].replace("\n","")
        headers = {"user-agent": user_agent}
        return requests.get(url, headers=headers)

    def header_extraction(self,article):
        header = article.find("h3")
        if header:
            return header.text
        else:
            return None 

    def exctract_content(self,ul,date):

        all_data = []

        for li in ul.findAll("li"):
            try:
                src = li.find("img")["src"]
                title = li.find("a").text
                all_ul = li.findAll("ul") 

                cr = self.extract_category_and_writer(all_ul)

                temp = {"src":src,
                        "title":title,
                        "all_category":cr[0] if cr else None,
                        "all_writer":cr[1] if cr else None }


                if self.img_flag:
                    path = "data/img/" + date.lower().replace(" ","_") + temp["title"].replace(" ","_") + ".jpg"
                    success = self.download_image(temp["src"],path)
                    if success:
                        temp["src"] = path
                    else:
                        temp["src"] = None

                all_data.append(temp)
            except Exception as e:
                pass 
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
            ul = article.find("ul")
            all_data[date] = self.exctract_content(ul,date)

        return all_data

    def download_image(self,url, save_path):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(save_path, "wb") as f:
                    f.write(response.content)
                return True
            else:
                return False
        except Exception as e:
            return False 
        
    def run(self):
        r = self.send_request(self.url)
        if r.status_code == 200:
            print(colorama.Fore.GREEN + "\n[+] Successfully connected to the site.")
            soup = BeautifulSoup(r.text,"html.parser")
            data = self.page_sorting(soup)
            helper.write_json(data,self.tip) 
            print(colorama.Fore.GREEN + f"[+] Data successfully extracted.\n[+] Path : data/json/{self.tip}.json\n")
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
    download_img = input("\nDownload image (y/n):")
    img_flag = False

    if "y" in download_img.lower() and len(download_img) < 4:
       img_flag = True 

    if tip not in [1,2,3] and len(country) != 2:
        print(colorama.Fore.RED + "\n[-] ERROR : ╭∩╮( •̀_•́ )╭∩╮")
    else:
        upcoming_page = Main(country,TIP[int(tip)],img_flag)
        upcoming_page.run()

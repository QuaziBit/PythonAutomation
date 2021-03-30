import time
import datetime
import requests
import urllib3
from bs4 import BeautifulSoup

class PageCrawler:

    def __init__(self):
        self.tr_count = 0
        self.td_count = 0
        self.total_run_time = 0
        print(f'Page Crawler')

    # create a get request and retrive html page
    def get_html(self, ticker):

        # timeout = Timeout(connect=4.0, read=10.0)
        http = urllib3.PoolManager()

        # using candle sticks
        url = f'''https://bigcharts.marketwatch.com/advchart/frames/frames.asp?show=&insttype=&symb={ticker}&x=39&y=12&time=7&startdate=1%2F4%2F1999&enddate=2%2F1%2F2021&freq=1&compidx=aaaaa%3A0&comptemptext=&comp=none&ma=5&maval=20+40&uf=0&lf=4&lf2=32&lf3=1&type=4&style=320&size=2&timeFrameToggle=false&compareToToggle=false&indicatorsToggle=false&chartStyleToggle=false&state=11'''

        http_pool = ""
        web_page = ""
        html = "null"
        status_code = 400

        try:
            http_pool = urllib3.connection_from_url(url)
            web_page = http_pool.urlopen('GET',url)
            status_code = web_page.status
            
        except Exception as e:
            print(f'\n[-] ERROR: URL: {e}\n')

        print(f'[@] status-code: {status_code}')

        if status_code == 200:
            html = web_page.data.decode('utf-8')      

        return html

    def get_img(self, html):

        img = "ERROR"

        # create BeautifulSoup object and parse it
        soup = BeautifulSoup (html, features="lxml")

        # get tb by class='padded vatop' and get its first chield img
        tmp = soup.select('td.padded.vatop > img')

        try:
            img = str( tmp[0] ) # get first element in the list
        except Exception as e:
            print(f'\n[-] ERROR: IMG-API: {e}\n')

        return img

    def get_graph(self, ticker):

        img = "null"

        html = self.get_html(ticker)

        if html != 'null':
            img = self.get_img(html)

            if img == "ERROR":
                raise Exception(f"Cannot retrive graph for a ticker: {ticker}")

        return img

    def run(self, final_report):


        index = 0
        for k in final_report:
            t1 = datetime.datetime.now().second

            ticker = final_report[k][0][0]
            last_close = final_report[k][0][1]

            print(f'[*][{index}] ticker: {ticker} --- last_close: {last_close}')

            img = ""
            api_error = False
            try:
                img = self.get_graph(ticker)
                api_error = False
            except Exception as e:
                print(f'\n[-] ERROR IMG-API: {e}\n')
                img = str(e)
                api_error = True

            print(f'{img}\n')

            self.write_fragmens(img, api_error, ticker, last_close, index)

            t2 = datetime.datetime.now().second
            dt = t2 - t1
            m = 0
            if dt > 0:
                # sometimes dt is negative value
                self.total_run_time = self.total_run_time + dt
            
            m = self.total_run_time / 60
            print(f'last task [{dt}] seconds:')
            print(f'\ttotal run time [{self.total_run_time}] seconds - [{m}] minutes\n')

            index += 1


    def write_fragmens(self, data, api_error, ticker, last_close, index):

        filename = "output.html"

        tmp_html = ""

        tmp = f'\n<h1>{index}: {ticker} - last-close: {last_close}</h1>\n'
        if api_error == True:
            tmp += f'<span style="color: red;">'
            tmp += data
            tmp += f'</span>'
        else:
            tmp += data
        tmp += "\n"

        if self.td_count == 2:
            self.td_count = 0

        if self.td_count == 0:
            tmp_html = f'<tr>\n<td>{tmp}</td>\n'

        if self.td_count == 1:
            tmp_html = f'<td>{tmp}</td>\n</tr>\n'

        self.td_count = self.td_count + 1

        html_object = open(filename, "a")
        # html_object.truncate(0) # errace old content
        html_object.write(tmp_html) # write new content 
        html_object.close()     # close IO stream



    
# Author: Olexandr "Alex" Matveyev
import time
import datetime
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class RunFirefox:
    
    def __init__(self, download_path, iframe_url, wb_path, firefox_dPath):
        self.tr_count = 0
        self.td_count = 0
        self.total_run_time = 0
        self.download_path = download_path
        self.iframe_url = iframe_url
        self.wb_path = wb_path
        self.firefox_dPath = firefox_dPath
        print(f'Run FireFox Selenium:')

    # test 4
    # s0: time in seconds --> system time
    # page_load_time: time in secods to wait for page to load
    # wait_time: Explicit wait time
    # driver_time: initialize the WebDriverWait --> driver time
    def run_firefox(self, s0, page_load_time, wait_time, driver_time):
        print(f'\tRun FireFox Selenium for [www.zacks.com]')

        # ---------------------------------------------------------------------------------------------------- #
        # find way to work with web browser popup window to save a csv file
        # set up profile to work around popup window to safe files
        options = OptionsFirefox()
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv")
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", self.download_path)
        #options.update_preferences()
        #browser = webdriver.WebDriver(firefox_profile=profile)

        binary = FirefoxBinary(self.wb_path)
        driver = webdriver.Firefox(firefox_options=options,executable_path=self.firefox_dPath)

        driver.get(self.iframe_url)

        driver.set_page_load_timeout(page_load_time)
        driver.implicitly_wait(driver_time)

        time.sleep(s0)

        # Company Descriptors
        tmp_xpath = '/html/body/main/section/div/div[2]/aside/div/div/div[2]/ul/li[2]/a'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Company Descriptors"
        print(f'{m}')

        time.sleep(s0)

        # Exchange
        tmp_xpath = '/html/body/main/section/div/div[2]/section/div[2]/div/div[2]/div/table/tbody/tr[1]/th/fieldset/span[2]/select/option[4]'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Exchange --> NSDQ"
        print(f'{m}')

        time.sleep(s0)

        # Add
        tmp_xpath = '/html/body/main/section/div/div[2]/section/div[2]/div/div[2]/div/table/tbody/tr[1]/td/a'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Add"
        print(f'{m}')

        time.sleep(s0)

        # Size & Share Volume 
        tmp_xpath = '/html/body/main/section/div/div[2]/aside/div/div/div[2]/ul/li[3]/a'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Size & Share Volume"
        print(f'{m}')

        time.sleep(s0)

        # Avg Volume
        val = 200000
        tmp_xpath = '//*[@id="val_12015"]'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.send_keys(f'{val}')
        m = f"Insert value {val}"
        print(f'{m}')

        time.sleep(s0)

        # Add
        tmp_xpath = '/html/body/main/section/div/div[2]/section/div[2]/div/div[2]/div/table/tbody/tr[3]/td/a'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Add"
        print(f'{m}')

        time.sleep(s0)

        # Price & Price Changes
        tmp_xpath = '/html/body/main/section/div/div[2]/aside/div/div/div[2]/ul/li[4]/a'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Price & Price Changes"
        print(f'{m}')

        time.sleep(s0)

        # Last Close
        val = 5
        tmp_xpath = '//*[@id="val_14005"]'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.send_keys(f'{val}')
        m = f"Insert value {val}"
        print(f'{m}')

        time.sleep(s0)

        # Add
        tmp_xpath = '/html/body/main/section/div/div[2]/section/div[2]/div/div[2]/div/table/tbody/tr[1]/td/a'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Add"
        print(f'{m}')

        time.sleep(s0)

        # Run Screen
        tmp_xpath = '//*[@id="run_screen_result"]'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Run Screen"
        print(f'{m}')

        time.sleep(s0)

        """
        # Drop down menu: records per page [default 15] set it to 100
        # Initialize the WebDriverWait, with 5 seconds of wait time.
        tmp_xpath = '/html/body/main/section/div/div[4]/div/div[1]/div[2]/ul/li[10]/select/option[3]'
        # records_per_page = wait.until(EC.element_to_be_clickable((By.XPATH, tmp_xpath)))
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Records per page --> 100"
        print(f'{m}')
        """

        time.sleep(s0)

        
        # download csv file
        tmp_xpath = '/html/body/main/section/div/div[4]/div/div[1]/div[2]/div[1]/div/div[1]/a[1]'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked CSV"
        print(f'{m}')
        
        time.sleep(s0)

        # Back to Screen --- My Criteria
        tmp_xpath = '/html/body/main/section/div/div[4]/div/div[1]/div[1]/a[1]'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked My Criteria"
        print(f'{m}')

        time.sleep(s0)

        # Exchange
        tmp_xpath = '/html/body/main/section/div/div[2]/section/div[1]/form/div/div[2]/table/tbody/tr/th/fieldset/div[1]/span[2]/select/option[5]'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Exchange --> NYSE"
        print(f'{m}')

        time.sleep(s0)

        # Run Screen
        tmp_xpath = '//*[@id="run_screen_result"]'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Run Screen"
        print(f'{m}')

        time.sleep(s0)

        # download csv file
        tmp_xpath = '/html/body/main/section/div/div[4]/div/div[1]/div[2]/div[1]/div/div[1]/a[1]'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked CSV"
        print(f'{m}')
        
        time.sleep(s0)

        driver.quit()
        m = "Quit driver."
        print(f'{m}')



    # s0: time in seconds --> system time
    # page_load_time: time in secods to wait for page to load
    # driver_time: initialize the WebDriverWait --> driver time
    def bigcharts_init(self, final_report, s0, page_load_time, wait_time, driver_time):

        failed_index = -1 # if program throw an exception remember what index was it
        failed_tickers_index = [] # store all failed indexes of tickers

        ticker = ""
        index = 0
        for k in final_report:
            # whe should start working on the ticker after a ticker that failed
            if index > failed_index:
                try:
                    print(f'\t[@]start index: {index}')
                    # run_bigcharts: if failed should return on what index it did fail
                    failed_index = self.run_bigcharts(index, final_report, s0, page_load_time, wait_time, driver_time)
                    failed_tickers_index.append(failed_index) # ad to a list failed ticker's index
                    print(f'\t[#] failed index: {failed_index}')
                    index = failed_index

                    # get a ticker name based on failed ticker's index
                    tmp_index = 0
                    for k2 in final_report:
                        if tmp_index == failed_index:
                            # write failed ticker info into output.html
                            ticker = final_report[k2][0][0]
                            last_close = final_report[k2][0][1]
                            # write failed ticker name into output.html
                            self.write_fragmens('null', ticker, last_close, failed_index)
                        tmp_index = tmp_index + 1

                except Exception as e:
                    print(f'Exception: {e}\n')
                finally:
                    print(f'All job done!\n')

            index = index + 1

        # print all tickers' indexes that failed
        for i in failed_tickers_index:
            print(f'failed tickers: {i}\n')
            
                

    # for https://bigcharts.marketwatch.com/
    # s0: time in seconds --> system time
    # page_load_time: time in secods to wait for page to load
    # driver_time: initialize the WebDriverWait --> driver time
    def run_bigcharts(self, start_index, final_report, s0, page_load_time, wait_time, driver_time):
        print(f'\tRun FireFox Selenium for [www.bigcharts.marketwatch.com]')

        # need to add ping test to check is connection to the website is availebel 

        # the failed_index should start with start_index 
        failed_index = start_index

        download_path = "C:\\Users\\alexm\Desktop\\Programs\\Software\\Programming\\ProgrammingProjects\\XHTML_CSS_JavaScript\\Python\\CrawlWebPage\\StockCrawler\\stocks\\\download\\"
        fx_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

        # url https://bigcharts.marketwatch.com/
        url = 'https://bigcharts.marketwatch.com/default.asp'

        # init web-driver
        # ---------------------------------------------------------------------------------------------------- #
        # firefox_dPath = "C:\Python\Drivers\BrowersDriver\Firefox\geckodriver.exe"
        firefox_dPath = "drivers/Firefox/geckodriver.exe"

        # find way to work with web browser popup window to save a csv file
        # set up profile to work around popup window to safe files
        options = OptionsFirefox()
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv")
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", download_path)
        #options.update_preferences()
        #browser = webdriver.WebDriver(firefox_profile=profile)

        binary = FirefoxBinary(fx_path)
        driver = webdriver.Firefox(firefox_options=options,executable_path=firefox_dPath)

        driver.get(url)

        driver.set_page_load_timeout(page_load_time)
        driver.implicitly_wait(driver_time)

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0

        # values for bigcharts.marketwatch.com
        # time: 6 month
        # frequency: daily
        # moving average: EMA (2-line) - 20 40
        # uper indicators: none
        # lower indicators 1: MACD
        # lower indicators 2: Slow Stochastic
        # lower indicators 3: Volume

        # loop over generated report that has all tickers
        # get the image chart from the bigcharts website based on the tickers
        # save images in the word document

        # section: init search
        # init first run to get first ticker
        ticker = ""
        last_close = ""
        index = 0
        for k in final_report:
            if index == start_index:
                ticker = final_report[k][0][0]
                last_close = final_report[k][0][1]
                print(f'\t[*][{start_index}] ticker: {ticker} --- last_close: {last_close}')
                failed_index = index
                break
            index += 1

        # Search
        val = ticker
        tmp_xpath = '/html/body/header/div[1]/div[3]/div[1]/form[3]/input[1]'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.send_keys(f'{val}')
        m = f"Insert value {val}"
        print(f'{m}')

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0

        # section: Advanced Chart 
        # Advanced Chart
        tmp_xpath = '/html/body/header/div[1]/div[3]/div[1]/form[3]/button[2]'
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Advanced Chart"
        print(f'{m}')

        time.sleep(s0)

        # section: time frame
        # time
        tmp_xpath = "/html/body/div[2]/div[2]/table/tbody/tr/td[1]/form/div[2]/div[1]/select[1]/option[9]"
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Time: 6 month"
        print(f'{m}')

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0

        # Frequency
        tmp_xpath = "/html/body/div[2]/div[2]/table/tbody/tr/td[1]/form/div[2]/div[1]/select[2]/option[6]"
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Frequency: Daily"
        print(f'{m}')

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0

        # section: indicator 
        # indicator drop down
        tmp_xpath = "/html/body/div[2]/div[2]/table/tbody/tr/td[1]/form/div[2]/h3[3]/a"
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Indicator Drop Down"
        print(f'{m}')

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0

        # Moving Evarage
        tmp_xpath = "/html/body/div[2]/div[2]/table/tbody/tr/td[1]/form/div[2]/div[3]/select[1]/option[6]"
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Moving Evarage"
        print(f'{m}')

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0

        # empty input
        val = ""
        tmp_xpath = '//*[@id="maval"]' # different input field
        element = driver.find_element_by_xpath(tmp_xpath)
        element.clear()
        element.send_keys(val)
        m = f"Insert value: clear"
        print(f'{m}')

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0

        # moving average value
        val = "20 40"
        tmp_xpath = '//*[@id="maval"]' # input: 20 40
        element = driver.find_element_by_xpath(tmp_xpath)
        element.send_keys(f'{val}')
        m = f"Insert value {val}"
        print(f'{m}')

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0

        # Lower Indicator 1:
        tmp_xpath = "/html/body/div[2]/div[2]/table/tbody/tr/td[1]/form/div[2]/div[3]/select[3]/option[4]"
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Lower Indicator 1"
        print(f'{m}')

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0

        # Lower Indicator 2:
        tmp_xpath = "/html/body/div[2]/div[2]/table/tbody/tr/td[1]/form/div[2]/div[3]/select[4]/option[8]"
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Lower Indicator 2"
        print(f'{m}')

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0
        
        # Lower Indicator 3: 
        tmp_xpath = "/html/body/div[2]/div[2]/table/tbody/tr/td[1]/form/div[2]/div[3]/select[5]/option[2]"
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Lower Indicator 3"
        print(f'{m}')

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0
        
        # section: chart style
        # price display drop down
        tmp_xpath = "/html/body/div[2]/div[2]/table/tbody/tr/td[1]/form/div[2]/h3[4]/a"
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Price Display Drop Down"
        print(f'{m}')

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0

        # price display
        tmp_xpath = "/html/body/div[2]/div[2]/table/tbody/tr/td[1]/form/div[2]/div[4]/select[1]/option[4]"
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Price Display"
        print(f'{m}')

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0

        """
        # chart background
        tmp_xpath = "/html/body/div[2]/div[2]/table/tbody/tr/td[1]/form/div[2]/div[4]/select[1]/option[4]"
        element = driver.find_element_by_xpath(tmp_xpath)
        # chart_bg = wait.until(EC.element_to_be_clickable((By.XPATH, chart_bg)))
        element.click()
        m = "Clicked Chart Background"
        print(f'{m}')

        time.sleep(s0)
        """

        """
        # chart size: large
        tmp_xpath = "/html/body/div[2]/div[2]/table/tbody/tr/td[1]/form/div[2]/div[4]/select[3]/option[3]"
        element = driver.find_element_by_xpath(tmp_xpath)
        # chart_size = wait.until(EC.element_to_be_clickable((By.XPATH, chart_size)))
        element.click()
        m = "Clicked Chart Size"
        print(f'{m}')

        time.sleep(s0)
        """

        # generate image
        tmp_xpath = "/html/body/div[2]/div[2]/table/tbody/tr/td[1]/form/div[3]/input"
        element = driver.find_element_by_xpath(tmp_xpath)
        element.click()
        m = "Clicked Draw Chart"
        print(f'{m}')

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0

        # get graph that is just an image
        css_selector = "td[class='padded vatop']"
        element = driver.find_element_by_css_selector(css_selector)

        # getting a list and we need first element
        img_element = element.find_elements_by_tag_name('img')[0].get_attribute('outerHTML')
        print(f'[0] {ticker}: {img_element}\n')

        # write into output.html
        self.write_fragmens(img_element, ticker, last_close, index)

        time.sleep(s0)
        self.total_run_time = self.total_run_time + s0

        # init first run to get first ticker
        ticker = ""
        last_close = ""
        index = 0
        for k in final_report:
            # we need to start from the second ticker
            if index > start_index:
                t1 = datetime.datetime.now().second

                ticker = final_report[k][0][0]
                last_close = final_report[k][0][1]
                print(f'ticker: {ticker} --- last_close: {last_close}')
            
                """
                # Option 1
                # --------------------------------------------------------------------------- #
                img_element = "null"
                try:
                    img_element = self.option_1_2(driver, ticker)
                except Exception as e:
                    failed_index = index
                    # write into output.html failed ticker
                    self.write_fragmens(img_element, ticker, last_close, index)
                    print(f'Exception: {e}\n')
                    driver.quit()
                    break
                finally:
                    # write into output.html
                    self.write_fragmens(img_element, ticker, last_close, index)

                    print(f'[{index}] {ticker}: {img_element}')
                
                t2 = datetime.datetime.now().second
                dt = t2 - t1
                if dt > 0:
                    # sometimes dt is negative value
                    self.total_run_time = self.total_run_time + dt
                print(f'last task [{dt}] seconds --- total run time [{self.total_run_time}] seconds\n')
                # --------------------------------------------------------------------------- #
                """
                

                # Option 2
                # --------------------------------------------------------------------------- #
                self.option_1_2_1(driver, ticker, last_close, index)
                t2 = datetime.datetime.now().second
                dt = t2 - t1
                if dt > 0:
                    # sometimes dt is negative value
                    self.total_run_time = self.total_run_time + dt
                print(f'last task [{dt}] seconds --- total run time [{self.total_run_time}] seconds\n')
                # --------------------------------------------------------------------------- #
                

                start_index = index
                failed_index = index

            index += 1

        return failed_index

    def option_1_2(self, driver, ticker):

        # get current url with the new ticker name
        currentUrl = driver.current_url
        s_code = 0

        try:
            # check is URL is working, and if not exit with s_code = 0
            req = requests.get(currentUrl)
            s_code = req.status_code
            print(f'\treq.status_code: {req.status_code}\n')
        except Exception as e:
            print(f'URL is unreachable: URL: {currentUrl} --- Exception: {e}\n')

        # throw exception and move to a different ticker
        if s_code != 200:
            raise Exception(f"URL is unreachable --- status-code: {s_code}") 

        # Option 1
        # --------------------------------------------------------------------------- #
        # empty input
        val = ""
        tmp_xpath = '//*[@id="symb"]' # different input field
        element = driver.find_element_by_xpath(tmp_xpath)
        element.clear()
        element.send_keys(val)
        m = f"Insert value: clear"
        print(f'{m}')

        # insert ticker value
        tmp_xpath = '//*[@id="symb"]' # different input field
        element = driver.find_element_by_xpath(tmp_xpath)
        element.send_keys(f'{ticker}')
        m = f"Insert value {ticker}"
        print(f'{m}')

        # generate image
        tmp_xpath = "/html/body/div[2]/div[2]/table/tbody/tr/td[1]/form/div[3]/input"
        element = driver.find_element_by_xpath(tmp_xpath)
        # draw_chart = wait.until(EC.element_to_be_clickable((By.XPATH, draw_chart)))
        element.click()
        m = "Clicked Draw Chart"
        print(f'{m}')

        # time.sleep(s0)
                
        img_element = "null"
        try:
            # get graph that is just an image
            css_selector = "td[class='padded vatop']"
            element = driver.find_element_by_css_selector(css_selector)
                    
            # getting a list and we need first element
            img_element = element.find_elements_by_tag_name('img')[0].get_attribute('outerHTML')
        except Exception as e:
            print(f'Exception: {e}\n')

        # --------------------------------------------------------------------------- #

        return img_element

    def option_1_2_1(self, driver, ticker, last_close, index):
        img_element = "null"
        try:
            # no candle sticks
            # b_url = f'''https://bigcharts.marketwatch.com/advchart/frames/frames.asp?show=&insttype=&symb={ticker}&x=47&y=17&time=7&startdate=1%2F4%2F1999&enddate=1%2F29%2F2021&freq=1&compidx=aaaaa%3A0&comptemptext=&comp=none&ma=5&maval=20+40&uf=0&lf=4&lf2=32&lf3=1&type=2&style=320&size=2&timeFrameToggle=false&compareToToggle=false&indicatorsToggle=false&chartStyleToggle=false&state=10'''

            # using candle sticks
            b_url = f'''https://bigcharts.marketwatch.com/advchart/frames/frames.asp?show=&insttype=&symb={ticker}&x=39&y=12&time=7&startdate=1%2F4%2F1999&enddate=2%2F1%2F2021&freq=1&compidx=aaaaa%3A0&comptemptext=&comp=none&ma=5&maval=20+40&uf=0&lf=4&lf2=32&lf3=1&type=4&style=320&size=2&timeFrameToggle=false&compareToToggle=false&indicatorsToggle=false&chartStyleToggle=false&state=11'''

            driver.get(b_url)

            # get graph that is just an image
            css_selector = "td[class='padded vatop']"
            element = driver.find_element_by_css_selector(css_selector)
                
            # getting a list and we need first element
            img_element = element.find_elements_by_tag_name('img')[0].get_attribute('outerHTML')
        except Exception as e:
            print(f'Exception: {e}\n')
            self.write_fragmens(img_element, ticker, last_close, index)
        finally:
            self.write_fragmens(img_element, ticker, last_close, index)

            print(f'[{index}] {ticker}: {img_element}')


    def write_fragmens(self, data, ticker, last_close, index):

        filename = "output.html"

        tmp_html = ""

        tmp = f'\n<h1>{index}: {ticker} - last-close: {last_close}</h1>\n'
        tmp += data
        tmp += "\n"
        #tmp += f'\n<br /><br />'
        # tmp += '\n\n'

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

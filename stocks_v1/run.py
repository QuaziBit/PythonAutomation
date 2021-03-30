import os
import sys
import time
import pathlib
import threading
from runfirefox import RunFirefox
from csv_reader import CSVReader
from page_crawler import PageCrawler
import concurrent.futures

# generate start and end indexes for each thread to start getting records from the dictionary of records
def split_records(final_report, num_of_records, num_of_threads):
    
    '''
    # print report
    index = 1
    for k in final_report:
        ticker = final_report[k][0][0]
        last_close = final_report[k][0][1]
        print(f'\t[*][{index}] ticker: {ticker} --- last_close: {last_close}')
        index += 1
    '''

    # records per thread
    rec_per_thread = {} # dictionary

    num_of_rec_per_thr = num_of_records / num_of_threads
    # print(f'\tRecords per thread [{num_of_rec_per_thr}]\n')

    # init dictionary
    n = 1
    while n <= num_of_threads:
        # create key and empty list to store index of where to stop in CSV file
        rec_per_thread[f'{n}'] = [] 
        n = n + 1
    rpt_size = len(rec_per_thread)
    # print(f'\tNumber of records in dictionary: [{rpt_size}]\n')
    
    # for odd number of recods
    records_head_index = 0 # max index for the records that can be split equally between threads
    records_tail_index = 0 # max index for the rest of recods
    tmp_recods = num_of_records

    if (num_of_records % num_of_threads) == 0:
        print(f'Records can be split evenly:')
        print(f'\tRecords per thread [{num_of_rec_per_thr}]\n')

        # convert into int
        num_of_rec_per_thr = int(num_of_rec_per_thr)

        # generate start and end index for each thread
        # the start index means start getting recods from the specific index in the CSV
        # the end index means get records from the CSV file till specific index
        n = 1
        shift_start = 0
        shift_end = num_of_rec_per_thr - 1
        while n <= num_of_threads:
            # generate start and end index for each thread
            start = shift_start
            end = shift_end
            #print(f'start: {start} --- end: {end}')
            temp_list = [start, end]
            # create key and empty list to store index of where to stop in CSV file
            rec_per_thread[f'{n}'] = temp_list

            shift_start = shift_start + num_of_rec_per_thr
            shift_end = shift_start + num_of_rec_per_thr - 1

            n = n + 1

        """
        # print dictionary
        for k in rec_per_thread:
            print(f'{k}:{rec_per_thread[k]}')
        """

    else:
        print(f'Records cannot be split evenly:')
        print(f'\t[1] Records per thread [{num_of_rec_per_thr}]\n')
            
        while (tmp_recods % num_of_threads) != 0:
            tmp_recods = tmp_recods - 1

        # number of records that can be divided equally among threads
        records_head = tmp_recods # even number of records

        # leftover records that will be added to the final thread
        records_tail = int(num_of_records) - records_head # leftover records

        print(f'\t[2*] Records head per thread [{records_head}]\n')
        print(f'\t[3*] Records tail per thread [{records_tail}]\n')

        # split even number of records between threads
        records_head = int(records_head) / num_of_threads
        records_head = int(records_head)

        # generate start and end index for each thread
        # the start index means start getting recods from the specific index in the CSV
        # the end index means get records from the CSV file till specific index
        n = 1
        shift_start = 0
        shift_end = records_head - 1
        while n <= num_of_threads:
            # generate start and end index for each thread
            start = shift_start
            end = shift_end
            # print(f'start: {start} --- end: {end}')

            if (n == num_of_threads):
                # print(f'last thread have extra {records_tail} records')
                end = end + records_tail

            temp_list = [start, end]
            # create key and empty list to store index of where to stop in CSV file
            rec_per_thread[f'{n}'] = temp_list

            shift_start = shift_start + records_head
            shift_end = shift_start + records_head - 1

            n = n + 1

        """
        # print dictionary
        for k in rec_per_thread:
            print(f'{k}:{rec_per_thread[k]}')
        """
        

    return rec_per_thread

# this function init object to work with the WebDiver
def thread_function(k, final_report_temp, s0, page_load_time, wait_time, driver_time):

    print(f'thread [{k}]: records:')

    index = 0
    for k in final_report_temp:
        ticker = final_report_temp[k][0][0]
        last_close = final_report_temp[k][0][1]
        print(f'\t[*][{index}] ticker: {ticker} --- last_close: {last_close}')
        index += 1

    print(f'\n')

    # Init FireFox Run
    # ---------------------------------------------------------------------------------- #
    run_firefox = RunFirefox()
    # ---------------------------------------------------------------------------------- #

    run_firefox.bigcharts_init(final_report_temp, s0, page_load_time, wait_time, driver_time)

    time.sleep(5)

# main function to work with the threads
def multithreading(final_report, csv_reader, num_of_records, s0, page_load_time, wait_time, driver_time):

    # multithreading
    # ---------------------------------------------------------------------------------- #
    # need to find a way to use multithreading to speed up data collaction proccess 
    # Get the number of CPUs 
    # in the system using 
    # os.cpu_count() method 
    cpuCount = os.cpu_count()
    # num_of_threads = cpuCount
    num_of_threads = int(cpuCount / 4 ) # for now we can use only 2 threads
    print(f'System has [{ int(cpuCount / 2 )}] CPU cores and can suport [{num_of_threads}] threads.')
    print(f'\tFinal report has [{num_of_records}] records.')

    # split records equally between threads
    # return dictionary
    rec_per_thread = split_records(final_report, num_of_records, num_of_threads)

    # loop over splitted indexes and create threads
    threads = list()
    for k in rec_per_thread:
        print(f'[*]{k}:{rec_per_thread[k]}')

        # get start and end index
        start = rec_per_thread[k][0]
        end = rec_per_thread[k][1]
        final_report_temp = csv_reader.slice_csv(start, end, final_report)

        # init thread
        t = threading.Thread(target=thread_function, args=(k, final_report_temp, s0, page_load_time, wait_time, driver_time))
        threads.append(t)
        t.start()


    for index, thread in enumerate(threads):
        thread.join()

    # Test
    # ----------------------------------------------------------------------------------- #
    """
    # Init FireFox Run
    # ---------------------------------------------------------------------------------- #
    run_firefox = RunFirefox()
    # ---------------------------------------------------------------------------------- #

    # get specific number of recods
    start = rec_per_thread['1'][0] # 0
    end = rec_per_thread['1'][1] # 375
    final_report_temp = r.slice_csv(start, end, final_report)

    # print report
    index = 1
    for k in final_report_temp:
        ticker = final_report[k][0][0]
        last_close = final_report[k][0][1]
        print(f'\t[*][{index}] ticker: {ticker} --- last_close: {last_close}')
        index += 1

    # Run firefox for https://bigcharts.marketwatch.com/
    # get a list
    # ---------------------------------------------------------------------------------- #
    s0 = 2 # time in seconds --> system time
    page_load_time = 180 # time in seconds to wait for page to load
    wait_time = 1 # Explicit wait time
    driver_time = 60 # implicitly wait time --> driver time 
    run_firefox.bigcharts_init(final_report_temp, s0, page_load_time, wait_time, driver_time)
    # ---------------------------------------------------------------------------------- #
    """
    # ----------------------------------------------------------------------------------- #

def singlethread(final_report, s0, page_load_time, wait_time, driver_time):

    # Init FireFox Run
    # ---------------------------------------------------------------------------------- #
    run_firefox = RunFirefox()
    # ---------------------------------------------------------------------------------- #

    # single thread
    # ---------------------------------------------------------------------------------- #
    # Run firefox for https://bigcharts.marketwatch.com/
    run_firefox.bigcharts_init(final_report, s0, page_load_time, wait_time, driver_time)
    # ---------------------------------------------------------------------------------- #

def main():

    # store downloaded CSV files
    download_path = f'{pathlib.Path().absolute()}\\download\\'
    print(f'path: {download_path}')

    # iframe url zacks.com
    iframe_url = 'https://screener-api.zacks.com/?scr_type=stock&c_id=zacks&c_key=0675466c5b74cfac34f6be7dc37d4fe6a008e212e2ef73bdcd7e9f1f9a9bd377&ecv=2ITM2QTOyQDO&ref=screening#'

    # path to web-browser
    wb_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

    # path to web-driver
    firefox_dPath = f'{pathlib.Path().absolute()}\\drivers\\Firefox\\geckodriver.exe'

    if len(sys.argv) >= 2:
        order = "no-sorting"
        output_fn = "all-no-sorting.csv"

        # test if user provided a sorting method
        # ---------------------------------------------------------------------------------- #
        if sys.argv[1] != "ascending" and sys.argv[1] != "descending":
            print(f'Default sorting for final report: {order}')
        elif sys.argv[1] == "ascending" or sys.argv[1] == "descending":
            order = sys.argv[1] # user should provide a sorting name
            print(f'Sorting for final report: {order}')
        # ---------------------------------------------------------------------------------- #

        # sort report
        # ---------------------------------------------------------------------------------- #
        if order == "ascending":
            output_fn = "all-ascending.csv"
        if order == "descending":
            output_fn = "all-descending.csv"
        # ---------------------------------------------------------------------------------- #

        # Init FireFox Run
        # ---------------------------------------------------------------------------------- #
        run_firefox = RunFirefox(download_path, iframe_url, wb_path, firefox_dPath)
        # ---------------------------------------------------------------------------------- #

        # init CSV Reader
        # ---------------------------------------------------------------------------------- #
        csv_dir = "download/"
        csv_dir_out = "output/"
        csv_reader = CSVReader(csv_dir, csv_dir_out) # init CSV reader
        csv_reader.clean_download() # remove downloaded reports before getting new files
        # ---------------------------------------------------------------------------------- #

        # get csv files that have tickers and its values
        # ---------------------------------------------------------------------------------- #
        s0 = 10 # time in seconds --> system time
        page_load_time = 180 # time in seconds to wait for page to load
        wait_time = 1 # Explicit wait time
        driver_time = 60 # implicitly wait time --> driver time 
        # Run firefox for zacks.com
        run_firefox.run_firefox(s0, page_load_time, wait_time, driver_time) # using a url of the iframe
        # ---------------------------------------------------------------------------------- #
        
        # working with csv files
        # ---------------------------------------------------------------------------------- #
        print(f'Building final report for zacks.com tickets.')
        csv_reader.empty_reports("output/all-ascending.csv")  # empty doc
        csv_reader.empty_reports("output/all-descending.csv") # empty doc
        csv_reader.empty_reports("output/all-no-sorting.csv") # empty doc
        csv_reader.empty_reports("output.html") # empty doc
        print(f'Sorting final report: {order}')
        csv_reader.write_csv(order) # arg: ascending, descending, no-sorting; overwrites existing file
        csv_reader.clean_download() # remove downloaded reports
        # load final report into dictionary and this report will not include the header from CSV file
        final_report = csv_reader.read_final_report(output_fn)
        num_of_records = len(final_report)
        print(f'Report is reade.')
        # ---------------------------------------------------------------------------------- #
        
        # Using Selenium WebDriver
        # ---------------------------------------------------------------------------------- #
        s0 = 2 # time in seconds --> system time
        page_load_time = 180 # time in seconds to wait for page to load
        wait_time = 1 # Explicit wait time
        driver_time = 60 # implicitly wait time --> driver time 

        # singlethread: get charts
        # singlethread(final_report, s0, page_load_time, wait_time, driver_time)

        # multithreading: get charts
        # multithreading(final_report, csv_reader, num_of_records, s0, page_load_time, wait_time, driver_time)
        # ---------------------------------------------------------------------------------- #

        # Using BeautifulSoup and urllib3
        # ---------------------------------------------------------------------------------- #
        # singlethread: get charts
        pc = PageCrawler()
        pc.run(final_report)

        # multithreading: get charts

        # ---------------------------------------------------------------------------------- #


    else:
        print("Please, provide one of the sorting names: ascending, descending, no-sorting as an argument.")
    
if __name__ == "__main__":
    main()

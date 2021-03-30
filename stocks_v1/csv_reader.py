import os
import csv

class CSVReader():
    def __init__(self, csv_dir_in, csv_dir_out):
        self.csv_dir_in = csv_dir_in   # directory where temp csv files from zacks.com saved
        self.csv_dir_out = csv_dir_out # directory for the combined csv file
        print(f'Working with CSV files from zacks.com')

    # get all csv files in the download directory
    def get_csv_files(self):
        
        entries = os.listdir(self.csv_dir_in) # get list of csv files
        entries.reverse() # reverse list, so we will start reading that csv file that was saved first

        return entries
    
    # read csv files
    def read_csv(self):
        output = {} # dictionary
        entries = self.get_csv_files() # get all csv files that we have to go thought
 
        file_num = 1 # this one is a file indexer
        line_index = 0 # this is a key for the dictionary
        for e in entries:
            print(f'[{file_num}]: {e}')
            line_count = 1 # used as info in console

            file_path = f'{self.csv_dir_in}{e}'
            with open(file_path, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                # iterate over csv data
                header_index = 0 # if '0' we should add header to dictionary if more then 0 do not add
                for row in csv_reader:
                    if header_index == 0 and file_num == 1:
                        # header
                        # need: Ticker[1], Last Close[4]
                        # print(f'\t{row[1]}, {row[4]}')
                        temp_list = [row[1], row[4]] # create a list for headers
                        output[f'{line_index}'] = [] # init empty list in the dictionary
                        output[f'{line_index}'].append(temp_list) # add headers to the dictionary
                    elif header_index > 0:
                        # data
                        # need: Ticker[1], Last Close[4]
                        # print(f'\t{row[1]}, {row[4]}')
                        temp_list = [row[1], row[4]] # create a list for data
                        output[f'{line_index}'] = [] # init empty list in the dictionary
                        output[f'{line_index}'].append(temp_list) # add data to the dictionary

                    line_count = line_count + 1
                    header_index = header_index + 1
                    line_index = line_index + 1

                file_num = file_num + 1

                print(f'Processed {line_count} lines.')

        return output

    # order: option 1: ascending, option 2: descending
    def sort_csv_output(self, order):

        output = self.read_csv() # dictionary
        sorted_output = {}

        if order == "ascending":
            # Ascending order: the smallest or first or earliest in the order will appear at the top of the list
            # ----------------------------------------------------------------------------------------------- #
            index = 1 # we need this to shift at what index starts the second loop
            for key in output:
                temp_key = key # store initila key
                # we have to ignore the header, so that is why we have 'int(key) > 0'
                if int(key) > 0: 
                    shift_index = 0 # we need this to shift at what index starts the second loop
                    for key2 in output:
                        # we have to ignore the header, so that is why we have 'int(key) > 0'
                        if int(key2) > 0:
                            # we have shift at what index we start to avoid backward element swapping
                            if shift_index >= index:
                                v1 = output[temp_key]
                                v2 = output[key2]
                                lc1 = float(v1[0][1]) # Last Close
                                lc2 = float(v2[0][1]) # Last Close
                                if lc2 < lc1:
                                    temp_key = key2

                            shift_index = shift_index + 1
                
                # we have shift at what index we start to avoid backward element swapping
                index = index + 1

                # swap values
                tmp = output[temp_key]
                output[temp_key] = output[key]
                output[key] = tmp
            # ----------------------------------------------------------------------------------------------- #

        if order == "descending":
            # Descending order: the largest or last in the order will appear at the top of the list:
            # ----------------------------------------------------------------------------------------------- #
            index = 1 # we need this to shift at what index starts the second loop
            for key in output:
                temp_key = key # store initila key
                # we have to ignore the header, so that is why we have 'int(key) > 0'
                if int(key) > 0: 
                    shift_index = 0 # we need this to shift at what index starts the second loop
                    for key2 in output:
                        # we have to ignore the header, so that is why we have 'int(key) > 0'
                        if int(key2) > 0:
                            # we have shift at what index we start to avoid backward element swapping
                            if shift_index >= index:
                                v1 = output[temp_key]
                                v2 = output[key2]
                                lc1 = float(v1[0][1]) # Last Close
                                lc2 = float(v2[0][1]) # Last Close
                                if lc2 > lc1:
                                    temp_key = key2

                            shift_index = shift_index + 1
                
                # we have shift at what index we start to avoid backward element swapping
                index = index + 1

                # swap values
                tmp = output[temp_key]
                output[temp_key] = output[key]
                output[key] = tmp
            # ----------------------------------------------------------------------------------------------- #

            
        return output

    # write csv files, in this case combine two csv files
    # order: option 1: ascending, option 2: descending, option 3: no-sorting
    def write_csv(self, order):
        
        output = {} # dictionary
        file_name = ""
        if order == "ascending":
            output = self.sort_csv_output("ascending")
            file_name = "all-ascending.csv"
        if order == "descending":
            output = self.sort_csv_output("descending")
            file_name = "all-descending.csv"
        if order == "no-sorting":
            output = self.read_csv()
            file_name = "all-no-sorting.csv"
        
        full_path = f'{self.csv_dir_out}{file_name}'
        
        # write to the final report all tickers and its value (price)
        with open(full_path, mode='w', newline='') as dump_file:
            csv_writer = csv.writer(dump_file, delimiter=',')

            for key in output:
                # print(f'key: {key}\n')
                for val in output[key]:
                    tmp = ""
                    index = 1 # counting number of rows to avoid adding extra comma at the end of the row
                    for sv in val:
                        if index < len(val):
                            # add come on the end
                            tmp = tmp + f'{sv},'
                        else:
                            # do not add come on the end
                            tmp = tmp + f'{sv}'
                        index = index + 1
                    # print(f'\tval: {tmp}')

                    csv_writer.writerow(val)

        # no return

    def clean_download(self):
        print("Empty download directory:") 
        entries = self.get_csv_files()

        if len(entries) < 1:
            print("Download directory is empty.") 

        tmp_file_path = ""
        for e in entries:
            file_path = f'{self.csv_dir_in}{e}'
            tmp_file_path = file_path
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"The file {file_path} was removed.") 
            else:
                print(f"No files to remove in {tmp_file_path}") 

    def read_final_report(self, file_name):
        output = {} # dictionary

        file_path = f'{self.csv_dir_out}{file_name}'
        line_index = 0 # this is a key for the dictionary
        with open(file_path, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            # iterate over csv data
            header_index = 0 # if '0' we should add header to dictionary if more then 0 do not add
            for row in csv_reader:
                if header_index > 0:
                    # data
                    temp_list = [row[0], row[1]] # create a list for data
                    output[f'{line_index}'] = [] # init empty list in the dictionary
                    output[f'{line_index}'].append(temp_list) # add data to the dictionary
                    
                    line_index = line_index + 1

                header_index = header_index + 1

        return output

    def slice_csv(self, start, end, records):

        output = {} # dictionary

        # iterate over dictionary of records
        index = start # if '0' we should add header to dictionary if more then 0 do not add
        shift_index = start
        for k in records:
            if shift_index >= start and shift_index <= end:
                ticker = records[k][0][0]
                last_close = records[k][0][1]
                temp_list = [ticker, last_close] #  # create a list for data
                output[f'{index}'] = [] # init empty list in the dictionary
                output[f'{index}'].append(temp_list) # add data to the dictionary

                if shift_index == end:
                    break
                    
                index = index + 1

            shift_index = shift_index + 1

        return output

    def empty_reports(self, file_path):
        open(file_path, 'w').close()
        # file = open(file_path,"r+")
        # file.truncate(0)
        # file.close()
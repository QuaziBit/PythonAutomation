def write_fragmens(filename, data):

    # this statement automatically acquires the lock before entering the block, 
    # and releases it when leaving the block
    with lock:
        html_object = open(filename, "a")
        html_object.truncate(0) # errace old content
        html_object.write(data) # write new content 
        html_object.close()     # close IO stream
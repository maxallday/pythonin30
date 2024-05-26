#🐍 Day 15: Make Your Mark: Writing to Files 🐍code 
#Basic File Writing You can use the write() method to write data into a file. Let’s see how to do this with a context manager:
'''with open("writofile.txt", "w") as file: #w is for write ,overites existing data on file
    #file.write("Hello programmer")   
with open("writofile.txt", "a") as file: #a is for append, adds new data to the end of the file
    file.write("\nHello Python programmer")

#Task 1: Personal Diary: Create a text file and write a short diary entry into it.    
with open("diary.txt", "a") as file:
     #file.write("Today I learned how to write to a file")
    write = input("\nEnter your diary entry: ")
    file.write(write)
'''    
# Taask2:Data Logger: Write a function that logs the current date and time into a text file every time it's run.
import datetime
def log_date_time():
    #get current date
    now = datetime.datetime.now()
    #format date & time
    date_time_str = now.strftime("%d/%m/%Y %H:%M:%S")
    #write date & time to file
    with open("diary.txt", "a") as file:
        file.write(date_time_str + "\n")
    print(f"Date and time exactly stopped coding for the day was:{date_time_str} ")    

log_date_time()    
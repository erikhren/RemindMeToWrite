# Every time at a certain time it will open a window; then it will check if you put it in and remind you
 
# packages
from os.path import exists
import datetime
import pandas as pd
 
# path to file
path_to_file = "C:\\Users\\DM5025\\Desktop\\checking-with-myself.csv"
 
# innitiate the input box
accept = "n"
while accept == "n":
    print("Hello champ, good to see you. What's on your mind today?")
    log_string = str(input())
    print("Enter: n to cancel the entry and write again; to accept press any other key.")
    accept = str(input()) # accept entry or try again
 
# get todays date
today = datetime.datetime.today().strftime("%Y-%m-%d %HH:%MM")
 
# create a Dataframe, convert it to string
df = pd.DataFrame({"date":today, "Log":log_string}, index=[0])
 
# check if file exits; open it; else create it
if exists(path_to_file):
    old = pd.read_csv(path_to_file,index_col=0)
    df = old.append(df).reset_index(drop=True)
    df.to_csv(path_to_file)
else:
    df.to_csv(path_to_file)
 
## Find python path for .bat file
#import sys
#print(sys.path)
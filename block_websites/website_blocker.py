import time
from datetime import datetime as dt

#hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
hosts_path=r"D:\Dropbox\python\CU\python-tutorials\block_websites\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.elmundo.es"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect +" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            # After reading all the lines, let's go back to the beginning
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            # After writting the new content at the beginning of the file, truncate the rest of the file
            file.truncate()
        print("Fun hours...")
    time.sleep(5)

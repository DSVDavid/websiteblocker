import time
from datetime import datetime as dt
#hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
web_list=["www.pornhub.com","www.redtube.com","www.xhamster.com", "www.xvideos.com"]

while True:
    print(1)
    if 16 < dt.today().hour and dt.today().hour <20:
        print("NO FUN")
        with open(hosts_path,'r+') as file:
                content=file.read()
                for site in web_list:
                    if site in content:
                        pass
                    else:
                        file.write(redirect+" "+site+"\n")
    else:
        print("HAVE FUN")
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in web_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)

import time
from datetime import datetime as dt
hosts_path = 'C:\Windows\System32\drivers\etc\hosts' # needs to be opened with administrative privileges
redirect = '127.0.0.1' # where to redirect the website
website = ['www.facebook.com','facebook.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,21):
        print('Working hours!')
        with open(hosts_path,'r+') as file:
            content = file.read()
            print(content)
            for web in website:
                if web in content:
                    pass
                else:
                    file.write('\n')
                    file.write(redirect+' '+web)
                    
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines() #list of strings with all the lines
            file.seek(0)
            for line in content:
                if not any(web in line for web in website):
                    file.write(line)
            file.truncate() # deletes everything below the written file.
        print('Time to play!')
        
    time.sleep(10) # to repeat the while loop every 10 seconds.
#needs to be saved as a script, to run in the background

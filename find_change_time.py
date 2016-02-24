from fetch import fetch
import time

oldpassword = ''

while True:
    (server, server_port, password, method) = fetch()
    if (oldpassword != password):
        strTime = time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time()))
        print(strTime + ' Password changed to:' + password);
    oldpassword = password
    time.sleep(60)
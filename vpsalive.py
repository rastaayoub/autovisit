import requests
import time
i=1
while i<5:
 r=requests.get('https://shakeelvps.herokuapp.com/vnc.html')
 print(r.status_code)
 time.sleep(20)

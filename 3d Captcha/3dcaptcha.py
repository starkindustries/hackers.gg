import subprocess
import requests
import time

def list_rand():
    for i in range(0,100):
        # command = 'php -r \'$rnd = mt_rand(1, 1); srand(time()); $rnd &= rand(); echo $rnd;\''
        command = 'php -r \'mt_srand(1000); $rnd = mt_rand(); echo $rnd;\''
        command2 = "php -r '$c = chr(mt_rand(33,126)).chr(mt_rand(33,126)).chr(mt_rand(33,126)).chr(mt_rand(33,126)).chr(mt_rand(33,126)); echo $c;'"
        cmd_output = subprocess.check_output(command2, shell=True)
        print(cmd_output)
        i += 1

url = "http://hackers.gg:6656/"
image_url = url + "index.php?image"
session = "772fc20711e3813e50977deef3fef38a"
cookies = {}
cookies["PHPSESSID"] = "772fc20711e3813e50977deef3fef38a"

def solve():
    # print(page.text)
    startTime = time.time()
    page = requests.get(url, cookies = cookies)
    page = requests.get(image_url, cookies = cookies)
    page = requests.post(url, data = {"captcha":"EV?#i"}, cookies = cookies)
    stopTime = time.time()
    diff = stopTime - startTime
    print("=======================")
    print("TIME: " + str(diff))
    #print(page.text)
    #print("LENGTH")
    print(len(page.text))
    if len(page.text) < 280:
      print(page.text)
    # print("COOKIES")
    # print(page.cookies)

#page = requests.post(url, cookies = cookies)
while True:
    solve()
    "EV?#i"
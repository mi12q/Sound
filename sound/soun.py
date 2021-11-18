import requests as rq
response = rq.get('http://192.168.212.35/Image.png')
file = open('ar2co2.png',"wb")
file.write(response.content)
file.close()

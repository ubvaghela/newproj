from win32com.client import Dispatch
import json, requests
import time
from datetime import datetime
API_Key = '00f8d98a0d1d4b99ae68df4d3040e808'

def home(k):
	if k==1:
		print(f"Hello Sir, Welcome on News Reader, Today is {time.strftime('%A, %d %B %Y ')}, Please, Select News Channel for listen news")
		readnews(f"Hello Sir, Welcome on News Reader, Today is {time.strftime('%A, %d %B %Y ')}, Please, Select News Channel for listen news")
		medialist()
		home(2)
	else:
		medialist()

def medialist():
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=00f8d98a0d1d4b99ae68df4d3040e808'
    data = requests.get(url).text
    json_py = json.loads(data)
    #print(time.asctime(time.localtime()))
    for index,item in enumerate(json_py['articles'],1):
    	#if item['source']['id'] != None:
    	print(index,item['source']['name'])
    no=int(input('Select News Media For Listion : '))
    return selectnewsmedia(json_py['articles'][no-1]['source']['name'],json_py['articles'][no-1]['source']['id'])

def selectnewsmedia(name,medianame):
	if medianame is not None:
		newurl = f'https://newsapi.org/v2/top-headlines?sources={medianame}&apiKey={API_Key}'
	else:
		newurl = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_Key}'
	data2 = requests.get(newurl).text
	newspaper = json.loads(data2)
	readnews(f"Today's News From {name}")
	for index,item in enumerate(newspaper['articles'],1):
		readnews(index)
		print(index, item['title'])
		readnews(item['title'])
	readnews('Thanks, If You Want listening More New From another Media, Please Select New Channel')
	medialist()

def readnews(news):
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(news)

if __name__ == "__main__":
	home(1)
    
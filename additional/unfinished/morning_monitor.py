from tkinter import *
import requests
from bs4 import BeautifulSoup 
from weather import Weather
from datetime import datetime
import calendar
import webbrowser
import time
from PIL import Image
# from PIL import ImageTK

root = Tk()
# root.geometry("1250x1250")
root.title('Daily View')
root.configure(bg = 'white')

# Pull in the weather data
weather = Weather()
location = weather.lookup_by_location('metuchen, nj')
condition = location.condition()
forecasts = location.forecast()
astronomy = location.astronomy()

dt_format='%d%m%Y'

weather_bg = 'white'

####### PULL IN WEATHER DATA ########

# Show the location
weather_root = Frame(root, bg = 'orange').grid(row = 0, column = 0,sticky = W)

# Read in the temperature
weather_start_row = 0
Label(weather_root, text = condition['temp'] + '° ' +condition['text'], fg = 'cornflowerblue', bg = weather_bg, font = ('Calibri',17,'bold')).grid(row=weather_start_row,column = 0)
Label(weather_root, text = location.title().replace('Yahoo! Weather - ',''), fg = 'cornflowerblue', bg = weather_bg, font = ('Calibri',12)).grid(row=weather_start_row+2,column = 0)
Label(weather_root, text = forecasts[0].high() + ' / ' + forecasts[0].low(), fg = 'slategrey', bg = weather_bg, font = ('Calibri',12, 'bold')).grid(row=weather_start_row+3,column = 0)
Label(weather_root, text = 'Sunrise: ' + astronomy.get('sunrise'), fg = 'slategrey', bg = weather_bg, font = ('Calibri',8)).grid(row=weather_start_row+4,column = 0)
Label(weather_root, text = 'Sunset: ' + astronomy.get('sunset'), fg = 'slategrey', bg = weather_bg, font = ('Calibri',8)).grid(row=weather_start_row+5,column = 0)



# file_in = 'C:\\Users\\peterru\\Desktop\\weather\\sunny.png'
# pil_image = Image.open(file_in)
# image200x100 = pil_image.resize((10, 10), Image.ANTIALIAS)
# file_out = 'Roses200x100.jpg'
# image200x100.save(file_out)
# curr_weather = ImageTK.PhotoImage(PhotoImage(image200x100))
# curr_weather = curr_weather.subsample(2, 2)
# label = Label(root, image=curr_weather, borderwidth = 0, highlightthickness=0)
# label.image = curr_weather
# label.grid(row = weather_start_row+1, column = 0)



forecast_root = Frame(root, bg = 'blue').grid(row = 0, column =1,sticky = W)
j = 0 
for forecast in forecasts[1:6]:

	Label(forecast_root, text = 'Image Placehold',
		fg = 'slategrey', bg = weather_bg, font = ('Calibri',8), anchor = W).grid(row=2,column = 1+j, rowspan = 2, sticky = W)

	date_given = forecast.date()
	weekday_from_date = calendar.day_name[datetime.strptime(date_given,'%d %b %Y').weekday()][:3]

	Label(forecast_root, text = weekday_from_date,
		fg = 'slategrey', bg = weather_bg, font = ('Calibri',8)).grid(row=3,column = 1+j)

	Label(forecast_root, text = forecast.low() + '  /  ' + forecast.high(),
		fg = 'slategrey', bg = weather_bg, font = ('Calibri',8)).grid(row=4,column = 1+j)

	j += 1 


# # SHOW THE TIME

now = datetime.now()

time_root = Frame(root, bg = 'blue').grid(row = 0, column = 7,sticky = NE)
Label(time_root, text = now.strftime('%I:%M:%S'), fg = 'slategrey', bg = 'white', font = ('Calibri',12,'bold')).grid(row=0,column = 7, sticky = S)
Label(time_root, text = now.strftime('%B %d,%Y'), fg = 'slategrey', bg = 'white', font = ('Calibri',8)).grid(row=1,column = 7,rowspan = 4, sticky = N)

# #####################################

quote_root = Frame(root, bg = 'blue').grid(row = 7, column = 0, columnspan = 8)
url = 'http://feeds.feedburner.com/brainyquote/QUOTEBR'
response = requests.get(url)
soup = BeautifulSoup(response.content, features = 'xml')
items = soup.findAll('item')
for item in items: 
		Label(quote_root, text = items[0].description.text + '  -' +items[0].title.text , fg = 'grey', bg = 'white', font = ('Calibri',11,'italic')).grid(row=8, column = 0, columnspan =8)

#######################################

# # FILL IN THE TOP STORIES

section_start = 9 

news_root = Frame(quote_root, bg = 'green').grid(row = section_start, column = 0, columnspan = 5, rowspan = 20, sticky = W)

# url = 'http://feeds.bbci.co.uk/news/rss.xml'
# url = 'https://www.reddit.com/r/news/.rss'
url = 'http://www.bloomberg.com/politics/feeds/site.xml'

response = requests.get(url)
soup = BeautifulSoup(response.content, features = 'xml')

items = soup.findAll('item')
Label(news_root, text = 'World News', fg = 'navy', bg = 'white', font = ('Calibri',15,'bold')).grid(row=section_start,column = 0, columnspan = 4, sticky = 'W')

i = section_start + 1
for item in items[:5]: 
	i +=2
	Label(news_root, text = item.title.text, fg = 'steelblue', bg = 'white', font = ('Calibri',10)).grid(columnspan = 4, rowspan =4, sticky = 'W')
	Label(news_root, text = item.description.text, fg = 'dimgray', bg = 'white', font = ('Calibri',8), wraplength = 500,  justify = LEFT).grid(rowspan =4, columnspan = 4, sticky = W)


# # #####################################

# # # FILL IN THE SPORTS 

# # #####################################

# url = 'http://www.espn.com/espn/rss/news'
url = 'http://nypost.com/sports/feed/'

sport_root = Frame(news_root, bg = 'green').grid(column = 0, columnspan = 4,sticky = W)

response = requests.get(url)
soup = BeautifulSoup(response.content, features = 'xml')

items = soup.findAll('item')
Label(news_root, text = 'Sports News', fg = 'navy', bg = 'white', font = ('Calibri',15,'bold')).grid(column = 0, columnspan = 4, sticky = 'W')

i = section_start + 1
for item in items[:5]: 
	i +=2
	Label(sport_root, text = item.title.text, fg = 'steelblue', bg = 'white', font = ('Calibri',10)).grid(column = 0, columnspan = 4, sticky = 'W')
	Label(sport_root, text = item.description.text, fg = 'dimgray', bg = 'white', font = ('Calibri',8), wraplength = 500, justify = LEFT).grid(column = 0, rowspan = 4, columnspan = 4, sticky = 'W')

# # #######################################

url = 'https://www.scorespro.com/rss2/live-basketball.xml'

scores_root = Frame(root, bg = 'green',  borderwidth = 100).grid(row = 0, column = 1, rowspan = 50)

response = requests.get(url)
soup = BeautifulSoup(response.content, features = 'xml')

Label(scores_root, text = 'Live NBA Scores', fg = 'navy', bg = 'white', font = ('Calibri',15,'bold')).grid(row = 9, column = 4,  columnspan = 3, rowspan =10)

items = soup.findAll('item')

i = 10 #section start + 1
for item in items: 
	if ('USA-NBA') in item.title.text:
		x = item.title.text.replace('#Basketball #Livescore @ScoresPro: (USA-NBA) #','').replace('#', '')
		Label(scores_root, text = x, fg = 'grey', bg = 'white', font = ('Calibri',8)).grid(row = section_start+i+2, column = 4, columnspan = 3,  rowspan =10, sticky = EW)
		i += 1

# if i == section_start:
# 	Label(scores_root, text = 'No live NBA games currently', fg = 'darkgray', bg = 'white', font = ('Calibri',10,'italic')).grid(row = section_start + 1, column = 0, columnspan = 3, sticky = E)
# # ###########################################

# url = 'https://www.scorespro.com/rss2/live-football.xml'

# football_root = Frame(root, bg = 'green').grid(row = section_start + i + 2, column = 0, columnspan = 4,sticky = W)

# response = requests.get(url)
# soup = BeautifulSoup(response.content, features = 'xml')

# Label(football_root, text = 'Live Football Scores', fg = 'navy', bg = 'white', font = ('Calibri',15,'bold')).grid(row=section_start + i + 2,column = 0, sticky = 'W')

# items = soup.findAll('item')

# section_start = section_start + i + 2

# i = section_start
# for item in items: 
# 	if (('USA-FBS') or ('USA-NFL') in item.title.text) and (item.description.text != 'Match Finished'):

# 		if ('USA-FBS') in item.title.text:
# 			x = item.title.text.replace('American Football #Livescore @ScoresPro: (USA-FBS) #','').replace('#', '')

# 		elif ('USA-NFL') in item.title.text:
# 			x = item.title.text.replace('American Football #Livescore @ScoresPro: (USA-NFL) #','').replace('#', '')
			
# 		Label(football_root, text = x, fg = 'black', bg = 'white', font = ('Calibri',10)).grid(row = i+2, column = 0, sticky = 'W')
# 		i += 1 

# if i == section_start: 
# 	Label(football_root, text = 'No live football games currently', fg = 'darkgray', bg = 'white', font = ('Calibri',10,'italic')).grid(row = section_start+1, column = 0, sticky = 'W')

# # ###########################################
# # Label(time_root, text = 'Test', fg = 'darkgray', bg = 'white', font = ('Calibri',10,'italic')).grid(row = 0, column = 1, sticky = 'W')
root.mainloop()

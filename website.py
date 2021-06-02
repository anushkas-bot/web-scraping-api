from flask import Flask, render_template, jsonify, make_response
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)

with open('example.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#print(soup.prettify())

#match = soup.h3
#match2 = soup.h3.text
match3 = soup.find('div', class_='post-grid col-lg-12 col-md-12 col-sm-12 col-xs-12 post-21084 post type-post status-publish format-standard has-post-thumbnail hentry category-mundane-astrology')
#print(match3.text + "\n")
match4 = soup.find('img', class_='attachment-thumbnail size-thumbnail wp-post-image')['src']
#print(match4 + "\n")
match5 = soup.find('div', class_='post-excerpt clearfix')
#print(match5.text + "\n")
match6 = soup.find('article', class_='post-21084 post type-post status-publish format-standard has-post-thumbnail hentry category-mundane-astrology')['id']
#print (match6 + "\n")
match7 = "(1) Title:" + match3.text + " Img:" + match4 + " Content:" + match5.text + " Id:" + match6
match8 = soup.find('div', class_='wpcf7')['id']
#print(match8)
match9 = soup.find('div', class_='wpb_wrapper')
match10 = match9.h2.text
#print(match10)
match11= soup.find('input', class_='wpcf7-form-control wpcf7-text wpcf7-validates-as-required')['placeholder']
#print(match11)
match12= soup.find('input', class_='wpcf7-form-control wpcf7-text wpcf7-email wpcf7-validates-as-required wpcf7-validates-as-email')['placeholder']
#print(match12)
match13= soup.find('input', class_='wpcf7-form-control wpcf7-number wpcf7-validates-as-number')['placeholder']
#print(match13)
match14= soup.find('select', class_='wpcf7-form-control wpcf7-select wpcf7-validates-as-required')
#print(match14.text.split())
match15= soup.find('input', class_='wpcf7-form-control wpcf7-date wpcf7-validates-as-required')['placeholder']
#print(match15)
match16= soup.find('span', class_='wpcf7-form-control-wrap BirthPlace')
#print(match16.input['placeholder'])
match17= soup.find('span', class_='wpcf7-form-control-wrap BirthHour')
#print(match17.input['placeholder'])
match18= soup.find('span', class_='wpcf7-form-control-wrap BirthMinute')
#print(match18.input['placeholder'])
match19= soup.find('span', class_='wpcf7-form-control-wrap BirthSecond')
#print(match19.input['placeholder'])
match20= soup.find('span', class_='wpcf7-form-control-wrap textarea-542')
#print(match20.textarea['placeholder'])
match21= soup.find('span', class_='cf7ic_instructions')
#print(match21.text)
match22= soup.find('ul', class_='social-link')
#print(match22.li.a['href'])
match23= soup.find('a', href='https://www.facebook.com/astrokapoorcom/')
#print(match23['href'])
match24= soup.find('a', href='https://twitter.com/@Astrokapoor')
#print(match24['href'])
match25= soup.find('a', href='https://plus.google.com/+ParshantKapoor')
#print(match25['href'])
match26= soup.find('a', href='http://in.linkedin.com/in/astrokapoor')
#print(match26['href'])
match27 = "Id: " + match8 + "; Title: " + match10 + "; Content: " + match11 + ', ' + match12 + ', ' + match13 + ', ' + match14.text + ', ' + match15 + ', ' + match16.input['placeholder'] + ', ' + match17.input['placeholder'] + ', ' + match18.input['placeholder'] + ', ' + match19.input['placeholder'] + ', ' + match20.textarea['placeholder'] + ', ' + match21.text + '; ' + 'Social media links: ' + match22.li.a['href'] + ', ' + match23['href'] + ', ' + match24['href'] + ', ' + match25['href'] + ', ' + match26['href']
#print(match27)
match28 = soup.find('aside', id='recent-comments-2')
#print(match28.text)
match29 = soup.find('aside', id='bwp_woo_recent_post_widget-1')
#print(match29.text)
match30 = soup.find('aside', id='displaycategorieswidget-2')
#print(match30.text)
match31 = soup.find('aside', id='archives-2')
#print(match31.text)
match32 = match28.text + "; " + match29.text + "; " + match30.text + '; ' + match31.text
match33 = soup.find('input', class_='s')['value']
#print(match33)
match34 = "Search value: " + match33
match35 = soup.find('a', href='https://astrokapoor.com/sharad-pawar-horoscope/')['href']
#print(match35)
#match36 = soup.find('div', id='recent_post_14877450391622462866')['id']
#print(match36)
match36 = soup.find('img', src='https://astrokapoor.com/wp-content/uploads/2021/04/Sharad-Pawar-political-career-to-endHealth-analysis-Prashant-Kapoor-150x150.jpg')['alt']
#print(match36)
match37 = soup.find('img', src='https://astrokapoor.com/wp-content/uploads/2021/04/Sharad-Pawar-political-career-to-endHealth-analysis-Prashant-Kapoor-150x150.jpg')['src']
#print(match37)
match39 = soup.find('img', src='https://astrokapoor.com/wp-content/uploads/2021/04/World-to-witness-chain-of-Earthquakes-after-4-April-2021-astrological-analysis-by-Prashant-Kapoor-150x150.jpg')['src']
#print(match39)
match40 = soup.find('img', src='https://astrokapoor.com/wp-content/uploads/2021/04/World-to-witness-chain-of-Earthquakes-after-4-April-2021-astrological-analysis-by-Prashant-Kapoor-150x150.jpg')['alt']
#print(match40)
match38= match7 + '  (2) Id: ' + match6 + '; Title: ' + match36 + '; Img: ' + match37 + '; Content: ' + '  (3) Id: ' + match6 + '; Title: ' + match40 + '; Img: ' + match39 + '; Content: '

@app.route("/api1")
def hello():
    return json.dumps(match38)

@app.route("/api2")
def hello2():
    return json.dumps(match27)

@app.route("/api3")
def hello3():
    return json.dumps(match32)

@app.route("/api4")
def hello4():
    return json.dumps(match34)

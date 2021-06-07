import json
from selenium import webdriver
from flask import request,jsonify,Flask

driver = webdriver.Firefox(executable_path='C:/Users/Bi/geckodriver.exe')
driver.get("https://vietnamnet.vn/vn/suc-khoe/tin-tuc-covid-19-sang-hom-nay-7-6-viet-nam-ghi-nhan-them-44-ca-covid-19-trong-nuoc-hon-5-300-benh-nhan-dang-dieu-tri-743428.html")

heading = driver.find_element_by_tag_name('h1')
content = driver.find_elements_by_xpath('//p')
img = driver.find_elements_by_xpath('//img')
date = driver.find_element_by_class_name('ArticleDate')

imgs=[]
contents=[]
for i in content:
    contents.append(i.text)
for i in img:
    imgs.append(i.get_attribute('src'))

app= Flask(__name__)
@app.route('/get_news')
def get_news():
    data = []
    data.append({
        'title':heading.text,
        'content':contents,
        'date':date.text,
        'image':imgs
    })
    return jsonify({'news':data})

if __name__=='__main__':
    app.run(port='8000',debug=True)


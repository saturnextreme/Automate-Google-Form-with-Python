from selenium import webdriver
import indian_names
import time
import random

l1 = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span']
l2 = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span']
l3 = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span']
l4 = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span']
l5 = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label/div[2]/div[2]/div/span', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]/label/div[2]/div[2]/div/span', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[3]/label/div[2]/div[2]/div/span']
l6 = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span']
l7 = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span']
l8 = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[2]/div/span','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[6]/label/div/div[2]/div/span']
l9 = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span']


for i in range(1):
    web = webdriver.Chrome()
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSddZWj2U2JZDs23ADg7-RrIknyVRxXH-gj2x7Oraske1YXR4Q/viewform')
    time.sleep(2)
    year = str(random.randrange(1960,2007))
    name = indian_names.get_full_name()
    name = random.choice([name+year,name])
    name += "@gmail.com"
    name = name.replace(" ", "")
    name = name.lower()
    femail = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
    femail.send_keys(name)
    fs1 = web.find_element('xpath', random.choice(l1))
    fs1.click()
    fs2 = web.find_element('xpath', random.choice(l2))
    fs2.click()
    fs3 = web.find_element('xpath', random.choice(l3))
    fs3.click()
    fs4 = web.find_element('xpath', random.choice(l4))
    fs4.click()
    fs5 = web.find_element('xpath', random.choice(l5))
    fs5.click()
    l = [False for j in range(4)]
    for j in range(random.randrange(1, 5)):
        y = random.randrange(1, 5)
        if l[y - 1] == False:
            fs6 = web.find_element('xpath', l6[y - 1])
            fs6.click()
            l[y - 1] = True
    fs7 = web.find_element('xpath',random.choice(l7))
    fs7.click()
    fs8 = web.find_element('xpath',random.choice(l8))
    fs8.click()
    fs9 = web.find_element('xpath',random.choice(l9))
    fs9.click()
    fregion = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fregion.send_keys(random.choice(['india', 'India', 'INDIA']))
    fsubmit = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    time.sleep(10)
    fsubmit.click()





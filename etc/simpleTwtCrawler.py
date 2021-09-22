import time
import csv
from selenium import webdriver

# make list of target twt names
list = []
with open(targetFile,'r') as raw:
    reader = csv.reader(raw)
    for lines in reader:
        list.append(lines[0])

for name in list:
    f = open(recordFile, 'a', encoding = 'utf-8-sig', newline="")
    wr = csv.writer(f)

    if name == "":
        wr.writerow(["","","",""])

    else:
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("headless")
            chromedriver = 'C:\ChromeDriver2\chromedriver.exe'
            driver = webdriver.Chrome(chromedriver)
            driver.get('https://twitter.com/'+name)

            tweets = driver.find_elements_by_class_name("r-qvutc0")
            tweets_count = tweets[23].text[:-2]

            num = driver.find_elements_by_class_name("r-b88u0q")
            followers = num[11].find_element_by_tag_name("span").text

            times = driver.find_elements_by_class_name("css-1dbjc4n")
            time.sleep(3)
            t = times[38].find_elements_by_tag_name("time")
            recent = t[0].text

            wr.writerow([name, tweets_count, followers, recent])
            driver.quit()
        except IndexError:
            wr.writerow([name,"error"])
            driver.quit()
    
    f.close()

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from download import *

driver = webdriver.Chrome()

def scrape_channel(url):
	driver.get(url)

	user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
	links = []
	for i in user_data:
		print(i.get_attribute('href'))
		links.append(i.get_attribute('href'))

	df = pd.DataFrame(columns = ['link', 'title', 'description', 'category'])

	wait = WebDriverWait(driver, 10)
	v_category = "CATEGORY_NAME"
	for x in links:
		    driver.get(x)
		    v_id = x.strip('https://www.youtube.com/watch?v=')
		    v_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
		    v_description =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#description yt-formatted-string"))).text
		    df.loc[len(df)] = [x, v_title, v_description, v_category]

	return df

def main():
	#df = scrape_channel('https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw/videos')
	df = pd.read_csv('test.csv')
	download(df)

if __name__ == '__main__':
	main()

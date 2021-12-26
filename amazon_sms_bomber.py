from selenium import webdriver
import time
options=webdriver.ChromeOptions()
options.headless=True
for i in range(1):
	driver=webdriver.Chrome(executable_path="D:\\installed software\\chromedriver.exe")
	driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
	driver.find_element_by_xpath("//input[@name='email']").send_keys("1234567890")
	driver.find_element_by_xpath("//input[@id='continue']").submit()
	driver.find_element_by_xpath("//a[@id='auth-fpp-link-bottom']").click()
	driver.find_element_by_xpath("//input[@id='continue']").submit()
	time.sleep(4)
	driver.close()
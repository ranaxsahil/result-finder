from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

f = open("this.txt", "w")
driver = webdriver.Edge()

for i in range(124):
    driver.get("http://results.nith.ac.in/scheme23/studentresult/index.asp")
    if i < 9: 
        rollnumber = "23bme" + 2*str(0) + str(i+1)
    elif i == 19 or i == 48 or i ==57 or i == 80 or i ==51 or i == 34 :
        continue 
    elif i < 99:
        rollnumber = "23bme" + 1*str(0) + str(i+1)
    else:
        rollnumber = "23bme" + str(i+1) 
    driver.find_element(By.NAME, "RollNumber").send_keys(rollnumber)
    driver.find_element(By.NAME, "B1").send_keys(Keys.ENTER)
    number = driver.find_element(By.XPATH, "//*[@id='page-wrap']/table[4]/tbody/tr/td[4]/p[2]")
    number_text = number.text
    a = 0
    for element in range(0, len(number_text)):
        
        if a == 1:
            f.write(number_text[element])
            print(number_text[element])
        if number_text[element] == "=":
            a = 1
        else:
            continue
    f.write("   " + rollnumber)
    f.write("\n")
    a = 0
    print(rollnumber)
f.close()
driver.close()
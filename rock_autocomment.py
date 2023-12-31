from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
import pandas as pd

# 1.  Declare browser variable
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

# 2. Open a website
driver.get("https://discord.com/login");

sleep(5);

# 3. Fill in information and password
user = driver.find_element(By.NAME, "email")
user.send_keys("");

password = driver.find_element(By.NAME, "password")
password.send_keys("");

# 4. Login
login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]')
login_button.click();
sleep(5);

# 5. Go to main page
driver.get("https://discord.com/channels/1190385741247811624/1190385756104036514");
sleep(5);

# 6. Auto comment for 20 times
i = 0;
while i < 10000:  
  comments = driver.find_elements(By.CLASS_NAME, 'messageContent__21e69')
  comment = "Level 5 soon!"
  if len(comments) > 0:
    comment = random.choice(comments).text
    while comment.startswith("A new rock") or len(comment) > 20 :
        sleep(1)
        comment = random.choice(comments).text
  sleep(1)
  driver.find_element(By.TAG_NAME, "body").send_keys(comment);
  sleep(1);
  actions = ActionChains(driver);
  actions.send_keys(Keys.ENTER);
  actions.perform();
  i = i + 1;
  sleep(38)

# 7. Close page
sleep(10);
driver.close();

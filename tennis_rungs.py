import logging
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from os import environ

def challenge_player():
        try:
            driver = webdriver.PhantomJS()
            driver.get('http://app.tennisrungs.com/Account/Login')
            tr_username = str(environ.get('USERNAME',None))
            tr_password = str(environ.get('PASS',None))
            num_hits = int(environ.get('NUM_HITS',17))
            sec_interval = int(environ.get('SEC_INTERVAL',30))
            ids=str(environ.get('ID_COMMA_LIST',None))
            names = str(environ.get('NAME_LIST',None))
            id_array = ids.split(',')
            name_array = names.split(',')
            driver.find_element_by_id("UserName").send_keys(tr_username)
            driver.find_element_by_id("Password").send_keys(tr_password)
            driver.find_element_by_css_selector(".btn[value='Login']").click()
            time.sleep(5)
            driver.get("http://app.tennisrungs.com/Ladders/Rankings/32383352")  
            driver.execute_script("window.confirm = function() { return true; }");
            time.sleep(5)
        except Exception as e:
            print("Bot Setup Error: " + str(e))
            driver.close()
            return  

        for x in range(num_hits):
            currentTime = datetime.datetime.now() - datetime.timedelta(hours=4)
            currentTime = currentTime.strftime("%m-%d %I:%M %p")
            for id_num in range(len(id_array)):
                try: 
                    player_id = str(id_array[id_num])
                    player_name=name_array[id_num]
                    driver.find_element_by_css_selector('.btn-green[onclick*="' + player_id + '"]').click()
                except Exception as e:
                    print(currentTime + " " + str(x+1) + "/17 Challenge Fail: " + player_name + " (" + player_id + ")")
            driver.refresh()
            driver.execute_script("window.confirm = function() { return true; }");
            time.sleep(sec_interval)

        driver.close()
        return

challenge_player()


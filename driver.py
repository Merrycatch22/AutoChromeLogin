from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

if __name__ == '__main__':

    #at the moment, assumes the same credentials for discord and youtube.
    file = open(".creds","r")
    creds=file.read().splitlines()

    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_extension('uBlock-Origin_v1.20.0.crx')
    try:
        browser = webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)
        browser.set_window_position(0,0)
        browser.set_window_size(1360,730)
        browser.maximize_window()
        
        browser.get('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3D%252F&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        assert 'YouTube' in browser.title
        youtubeUser = browser.find_element_by_xpath('//*[@id="identifierId"]')
        youtubeUser.send_keys(creds[0]+'\n')
        
        youtubePass = WebDriverWait(browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input'))
        youtubePass.send_keys(creds[1]+'\n')

        youtubeLoginSucc = WebDriverWait(browser, 10).until(lambda x: x.find_element_by_xpath('//*[@id="search"]'))
        
        browser.get('http://discordapp.com/login')
        assert 'Discord' in browser.title

        discordUser = browser.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[1]/div/input')
        discordUser.send_keys(creds[0])

        discordPass = browser.find_element_by_xpath('//*[@id="app-mount"]/div[1]/div/div[2]/div/form/div/div[3]/div[2]/div/input')
        discordPass.send_keys(creds[1]+'\n')
    except:
        browser.quit()
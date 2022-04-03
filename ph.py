from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()

class webrequest:
  accs = []
  password = 'brainDamage1234!@#'
  
  def __init__(self, url, proxy, nick_suffix):
    self.url = url
    self.proxy = proxy
    self.nick_suffix = nick_suffix
  
  def get_accs(self):
    with open('accs.txt', "r+") as f:
      self.accs = f.readlines()
      
      
  def auto_cfg(self):
    if (len(self.proxy) > 0):
      chrome_options.add_argument(f'proxy-server={self.proxy}')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
      
  def send_request(self):
    driver = webdriver.Chrome(options=chrome_options)     
                                                
    driver.get(self.url)
    for _ in self.accs:
      if(len(_.split('\n')) > 0):
        driver.find_element_by_name('email').send_keys(_.split('\n')[0])
        driver.find_element_by_name('username').send_keys(_.split('\n')[0][:3] + self.nick_suffix)
      driver.find_element_by_name('password').send_keys(self.password)
      time.sleep(5)
      driver.find_element_by_css_selector('input[type=\"submit\" i]').click() 
      time.sleep(25)
      driver.quit()
      driver.get(self.url)
      
def main():
  ph = webrequest('https://pl.pornhub.com/signup', '', 'cumil1337');
  ph.get_accs()
  ph.auto_cfg()
  ph.send_request()

  
if __name__ == "__main__":
  main()
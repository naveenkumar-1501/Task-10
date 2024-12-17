from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Insta:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        """The Automation Start Method"""

    def start(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(2)
            return True
        except Exception as error:
            print("ERROR : Unable to start the Python Selenium Automation !", error)
            return False

    """Fetch the followers and following"""

    def fetch_followers_following(self):
        try:
            sleep(5)
            # Locate followers count
            followers_element = self.driver.find_element(By.XPATH,"//li[2]//span[@title or text()]")
            followers = followers_element.get_attribute("title") or followers_element.text # Fetch either title or text

            # Locate following count
            following_element = self.driver.find_element(By.XPATH, "//li[3]//span")
            following = following_element.text  # Fetch the text for following count

            return followers, following
        except Exception as error:
            print(f"An error occurred:", error)
            return None, None

    """The Shutdown Method"""
    def shutdown(self):
        self.driver.quit()

# Main Execution Program

if __name__ == "__main__":
    url = "https://www.instagram.com/guviofficial/"

    naveen = Insta(url)
    if naveen.start():
        sleep(10)
        followers, following = naveen.fetch_followers_following()

        if followers and following:
            #Print extracted data
            print("Followers:", followers)
            print("Following:", following)
        else:
            print("Failed to fetch data.")

        naveen.shutdown()

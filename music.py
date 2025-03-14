from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class YoutubeSearch:
    def __init__(self, query):
        # Set up Chrome WebDriver with options
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # ✅ Keeps browser open

        service = Service(r"C:\Users\anand\Downloads\chromedriver-win64 2\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open Yahoo Search
        self.driver.get(f"https://www.youtube.com/results?search_query={query}")  # ✅ Fixed Syntax
        result=self.driver.find_element(By.XPATH, '//*[@id="thumbnail"]/yt-image/img')
        result.click()

        print("Search completed. Close the browser manually if needed.")


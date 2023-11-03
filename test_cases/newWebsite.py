from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome driver with the correct service
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

website = "https://www.thesun.co.uk/sport/football"  # Fixed typo in 'football'
# 'path' variable is not used, so I'm removing it

# You need to navigate to the website before finding elements
driver.get(website)

# Correcting the way of finding elements
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').text
    subtitle = container.find_element(by="xpath", value='./a/p').text

    container.find_element(by="xpath", value='./a')


# Close the driver after you're done
driver.quit()

from selenium import webdriver

def f_test_script():

    driver = webdriver.Chrome()

    driver.get("https://www.youtube.com")

    title=driver.title

    print("Title: ",title)

    driver.quit()

if __name__=="__main__":
    f_test_script()
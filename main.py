from time import sleep

from selenium.webdriver.common.by import By

from InternetSpeedTwitterBot import InternetSpeedTwitterBot


def get_internet_speed():
    istb = InternetSpeedTwitterBot()

    url = "https://www.speedtest.net/"

    istb.driver.get(url)

    # Wait for the page to load
    sleep(3)
    go_btn = istb.driver.find_element(By.XPATH,
                                      '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
    go_btn.click()
    sleep(45)

    dismiss_btn = istb.driver.find_element(By.XPATH,
                                           '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
    dismiss_btn.click()
    download_rate = istb.driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[1]/span')
    download_rate_text = download_rate.text
    print(download_rate_text)
    download_rate_value = istb.driver.find_element(By.XPATH,
                                                   '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
    download_rate_value_text = download_rate_value.text
    print(download_rate_value_text)
    upload_rate = istb.driver.find_element(By.XPATH,
                                           '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[1]/span')
    upload_rate_text = upload_rate.text
    print(upload_rate_text)
    upload_rate_value = istb.driver.find_element(By.XPATH,
                                                 '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
    upload_rate_value_text = upload_rate_value.text
    print(upload_rate_value_text)

    istb.driver.quit()
    return download_rate_value_text, download_rate_text, upload_rate_value_text, upload_rate_text


def tweet_at_provider(twit_text):
    istb = InternetSpeedTwitterBot()
    url = "https://twitter.com/"
    istb.driver.get(url)

    sign_in_btn = istb.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
    sign_in_btn.click()
    sleep(3)
    email_input = istb.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    email_input.send_keys(istb.my_email)
    next_btn = istb.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
    next_btn.click()
    sleep(1)
    try:
        username_input = istb.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username_input.send_keys("yuvalco")
        next2_btn = istb.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        next2_btn.click()
        sleep(2)
        pass_input = istb.driver.find_element(By.XPATH,
                                              '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_input.send_keys(istb.my_password)
        login_btn = istb.driver.find_element(By.XPATH,
                                             '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        login_btn.click()
    except:
        pass_input = istb.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_input.send_keys(istb.my_password)
        login_btn = istb.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        login_btn.click()
    sleep(5)
    post_input = istb.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    post_input.send_keys(f"My internet speed is: {twit_text} with Cellcom Fiber")
    post_btn = istb.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')
    post_btn.click()
    istb.driver.quit()


    # The code below is if we need to handle pop up windows....
    # base_window = istb.driver.window_handles[0]
    # fifty_bln_pop = istb.driver.window_handles[1]
    # istb.driver.switch_to.window(fifty_bln_pop)
    # print(istb.driver.title)

##############################################################################################################


dratevalue, drate, uratevalue, urate = get_internet_speed()

twit_text = f"Download is {dratevalue}{drate}/Sec and Upload is {uratevalue}{urate}/Sec"
#twit_text = f"Download is 440MB/Sec  and Upload is 103MB/Sec"

print("Speedtest Results are: "+twit_text)
tweet_at_provider(twit_text)



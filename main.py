import pdb
import os, time
import cv2
from pyzbar import pyzbar
from selenium import webdriver
from selenium.webdriver.common.by import By


def qrcode2website(qrcode_path='./test.png'):
    # 1、读取二维码图片
    qrcode = cv2.imread(qrcode_path)
    # 2、解析二维码中的数据
    data = pyzbar.decode(qrcode)
    # 3、在数据中解析出二维码的data信息
    website = data[0].data.decode('utf-8')
    return website

def driver_login(driver, user="12345678910", password="********"):
    driver.find_element(By.XPATH, "//*[@placeholder='请输入手机号']").send_keys(user)
    driver.find_element(By.XPATH, "//*[@type='password']").send_keys(password)
    driver.find_element(By.XPATH, "//*[@class='login-button']").click()

def driver_write(driver, roll_size=400, answer=[1,1,1,2,2,2]):
    # 如涉及安全、隐私、财产等问题，请确保答案的准确性
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/ul/li[1]/div[2]/div[1]/ul/li[{}]".format(str(answer[0]))).click()
    driver.execute_script('window.scrollBy(0,{})'.format(str(roll_size)))
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/ul/li[2]/div[2]/div[1]/ul/li[{}]".format(str(answer[1]))).click()
    driver.execute_script('window.scrollBy(0,{})'.format(str(roll_size)))
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/ul/li[3]/div[2]/div[1]/ul/li[{}]".format(str(answer[2]))).click()
    driver.execute_script('window.scrollBy(0,{})'.format(str(roll_size)))
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/ul/li[4]/div[2]/div[1]/ul/li[{}]".format(str(answer[3]))).click()
    driver.execute_script('window.scrollBy(0,{})'.format(str(roll_size)))
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/ul/li[5]/div[2]/div[1]/ul/li[{}]".format(str(answer[4]))).click()
    driver.execute_script('window.scrollBy(0,{})'.format(str(roll_size)))
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/ul/li[6]/div[2]/div[1]/ul/li[{}]".format(str(answer[5]))).click()
    # driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/button[2]").click()

def approach_website(website, add_header=False):
    if add_header:
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
        opt = webdriver.ChromeOptions()
        opt.add_argument('--user-agent=%s' % user_agent)
        driver = webdriver.Chrome(options=opt)
    else:
        driver = webdriver.Chrome()
    try:
        # 打开登陆界面
        driver.get(website)
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "/html/body/div[1]/body/div/div[8]/div[2]/div[3]/button").click()
        driver.find_element(By.XPATH, "/html/body/div[1]/body/div/div[2]/img[2]").click()
        driver.implicitly_wait(5)
        # 注册登陆
        driver_login(driver)
        driver.implicitly_wait(1)
        # 填写表单
        driver_write(driver, roll_size=400)
        print('success')
    except:
        print('error')
    finally:
        driver.close()

def batch_handle(dir_list):
    imgs = os.listdir(dir_list)
    for img in imgs:
        img_path = os.path.join(dir_list, img)
        website = qrcode2website(img_path)
        print(website)
        approach_website(website)
        time.sleep(10)

if __name__ == '__main__':
    batch_handle('./test')

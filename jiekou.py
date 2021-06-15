from selenium import webdriver
from fake_useragent import UserAgent
from time import  sleep
from downloadpic import savepic
#https://www.opacg.com/bg/PC/acgurl.php, {"User-Agent": UserAgent().random}
def jiekoupicture(apiurl):
    try:
        m = input("请输入要找的图片数：")
        n = int(eval(m))
        browser = webdriver.Edge("E:\python\msedgedriver.exe", {"User-Agent": UserAgent().random})
        browser.get("https://www.bilibili.com/")
        browser.maximize_window()
        t=0
        while t<n:
            newwindow = "window.open('{}')".format(apiurl)
            browser.execute_script(newwindow)
            handles = browser.window_handles
            browser.switch_to.window(handles[-1])
            imgbq = browser.find_element_by_tag_name('img')
            sleep(2)
            url = imgbq.get_attribute("src")
            imgurl = str(url)
            name = imgurl.split('/')[-1]
            if savepic(imgurl, name)==1 :
                t = t + 1
            sleep(2)
            browser.close()
            browser.switch_to.window(handles[0])
    except:
        print("程序出错了")
    browser.quit()
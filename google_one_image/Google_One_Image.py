from selenium import webdriver
import logging
logging.getLogger().setLevel(logging.INFO)
def get_image(item,executable_path="./chromedriver",headless=True):
    option = webdriver.ChromeOptions()
    if headless:
        option.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=executable_path, options=option)
    try:
        if not headless:
            driver.implicitly_wait(100)
        if type(item)==type([]):
            images = []
            logging.info(f"There are {len(item)} keywords.")
            for i in range(len(item)):
                keyword = item[i]
                driver.get(f'https://www.google.com.hk/search?q={keyword}&tbm=isch&ved=2ahUKEwi347PthejqAhUC6JQKHRAvCuUQ2-cCegQIABAA&oq=%E8%B3%88%E7%82%B3%E9%81%94%E9%81%93%E5%85%AC%E5%9C%92+%E8%B6%B3%E7%90%83%E5%A0%B4&gs_lcp=CgNpbWcQDFAAWABg5jVoAHAAeACAAQCIAQCSAQCYAQCqAQtnd3Mtd2l6LWltZw&sclient=img&ei=bfUbX_f4GYLQ0wSQ3qioDg&authuser=0&bih=1306&biw=1146&hl=zh-TW')
                element = driver.find_element_by_xpath('//img[@class="rg_i Q4LuWd"]')
                image = element.get_attribute('src')
                images.append(image)
                logging.info(f"[Got#{i+1}] {keyword}: {image[0:40]}...")
            driver.quit()
            return images
        else:
            driver.get(
                f'https://www.google.com.hk/search?q={item}&tbm=isch&ved=2ahUKEwi347PthejqAhUC6JQKHRAvCuUQ2-cCegQIABAA&oq=%E8%B3%88%E7%82%B3%E9%81%94%E9%81%93%E5%85%AC%E5%9C%92+%E8%B6%B3%E7%90%83%E5%A0%B4&gs_lcp=CgNpbWcQDFAAWABg5jVoAHAAeACAAQCIAQCSAQCYAQCqAQtnd3Mtd2l6LWltZw&sclient=img&ei=bfUbX_f4GYLQ0wSQ3qioDg&authuser=0&bih=1306&biw=1146&hl=zh-TW')
            element = driver.find_element_by_xpath('//img[@class="rg_i Q4LuWd"]')
            image = element.get_attribute('src')
            driver.quit()
            return image
    except Exception as e:
        if type(item)==type([]):
            return images
        else:
            return images
        logging.info(f"[Error] {e}")
        driver.quit()
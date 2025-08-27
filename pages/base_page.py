from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    # locator'a ait olan elementi bulamk için tanımladığım fonksyion
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    # elementin görünür ve tıklanabilr olmasını beklemek ve tıklamak için tanımladığım fonksiyon
    def click(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        
        # tıklama başarısız olduğunda js ile tıklamayı sağladım
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", self.find_element(locator))
        except TimeoutException as e:
            raise TimeoutException(f"Hata: '{locator}' elementi tıklanabilir hale gelmedi ya da bulunamadı.")

    # sayfanın doğru yüklendiğini doğrulamak için tanımladığım fonksiyon
    def get_title(self):
        return self.driver.title

    # test başarısız oldugunda ekran görüntüsü almak için tanımladığım fonksiyon
    def take_screenshot(self, name="screenshot"):
        self.driver.save_screenshot(f"{name}.png")
            
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    URL = "https://useinsider.com/"

    # locatorlar
    ACCEPT_COOKIES_BUTTON = (By.ID, "wt-cli-accept-all-btn") # çerezlerdeki kabul butonu 
    CAREERS_LINK = (By.XPATH, "//a[normalize-space()='Careers']") # Careers metinli link
    COMPANY_MENU = (By.XPATH, "//a[normalize-space()='Company']") # Company metinli link

    def __init__(self, driver):
        super().__init__(driver)
        
    # ana sayfaya gidip sayfanın doğru yüklendiğini kontrol edip ve varsa çerez bildirimini yönetmek için tanımladığım fonksyion
    def navigate_home_page(self):
        self.driver.get(self.URL)
        self.wait.until(EC.url_contains(self.URL)) # sayfanın yuklendiğini dogrulamak için 
        self.handle_cookies_popup()

    # sayfadaki cookie bildirimini yöneymek için tanımladığım fonksiyon
    def handle_cookies_popup(self):
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable(self.ACCEPT_COOKIES_BUTTON)) # cookie butonunun tıklanabilir olması için beklenir
            cookie_button.click()
            print("Çerez bildirimi kabul edildi")
            
            self.wait.until(EC.invisibility_of_element_located(self.ACCEPT_COOKIES_BUTTON))
        except:
            print("Çerez bildirimi bulunamadı")
            pass

    # Company menüsüne sonra Careers sayfasına gitmek için tanımladığım fonksiyon
    def go_to_careers_page(self):
        try:
            company_menu = self.find_element(self.COMPANY_MENU)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", company_menu) # elementin görüntülenebilmesi için sayfa kaydırmak için scroll ekledim
            
            self.wait.until(EC.element_to_be_clickable(self.COMPANY_MENU))
            company_menu.click()

            careers_link = self.find_element(self.CAREERS_LINK)
            self.wait.until(EC.element_to_be_clickable(self.CAREERS_LINK)) # tıklanabilir olması bekleniyor
            careers_link.click()
            
            print("Careers sayfasına gidildi")
            
        except Exception as e:
            print(f"Hata: Detay: {e}")
            raise 
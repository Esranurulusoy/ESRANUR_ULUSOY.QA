from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CareersPage(BasePage):
    URL = "https://useinsider.com/careers/"
    
    # locatorlar
    LOCATIONS_BLOCK_TITLE = (By.XPATH, "//h3[contains(text(), 'Our Locations')]")
    # 'Our Teams' butonu web sitesinde yer almadığı için onun yerine 'Find your calling' kullandım.
    TEAMS_BLOCK_TITLE = (By.XPATH, "//h3[contains(text(), 'Find your calling')]")
    LIFE_AT_INSIDER_BLOCK_TITLE = (By.XPATH, "//h2[contains(text(), 'Life at Insider')]")
    
    SEE_ALL_TEAMS_BUTTON = (By.XPATH, "//a[contains(text(), 'See all teams')]")
    QUALITY_ASSURANCE_LINK = (By.XPATH, "//a[contains(@href, '/quality-assurance/')]") 
    SEE_ALL_QA_JOBS_BUTTON = (By.XPATH, "//a[contains(text(), 'See all QA jobs')]")

    def __init__(self, driver):
        super().__init__(driver)

    # blokların görünürlüğünü doğrulayan fonksiyonu tanımladım
    def verify_page_blocks(self):
        self.wait.until(EC.visibility_of_element_located(self.LOCATIONS_BLOCK_TITLE))
        assert self.find_element(self.LOCATIONS_BLOCK_TITLE).is_displayed(), "'Our Locations' bloğu görünür değil"
        print("'Our Locations' bloğu görünür")
        
        self.wait.until(EC.visibility_of_element_located(self.TEAMS_BLOCK_TITLE))
        assert self.find_element(self.TEAMS_BLOCK_TITLE).is_displayed(), "'Find your calling' bloğu görünür değil"
        print("'Find your calling' bloğu görünür") 
        
        self.wait.until(EC.visibility_of_element_located(self.LIFE_AT_INSIDER_BLOCK_TITLE))
        assert self.find_element(self.LIFE_AT_INSIDER_BLOCK_TITLE).is_displayed(), "'Life at Insider' bloğu görünür değil"
        print("'Life at Insider' bloğu görünür")

    # Career sayfasından QA jobs sayfasına gitmeyi sağlamak için tanımladığım fonksiyon
    def go_to_qa_jobs_page(self):
        try:
            # See all teams butonuna tıklamak için
            self.click(self.SEE_ALL_TEAMS_BUTTON)
            print("See all teams butonuna tıklandı")

            # Quality Assurance linkini bulmak ve tıklamak için
            self.wait.until(EC.visibility_of_element_located(self.QUALITY_ASSURANCE_LINK)) # linkin görünür olması beklenir
            self.click(self.QUALITY_ASSURANCE_LINK)
            print("Quality Assurance linkine tıklandı")

            # See all QA jobs butonunu bulmak ve tıklamak için
            self.wait.until(EC.visibility_of_element_located(self.SEE_ALL_QA_JOBS_BUTTON))
            self.click(self.SEE_ALL_QA_JOBS_BUTTON)
            print("See all QA jobs butonuna tıklandı")
            
        except Exception as e:
            print(f"Hata: Detay: {e}")
            raise
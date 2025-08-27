
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class JobsPage(BasePage):
    URL = "https://useinsider.com/careers/quality-assurance/"
    
    #locatorlar
    LOC_FILTER = (By.XPATH, "//span[@id='select2-filter-by-location-container']")
    DEPT_FILTER = (By.XPATH, "//span[@id='select2-filter-by-department-container']")
    JOB_RESULTS = (By.CSS_SELECTOR, ".job-list")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 60)
    
    # dropdown menuyu açıp seçeneği seçmek için tanımladığım fonksiyon
    # ***Filter by Department menusunde departmanı seçiyor fakat Filter by Location dropdown menusunde hata veriyor lokasyonu seçemiyor***         
    def select_filter_option(self, filter_locator, option_text):
        self.wait.until(EC.visibility_of_element_located(filter_locator))   
        self.wait.until(EC.element_to_be_clickable(filter_locator)).click()
        option_locator = (By.XPATH, f"//span[contains(@class, 'select2-results__option') and contains(text(), '{option_text}')]")
        self.wait.until(EC.element_to_be_clickable(option_locator)).click()
        
    # işleri filtrelemek iiçin tanımladığım fonksiyon
    def filter_jobs(self, location, department):
        self.select_filter_option(self.LOC_FILTER, location)
        self.select_filter_option(self.DEPT_FILTER, department)
        print("Filtreleme tamamlandı")

    # iş detaylarını doğrulamak için tanımladığım fonksyion
    def verify_job_details(self, position, department, location):
        self.wait.until(EC.visibility_of_element_located(self.JOB_RESULTS))
        jobs = self.find_elements(self.JOB_RESULTS)
        assert len(jobs) > 0, "İlan bulunamadı"
        print(f"{len(jobs)} adet iş ilanı bulundu")

        for job in jobs:
            job_text = job.text
            assert position in job_text, f"Pozisyon '{position}' içermiyor"
            assert department in job_text, f"Departman '{department}' içermiyor"
            assert location in job_text, f"Lokasyon '{location}' içermiyor"
        
    # basvuru formuna gitmek için tanımladığım fonksiyon
    def go_to_application_form(self, job_title="Quality Assurance Engineer"):
        view_role_locator = (By.XPATH, f"//p[contains(text(), '{job_title}')]/ancestor::div[contains(@class, 'card-job')]//a[contains(text(), 'View Role')]")
        self.wait.until(EC.element_to_be_clickable(view_role_locator)).click()
        print("View Role butonuna tıklandı")

        
    


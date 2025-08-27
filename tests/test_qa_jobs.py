import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.jobs_page import JobsPage

@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_qa_job_application_flow(driver):
    try:
        # Home Page'e gitme ve doğrulama
        home_page = HomePage(driver)
        home_page.navigate_home_page()
        assert home_page.URL in driver.current_url, "Home Page URL'i yanlış"

        home_page.go_to_careers_page()
        
        #  Careers sayfasının URL'ini doğrulama
        expected_careers_url = "https://useinsider.com/careers/"
        assert expected_careers_url in driver.current_url, "Careers sayfası URL'i yanlış"
        
        careers_page = CareersPage(driver)
        
        # Careers sayfasındaki blokları doğrulama
        careers_page.verify_page_blocks()

        # See all QA jobs butonuna tıklama ve iş ilanları sayfasına gitme
        careers_page.go_to_qa_jobs_page()
        
        # QA Jobs URL'ini doğrulama
        expected_qa_url_part = "careers/quality-assurance"
        expected_qa_url_part_alt = "department=qualityassurance"
        assert expected_qa_url_part in driver.current_url or expected_qa_url_part_alt in driver.current_url, "QA iş ilanları sayfası URL'i yanlış"
                
        jobs_page = JobsPage(driver)
        
        # iş ilanlarını verilen filtrelere göre filtreleme ve sonuçları doğrulama
        # verilen dosyada Istanbul, Turkey yazıyor fakat web sitesinde Türkiye yazdığı için Türkiye olarak kullandım.
        jobs_page.filter_jobs(location="Istanbul, Turkiye", department="Quality Assurance") 
        jobs_page.verify_job_details(
            position="Quality Assurance",
            department="Quality Assurance",
            location="Istanbul, Turkiye"
        )
        
        # View Role butonuna tıklama ve başvuru formuna yönlendirmeyi kontrol etnme
        jobs_page.go_to_application_form()
        assert "lever.co" in driver.current_url, "Başvuru formu sayfasına yönlendirme başarısız"

    except Exception as e:
        base_page = BasePage(driver)
        base_page.take_screenshot(name=f"failure_{e.__class__.__name__}")
        pytest.fail(f"Test başarısız: {e}")
        
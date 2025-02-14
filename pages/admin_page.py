from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class AdminPage:
    def __init__(self, driver):
        self.driver = driver

        # Xác định các phần tử trên trang login
        self.menu_hover = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[5]")  # Phần tử cần hover  # Phần tử cần hover
        self.menu_admin =  (By.XPATH, "//h6[contains(text(), 'Admin')]")
        
    def open_admin_hover(self):
        # Tạo hành động hover
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()
        # Chờ phần tử Admin xuất hiện
        admin_name = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.menu_admin)
        )

        
    # def open_new_product_page(self):
    #     self.driver.find_element(*self.new_product_link).click()
    #     return CreateNewProductPage(self.driver)

    def check_admin_page_display(self):
        try:
            admin_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//h6[contains(text(), 'Admin')]"))
            )
            assert admin_element is not None, "❌ Không tìm thấy phần tử Admin!"
            print("✅ Profile admin name exists!")
        except Exception as e:
            assert False, f"❌ Lỗi khi kiểm tra Admin: {str(e)}"



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.admin_food_page import CreateNewFoodPage

class AdminPage:
    def __init__(self, driver):
        self.driver = driver

       
        
    def open_admin_hover(self):
        
        
         # Xác định phần tử cần hover
        hover_element = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div[5]") 
        
        # Chờ menu admin xuất hiện trước khi hover
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h6[contains(text(), 'Admin')]"))
        )

        # Thực hiện hover
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_element).perform()
        
        # Gọi phương thức mở trang Add Food
        return self.open_add_food_page()

    def open_add_food_page(self):
        # Click vào liên kết "Add Food"
        add_food_link = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/add/#food?page=1']/div"))
        )
        add_food_link.click()

        # Trả về trang mới để tiếp tục thao tác
        return CreateNewFoodPage(self.driver)


    def check_admin_page_display(self):
        try:
            admin_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//h6[contains(text(), 'Admin')]"))
            )
            assert admin_element is not None, "❌ Không tìm thấy phần tử Admin!"
            print("✅ Profile admin name exists!")
        except Exception as e:
            assert False, f"❌ Lỗi khi kiểm tra Admin: {str(e)}"



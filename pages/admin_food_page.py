from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateNewFoodPage():
    def __init__(self, driver):
        self.driver = driver

    
        self.title_input = (By.NAME, "name")  # Trường input cho Tname
        self.price_input = (By.NAME, "price")  # Trường input cho Price
        self.photo_input = (By.XPATH, "//input[@type='file' and @name='image']")
        self.add_food_button = (By.XPATH, "//button[contains(text(), 'Thêm')]")  # Nút "Add Product"
        self.message_create_food_successfully = (By.XPATH, "//*[@id='root']/div/div/div[3]/div[2]/div/div/form/div[2]")
        self.message_create_food_failed = (By.XPATH, "//*[@id='root']/div/div/div[3]/div[2]/div/div/form/p")



    def enter_title(self, title):
        self.driver.find_element(*self.title_input).send_keys(title)

    def enter_price(self, price):
        self.driver.find_element(*self.price_input).send_keys(price)


    def enter_image_url(self, image):
        self.driver.find_element(*self.photo_input).send_keys(image)

    def click_food_product(self):
        """Nhấn nút 'Add Product' để gửi form."""
        self.driver.find_element(*self.add_food_button).click()

    def is_success_message_appeared(self):
        try:
            error_element = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.message_create_food_failed)
            )
            return f"❌ Lỗi: {error_element.text}"
        except TimeoutException:
            pass 
        
        try:
            success_element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.message_create_food_successfully)
            )
            return f"✅ Thành công: {success_element.text}"
        except TimeoutException:
            return "❌ Không có thông báo nào hiển thị!"




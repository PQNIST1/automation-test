from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver


        # Xác định các phần tử trên trang login
        self.login_button =  (By.XPATH, "//a[@href='/login']/button")
        self.register_button =  (By.XPATH, "//a[@href='/register']/button")
        self.username_input = (By.NAME, "name")  # Tìm trường username
        self.password_input = (By.XPATH, "//input[@type='password']")   # Tìm trường password
        self.submit_button = (By.XPATH, "//button[@type='submit']")  # Nút submit
        

    def open_login_form(self):
        self.driver.find_element(*self.login_button).click()

    def open_register_form(self):
        self.driver.find_element(*self.register_button).click()

    # Hàm để nhập tên đăng nhập
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    # Hàm để nhập mật khẩu
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    # Hàm để nhấn nút login
    def click_login(self):
        self.driver.find_element(*self.submit_button).click()
      
    def get_error_message(self):
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div[1]/div/form/p"))
            )
            return error_element.text  # Trả về nội dung lỗi thay vì chỉ in ra
        except TimeoutException:
            return None  # Trả về None nếu không có lỗi thay vì in ra thông báo
        
    def check_profile_page_display(self):
        try:
            profile_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[1]/div[5]/div[2]/div[1]/h6"))
            )
            assert profile_element is not None, "❌ Không tìm thấy Profile Name!"
            print("✅ Profile name exists!")
        except Exception as e:
            assert False, f"❌ Lỗi khi kiểm tra Profile: {str(e)}"


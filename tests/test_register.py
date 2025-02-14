import unittest
import configparser

import HtmlTestRunner
import sys
import os



# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.register_page import RegisterPage
from utils.browser_setup import BrowserSetup


class RegisterTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)  # Sử dụng URL từ file config

    def test_valid_account_register(self):
        register_page = RegisterPage(self.driver)

        register_page.open_register_form()
        # Nhập thông tin đăng nhập
        register_page.enter_username("pqnist")
        register_page.enter_email("nguyen111@gmail.com")
        register_page.enter_phone("04343436")
        register_page.enter_password("123456")
        register_page.enter_cf_password("123456")
        
        register_page.click_register()

      
        # register_page = RegisterPage(self.driver)
        # register_page.check_profile_page_display()
        
        error_message = register_page.get_error_message()

        self.assertIsNotNone(error_message, "❌ Không có thông báo lỗi khi đăng nhập sai!")
        self.assertIn("username, phone or email already exists in the system", error_message, "❌ Thông báo lỗi không đúng!")
        print(f"✅ Thông báo lỗi hiển thị đúng: {error_message}")


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))


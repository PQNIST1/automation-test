import unittest
import configparser

import HtmlTestRunner
import sys
import os



# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


class LoginTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)  # Sử dụng URL từ file config

    def test_valid_login_with_admin_account(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("Admin")
        login_page.enter_password("123456")
        login_page.click_login()

      
        # Gọi hàm check để kiểm tra tên Admin có xuất hiện không
        admin_page = AdminPage(self.driver)
        admin_page.check_admin_page_display()


    def test_valid_login_with_user_account(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("nguyen")
        login_page.enter_password("123456")
        login_page.click_login()

        login_page = LoginPage(self.driver)
        login_page.check_profile_page_display()

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_form()
        
        login_page.enter_username("wronguser")
        login_page.enter_password("wrongpass")
        login_page.click_login()

        error_message = login_page.get_error_message()

        self.assertIsNotNone(error_message, "❌ Không có thông báo lỗi khi đăng nhập sai!")
        self.assertIn("Unauthorized: Invalid username or password", error_message, "❌ Thông báo lỗi không đúng!")
        print(f"✅ Thông báo lỗi hiển thị đúng: {error_message}")
        


    def test_navigate_to_the_registration_page(self):
        login_page = LoginPage(self.driver)
        expected_login_url = "https://cinema-ticket-booking-frontend.onrender.com/login"
        expected_register_url = "https://cinema-ticket-booking-frontend.onrender.com/register"

        # Mở trang đăng nhập
        login_page.open_login_form()
        self.assertEqual(self.driver.current_url, expected_login_url, "❌ Không phải trang đăng nhập!")
        print("✅ Đang ở trang login")

        # Chuyển sang trang đăng ký
        login_page.open_register_form()
        self.assertEqual(self.driver.current_url, expected_register_url, "❌ Không phải trang đăng ký!")
        print("✅ Đang ở trang register")
        

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))


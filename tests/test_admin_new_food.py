import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_setup import BrowserSetup
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.admin_food_page import CreateNewFoodPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateNewFoodTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)  # Sử dụng URL từ file config
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("Admin")
        login_page.enter_password("123456")
        login_page.click_login()
        
        # Gọi hàm check để kiểm tra tên Admin có xuất hiện không
        admin_page = AdminPage(self.driver)
        admin_page.check_admin_page_display()

    # def test_open_add_food_page(self):
    #     """Kiểm tra xem có mở được trang Add Food sau khi hover không"""
    #     admin_page = AdminPage(self.driver)
    #     admin_page.open_admin_hover()

    #     # Kiểm tra xem trang Add Food có mở thành công không
    #     current_url = self.driver.current_url
    #     self.assertIn("/add/#food", current_url, "❌ Không mở được trang Add Food!")
    #     print("✅ Mở thành công!")

    def test_creat_new_product_successfully(self):
        admin_page = AdminPage(self.driver)
        create_new_food_page= admin_page.open_admin_hover()
        create_new_food_page.enter_title("Nước Ngọt vị đào")
        create_new_food_page.enter_price("30000")
        create_new_food_page.enter_image_url(r"E:\cv\in_cv\Movie-food\combo199k-dd-coonline_1707397095517.jpg")
        create_new_food_page.click_food_product()
        message = create_new_food_page.is_success_message_appeared()
       

        if "❌ Lỗi" in message:
            print(message)
            self.fail("Tạo sản phẩm thất bại")
        else:
            print(message)
            self.assertTrue("✅ Thành công" in message)

       
       
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))


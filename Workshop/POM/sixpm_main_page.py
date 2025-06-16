from selenium.webdriver.common.by import By
from Helper.helper import Helper
from Test_data import test_data


class SIXPMPAGE(Helper):

    search_field = (By.XPATH, '//*[@id="searchAll"]', "Search Input Field")
    search_icon = (By.XPATH, '//*[@id="searchForm"]/button', "Search Icon/Button")

    def search_text(self):
        try:
            self.test_logger.info("Starting search action on SIXPMPAGE.")
            self.test_logger.info(f"Entering search text: '{test_data.search_text}'")

            self.find_and_send_keys(self.search_field, test_data.search_text)

            self.test_logger.info("Clicking on search icon.")
            self.find_and_click(self.search_icon)

            self.test_logger.info("Search submitted successfully.")
        except Exception as e:
            self.test_logger.exception(f"Exception occurred during search: {e}")

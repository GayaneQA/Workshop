from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class Helper:

    def __init__(self, driver, test_logger):
        self.driver = driver
        self.test_logger = test_logger

    def go_to_page(self, url):
        self.test_logger.info(f"Navigating to URL: {url}")
        self.driver.get(url)
        self.test_logger.info(f"Page opened: {url}")

    def find_elem_ui(self, loc, sec=60):
        by, value, desc = loc
        self.test_logger.info(f"Waiting for visibility of element: {desc}")
        try:
            elem = WebDriverWait(self.driver, sec).until(
                EC.visibility_of_element_located((by, value))
            )
            self.test_logger.info(f"Element is visible: {desc}")
            return elem
        except TimeoutException:
            self.test_logger.error(f"Timeout: Element not visible after {sec} seconds: {desc}")
        except Exception as e:
            self.test_logger.exception(f"Exception while waiting for visible element '{desc}': {e}")

    def find_elm(self, loc, timout=15, get_attribute="", get_text=""):
        by, value, desc = loc
        self.test_logger.info(f"Locating element: {desc}")
        try:
            element = WebDriverWait(self.driver, timout).until(
                EC.presence_of_element_located((by, value))
            )
            self.test_logger.info(f"Element located: {desc}")
            if get_attribute:
                value = element.get_attribute(get_attribute)
                self.test_logger.info(f"Attribute '{get_attribute}' of {desc}: {value}")
                return value
            elif get_text:
                text = element.text
                self.test_logger.info(f"Text of {desc}: {text}")
                return text
            else:
                return element
        except TimeoutException:
            self.test_logger.error(f"Timeout: Element not found after {timout} seconds: {desc}")
        except Exception as e:
            self.test_logger.exception(f"Exception while locating element '{desc}': {e}")

    def find_and_click(self, loc, sec=60):
        by, value, desc = loc
        self.test_logger.info(f"Attempting to click element: {desc}")
        try:
            elem = WebDriverWait(self.driver, sec).until(
                EC.element_to_be_clickable((by, value))
            )
            elem.click()
            self.test_logger.info(f"Clicked element: {desc}")
        except TimeoutException:
            self.test_logger.error(f"Timeout: Element not clickable after {sec} seconds: {desc}")
        except Exception as e:
            self.test_logger.exception(f"Exception while clicking element '{desc}': {e}")

    def find_and_send_keys(self, loc, inp_text, sec=60):
        by, value, desc = loc
        self.test_logger.info(f"Sending keys to element '{desc}': '{inp_text}'")
        try:
            elem = self.find_elem_ui(loc, sec)
            elem.send_keys(inp_text)
            self.test_logger.info(f"Keys sent to element: {desc}")
        except Exception as e:
            self.test_logger.exception(f"Exception while sending keys to '{desc}': {e}")

    def hover_and_click(self, locator):
        by, value, desc = locator
        self.test_logger.info(f"Hovering and clicking on element: {desc}")
        try:
            element = self.find_elm(locator)
            ActionChains(self.driver).move_to_element(element).click().perform()
            self.test_logger.info(f"Hovered and clicked on element: {desc}")
        except Exception as e:
            self.test_logger.exception(f"Exception while hovering and clicking '{desc}': {e}")

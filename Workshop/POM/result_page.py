from selenium.webdriver.common.by import By
from Helper.helper import Helper


class RESULTPAGE(Helper):

    # locators with description as the 3rd tuple item
    brand_checkbox = (By.XPATH, '//*[@id="brandNameFacet"]', "Brand Checkbox")
    brand_name = (By.XPATH, '//li[a//span[text()="RAEN Optics"]]', "Brand: RAEN Optics")
    price_checkbox = (By.XPATH, '//*[@id="priceFacet"]', "Price Checkbox")
    price = (By.XPATH, '//a//span[text()="$200.00 and Under"]', "Price: $200.00 and Under")
    color_checkbox = (By.XPATH, '//*[@id="colorFacet"]', "Color Checkbox")
    orange = (By.XPATH, '//a//span[text()="Orange"]', "Color: Orange")
    result_item_count = (By.XPATH, '//span[@class="wt-z"]', "Filtered Result Count")
    item_title = (By.XPATH, '//*[@id="products"]//article/a', "Search Result Title")

    def select_narrow_choices(self):
        self.test_logger.info("Starting selection of narrow choices on Result Page.")

        self.hover_and_click(self.brand_checkbox)
        self.find_and_click(self.brand_name)

        self.hover_and_click(self.price_checkbox)
        self.find_and_click(self.price)

        self.hover_and_click(self.color_checkbox)
        self.find_and_click(self.orange)

        result_count = self.find_elm(self.result_item_count, get_text=True)
        self.test_logger.info(f"Filtered result count is: {result_count}")

        item_title = self.find_elm(self.item_title, get_text=True)
        self.test_logger.info(f"First search result item title: {item_title}")

        return item_title

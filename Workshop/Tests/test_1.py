import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
from POM.sixpm_main_page import SIXPMPAGE
from POM.result_page import RESULTPAGE
from Test_data import test_data
import re


def test_1(test_driver, test_logger):

    # activate Chrome browser
    open_6pm_obj = SIXPMPAGE(test_driver, test_logger)
    open_6pm_obj.go_to_page(config.URL)
    open_6pm_obj.search_text()
    test_logger.info("Search text 'classic sunglasses' is sent")
    # Navigate to result page
    result = RESULTPAGE(test_driver, test_logger)
    text = result.select_narrow_choices()

    # Extract and validate brand name
    brand_name = text.split(" - ")[0].strip()
    assert brand_name == test_data.brand_name, "Name is not same"
    test_logger.info(msg='Selected and searched names match')

    # Extract the first price value from the text
    get_price_from_text = re.search(r'\$([\d.,]+)', text)

    if get_price_from_text:
        # Extract price as string, remove commas and trailing dot
        price_str = get_price_from_text.group(1).replace(',', '').rstrip('.')
        price = float(price_str)
        test_logger.info(f'Parsed price: {price}')

        # Extract maximum allowed price from test data
        max_price_match = re.search(r'\$([\d.,]+)', test_data.price)
        if max_price_match:
            max_price_str = max_price_match.group(1).replace(',', '').rstrip('.')
            max_price = float(max_price_str)
            test_logger.info(f'Max allowable price: {max_price}')

            assert price <= max_price, f"Actual price ${price} exceeds allowed maximum of ${max_price}"
            test_logger.info(f'Price from item is in range {test_data.price}')
        else:
            raise ValueError(f"Invalid price format in test data: {test_data.price}")
    else:
        raise AssertionError("Price not found in the result text")

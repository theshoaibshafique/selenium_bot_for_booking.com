# This file will include a class with instance methods.
# That will be responsible to interact with our website
# After we have some results, to apply filtrations.
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_start_rating(self, star_value):
        # star_filtration_box = self.driver.find_element_by_css_selector(
        #     'div[class="ffa9856b86 ad9a06523f"]'
        # )
        # star_child_elements = star_filtration_box.find_elements_by_css_selector("*")
        # for star_element in star_child_elements:
        #     if (
        #         str(star_element.get_attribute("innerHTML")).strip()
        #         == f"{star_value} stars"
        #     ):
        #         star_element.click()
        star_element = self.driver.find_element_by_css_selector(
            'div[data-filters-item="class:class=5"]'
        )
        star_element.click()

    def sort_price_lowest_first(self):
        element = self.driver.find_element_by_css_selector('li[data-id="price"]')
        element.click()

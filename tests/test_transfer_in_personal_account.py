from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestTransferInPersonalAccount:

    def test_transfer_in_personal_account_from_main_page(self, driver, log_in_account):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_PERSONAL_ACCOUNT_FORM)))
        assert 'https://stellarburgers.nomoreparties.site/account' in driver.current_url
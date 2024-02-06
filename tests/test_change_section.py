from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestExitFromAccount:

    def test_change_section_to_stuffing(self, driver, log_in_account):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_PERSONAL_ACCOUNT_FORM)))
        driver.find_element(*TestLocators.SEARCH_LOGO).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_CONSTRUCTOR_FORM)))
        driver.find_element(*TestLocators.SEARCH_CONSTRUCTOR_STUFFING).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_HEADER_STUFFING)))
        assert driver.find_element(*TestLocators.SEARCH_CURRENT_SEC_IN_CONSTRUCT).text == 'Начинки'

    def test_change_section_to_sauces(self, driver, log_in_account):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_PERSONAL_ACCOUNT_FORM)))
        driver.find_element(*TestLocators.SEARCH_LOGO).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_CONSTRUCTOR_FORM)))
        driver.find_element(*TestLocators.SEARCH_CONSTRUCTOR_SAUCES).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_HEADER_SAUCES)))
        assert driver.find_element(*TestLocators.SEARCH_CURRENT_SEC_IN_CONSTRUCT).text == 'Соусы'

    def test_change_section_to_buns(self, driver, log_in_account):
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_PERSONAL_ACCOUNT_FORM)))
        driver.find_element(*TestLocators.SEARCH_LOGO).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_CONSTRUCTOR_FORM)))
        driver.find_element(*TestLocators.SEARCH_CONSTRUCTOR_SAUCES).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_HEADER_SAUCES)))
        driver.find_element(*TestLocators.SEARCH_CONSTRUCTOR_BUNS).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_HEADER_BUNS)))
        assert driver.find_element(*TestLocators.SEARCH_CURRENT_SEC_IN_CONSTRUCT).text == 'Булки'

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from gener_user import GeneratorUser
from url_links import UrlLinks


class TestRegistration:
    def test_registration_add_new_user(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))
        # перешли по ссылке "Зарегистрироваться", подождали загрузку
        driver.find_element(*TestLocators.SEARCH_REGISTRATION_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))
        driver.find_elements(*TestLocators.SEARCH_REGISTRATION_FIELDS)[0].send_keys(
            GeneratorUser.generate_user()[0])
        driver.find_elements(*TestLocators.SEARCH_REGISTRATION_FIELDS)[1].send_keys(
            GeneratorUser.generate_user()[1])
        driver.find_elements(*TestLocators.SEARCH_REGISTRATION_FIELDS)[2].send_keys(
            GeneratorUser.generate_user()[2])
        # нажали "Зарегистрироваться", подождали загрузки страницы
        driver.find_element(*TestLocators.SEARCH_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((TestLocators.SEARCH_ENTER_BUTTON)))
        assert driver.current_url == UrlLinks.authorization_page

    def test_registration_not_correct_password(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*TestLocators.SEARCH_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))
        # перешли по ссылке "Зарегистрироваться", подождали загрузку
        driver.find_element(*TestLocators.SEARCH_REGISTRATION_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SEARCH_AUTHORIZATION_FORM)))
        driver.find_elements(*TestLocators.SEARCH_REGISTRATION_FIELDS)[0].send_keys(
            GeneratorUser.generate_user()[0])
        driver.find_elements(*TestLocators.SEARCH_REGISTRATION_FIELDS)[1].send_keys(
            GeneratorUser.generate_user()[1])
        driver.find_elements(*TestLocators.SEARCH_REGISTRATION_FIELDS)[2].send_keys(
            "12345")
        driver.find_element(*TestLocators.SEARCH_REGISTRATION_BUTTON).click()

        assert driver.find_element(*TestLocators.SEARCH_ERROR_PASSWORD_MSG).text == 'Некорректный пароль'
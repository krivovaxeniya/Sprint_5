from selenium.webdriver.common.by import By


class TestLocators:
#Кнопка "Личный кабинет" в шапке страницы
    SEARCH_PERSONAL_ACCOUNT_BUTTON = By.LINK_TEXT, "Личный Кабинет"
#Форма авторизации и регистрации
    SEARCH_AUTHORIZATION_FORM = By.XPATH, ".//div[contains(@class,'Auth_login')]"
#Ссылка на форму регистрации
    SEARCH_REGISTRATION_LINK = By.LINK_TEXT, "Зарегистрироваться"
#Поля ввода данных пользователя - имя, логин, пароль
    SEARCH_REGISTRATION_FIELDS = By.XPATH, ".//input[@class='text input__textfield text_type_main-default']"
#Кнопка "Зарегистрироваться" на форме регистрации
    SEARCH_REGISTRATION_BUTTON = By.XPATH, ".//button[text()='Зарегистрироваться']"
#Кнопка "Войти" на форме авторизации
    SEARCH_ENTER_BUTTON = By.XPATH, ".//button[text()='Войти']"
#Сообщение "Некорректный пароль"
    SEARCH_ERROR_PASSWORD_MSG = By.XPATH, ".//p[@class='input__error text_type_main-default']"
#Кнопка "Войти в аккаунт" на главной
    SEARCH_LOGIN_IN_ACC_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
#Форма ввода имени на странице авторизации
    SEARCH_INPUT_LOGIN = By.NAME, "name"
#Форма ввода пароля на странице авторизации
    SEARCH_INPUT_PASSWORD = By.NAME, "Пароль"
#Кнопка "Восстановить пароль"
    SEARCH_RECOVER_PASSWORD_BUTTON = By.LINK_TEXT, "Восстановить пароль"
#Ссылка "Войти" на форме восстановления пароля
    SEARCH_ENTER_LINK = By.LINK_TEXT, "Войти"
#Содержимое личного кабинета
    SEARCH_PERSONAL_ACCOUNT_FORM = By.XPATH, ".//main[contains(@class,'App_componentContainer')]"
#Кнопка "Конструктор" в шапке страницы
    SEARCH_CONSTRUCTOR_BUTTON = By.LINK_TEXT, "Конструктор"
#Содержимое конструктора
    SEARCH_CONSTRUCTOR_FORM = By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2"
#Заголовок конструктора
    SEARCH_CONSTRUCTOR_HEADER = By.XPATH, ".//h1[@class = 'text text_type_main-large mb-5 mt-10']"
#Логотип в шапке страницы
    SEARCH_LOGO = By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2"
#Кнопка "Выход" в личном кабинете
    SEARCH_EXIT_BUTTON = By.XPATH, ".//button[text()='Выход']"
#В конструкторе вкладка "Начинки"
    SEARCH_CONSTRUCTOR_STUFFING = By.XPATH, ".//span[text()='Начинки']"
#В конструкторе родительский класс вкладки "Начинки"
    SEARCH_CONSTRUCTOR_STUFFING_PAR = By.XPATH, ".//span[text()='Начинки']/parent::div"
#В конструкторе заголовок "Начинки"
    SEARCH_HEADER_STUFFING = By.XPATH, ".//h2[text()='Начинки']"
#В конструкторе подсветка выбранной секции
    SEARCH_CURRENT_SEC_IN_CONSTRUCT = By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span"
#В конструкторе вкладка "Соусы"
    SEARCH_CONSTRUCTOR_SAUCES = By.XPATH, ".//span[text()='Соусы']"
#В конструкторе родительский класс вкладки "Соусы"
    SEARCH_CONSTRUCTOR_SAUCES_PAR = By.XPATH, ".//span[text()='Соусы']/parent::div"
#В конструкторе заголовок "Соусы"
    SEARCH_HEADER_SAUCES = By.XPATH, ".//h2[text()='Соусы']"
#В конструкторе вкладка "Булки"
    SEARCH_CONSTRUCTOR_BUNS = By.XPATH, ".//span[text()='Булки']"
#В конструкторе родительский класс вкладки "Булки"
    SEARCH_CONSTRUCTOR_BUNS_PAR = By.XPATH, ".//span[text()='Булки']/parent::div"
#В конструкторе заголовок "Булки"
    SEARCH_HEADER_BUNS = By.XPATH, ".//h2[text()='Булки']"
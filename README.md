<h2>Sprint_5</h2>
<h3>Автотесты, реализованные для сайта Stellar Burgers</h3>

<h4>test_registration.py - тесты для проверки регистрации на сайте</h4>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_registration_add_new_user</td>
      <td>Проверка успешной регистрации на сайте</td>
    </tr>
    <tr>
      <td>test_registration_not_correct_password</td>
      <td>Проверка неуспешной регистрации, вывода ошибки при вводе пароля длиной меньше 6 символов</td>
    </tr>
  </tbody>
</table>

<h4>test_log_in.py - тесты для проверки авторизации зарегистрированного пользователя на сайте</h4>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_login_in_main_page</td>
      <td>Проверка авторизации с главной страницы сайта по нажатию на "Войти в аккаунт"</td>
    </tr>
    <tr>
      <td>test_login_in_personal_account</td>
      <td>Проверка авторизации после перехода по ссылке "Личный кабинет"</td>
    </tr>
    <tr>
      <td>test_login_in_recover_password</td>
      <td>Проверка авторизации после перехода по ссылке "Восстановить пароль"</td>
    </tr>
    <tr>
      <td>test_login_in_registration_page</td>
      <td>Проверка авторизации через форму регистрации по нажатию на "Войти"</td>
    </tr>
  </tbody>
</table>

<h4>test_transfer_in_personal_account.py - тесты для проверки перехода в личный кабинет</h4>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_transfer_in_personal_account_from_main_page</td>
      <td>Проверка перехода в личный кабинет через ссылку "Личный кабинет на главной странице</td>
    </tr>
  </tbody>
</table>

<h4>test_transfer_from_personal_account.py - тесты для проверки перехода по ссылкам из личного кабинета</h4>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_transfer_from_personal_account_to_constructor</td>
      <td>Проверка перехода из личного кабинета в конструктор по нажатию на кнопку "Конструктор"</td>
    </tr>
    <tr>
      <td>test_transfer_from_personal_account_to_logo</td>
      <td>Проверка перехода из личного кабинета на главную страницу сайта по нажатию на логотип</td>
    </tr>
  </tbody>
</table>

<h4>test_exit_from_account.py - тесты для проверки выхода пользователя в личном кабинете</h4>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_exit_from_personal_account</td>
      <td>Проверка выхода с сайта по нажатию "Выйти" в личном кабинете</td>
    </tr>
  </tbody>
</table>

<h4>test_change_section.py - тесты для проверки перехода по секциям в конструкторе</h4>
<table>
  <thead>
  </thead>
  <tbody>
    <tr>
      <td>test_change_section_to_stuffing</td>
      <td>Проверка перехода в секцию "Начинки" в конструкторе</td>
    </tr>
    <tr>
      <td>test_change_section_to_sauces</td>
      <td>Проверка перехода в секцию "Соусы" в конструкторе</td>
    </tr>
    <tr>
      <td>test_change_section_to_buns</td>
      <td>Проверка перехода в секцию "Соусы", затем в секцию "Булки" в конструкторе</td>
    </tr>
  </tbody>
</table>

Для работы необходимы библиотеки: </br>
<li>pytest</li>
<li>selenium</li>

Запуск тестов:  <b>pytest -v</b>

from selenium.webdriver.common.by import By

class MainPageLocators:
    main_form = (By.XPATH, ".//main[@class = 'App_componentContainer__2JC2W']")    #Форма главной страницы
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")    #Кнопка главной страницы
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")    #Кнопка Личный кабинет
    login_account_btn = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")    #Кнопка Войти в аккаунт
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")    #Кнопка Конструктор
    order_feed_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")    #Кнопка Лента заказов
    bun_btn = (By.XPATH, ".//span[text() = 'Булки']")    #Кнопка переключения на Булки
    sauces_btn = (By.XPATH, ".//span[text() = 'Соусы']")    #Кнопка переключения на Соусы
    toppings_btn = (By.XPATH, ".//span[text() = 'Начинки']")    #Кнопка переключения на Начинки
    place_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")    #Кнопка Оформить заказ
    bun = (By.XPATH, ".//h2[text() = 'Булки']")    #Текст Булки на главной странице
    bun_list = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[1]")    #Выбор булок на главной странице
    sauces = (By.XPATH, ".//h2[text() = 'Соусы']")    #Текст Соусы на главной странице
    sauces_list = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[2]")    #Выбор соусов на главной странице
    topping = (By.XPATH, ".//h2[text() = 'Начинки']")    #Текст Начинки на главной странице
    topping_list = (By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[3]")    #Выбор начинок на главной странице

class AuthPageLocators:
    auth_form = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")    #Форма авторизации
    email_input = (By.XPATH, ".//input[@name = 'name']")    #Поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")    #Поле ввода пароля
    login_account_btn = (By.XPATH, "//button[text() = 'Войти']")    #Кнопка Войти
    registration_btn = (By.XPATH, "//a[text() = 'Зарегистрироваться']")    #Кнопка Зарегистрироваться
    recover_btn = (By.XPATH, "//a[text() = 'Восстановить пароль']")    #Кнопка Восстановить пароль
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")    #Кнопка Конструктор
    order_feed_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")    #Кнопка Лента заказов
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")    #Кнопка главной страницы сайта
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")    #Кнопка Личный кабинет
    
class RegistrationPageLocators:
    name_input = (By.XPATH, "(.//input[@name = 'name'])[1]")    #Поле ввода имени
    email_input = (By.XPATH, "(.//input[@name = 'name'])[2]")    #Поле ввода email
    password_input = (By.XPATH, ".//input[@name = 'Пароль']")    #Поле ввода пароля
    registration_btn = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")    #Кнопка Зарегистрироваться
    login_account_btn = (By.XPATH, ".//a[text() = 'Войти']")    #Кнопка Войти
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")    #Кнопка Конструктор
    order_feed_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")    #Кнопка Лента заказов
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")    #Кнопка главной страницы сайта
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")    #Кнопка Личный кабинет
    error_message_double_reg = (By.XPATH, ".//p[text() = 'Такой пользователь уже существует']")    #Тескс ошибки при повторной регистрации существующего пользователя
    error_message_incorrect_password = (By.XPATH, ".//p[text() = 'Некорректный пароль']")    #Текст ошибки при вводе некорректного пароля

class RecoverPageLocators:
    email_input = (By.XPATH, ".//label[text() = 'Email']")    #Поле ввода email
    recover_btn = (By.XPATH, ".//button[text() = 'Восстановить']")    #Кнопка Восстановить
    login_account_btn = (By.XPATH, ".//a[text() = 'Войти']")    #Кнопка Войти
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")    #Кнопка Конструктор
    order_feed_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")    #Кнопка Лента заказов
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")    #Кнопка главной страницы сайта
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")    #Кнопка Личный кабинет

class PersonalAreaLocators:
    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")    #Форма личного кабинета
    profile_btn = (By.XPATH, ".//a[text() = 'Профиль']")    #Кнопка Профиль
    order_history_btn = (By.XPATH, ".//a[text() = 'История заказов']")    #Кнопка История заказов
    exit_btn = (By.XPATH, ".//button[text() = 'Выход']")    #Кнопка Выход
    save_btn = (By.XPATH, ".//button[text() = 'Сохранить']")    #Кнопка Сохранить
    cansel_btn = (By.XPATH, ".//button[text() = 'Отмена']")    #Кнопка Отмена
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")    #Кнопка Конструктор
    order_feed_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")    #Кнопка Лента заказов
    logo_btn = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")    #Кнопка главной страницы сайта
    personal_account_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")    #Кнопка Личный кабинет
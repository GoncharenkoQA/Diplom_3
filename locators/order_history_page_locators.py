from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    # Карточка заказа
    order_card = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
    # Заголовок карточки с названием
    order_card_title = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')
    # Номер заказа в карточке
    order_card_id = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]')
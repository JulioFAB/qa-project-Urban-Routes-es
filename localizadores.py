from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    mode_button = (By.CSS_SELECTOR, '.modes-container')
    pedir_un_taxi = (By.CLASS_NAME, 'button.round')
    tariff_picker = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]')
    tarifa_confort = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    numero_de_telefono = (By.CLASS_NAME, "np-button")
    campo_introduce_numero_telefono = (By.ID, 'phone')
    boton_siguiente_introduce_numero_telefono = (By.CLASS_NAME, 'button full')
    codigo_sms = (By.ID, 'code')
    confirmar_sms = (By.CLASS_NAME, 'button full')
    metodo_de_pago = (By.CLASS_NAME, 'pp-button filled')
    agregar_tarjeta = (By.CLASS_NAME, 'pp-plus-container')
    numero_de_tarjeta = (By.CLASS_NAME, 'card-number-input')
    codigo_de_tarjeta = (By.CLASS_NAME, 'card-code-input')
    card_space = (By.CSS_SELECTOR, '.plc')
    agregar = (By.CLASS_NAME, 'button full')
    cerrar_ventana_metodo_pago = (By.CLASS_NAME, 'close-button section-close')
    mensaje_para_conductor = (By.ID, 'comment')
    requisitos_del_pedido = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[1]')
    manta_panuelos = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]')
    helado = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    reservar = (By.CLASS_NAME, 'smart-button-wrapper')












import main
from selenium.webdriver.common.keys import Keys
import data
import localizadores
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Metodos
class UrbanRoutesPage:

    def __init__(self, driver):

        self.driver = driver
        self.from_field = localizadores.UrbanRoutesPage.from_field
        self.to_field = localizadores.UrbanRoutesPage.to_field
        self.clic_boton_pedir_taxi = localizadores.UrbanRoutesPage.pedir_un_taxi
        self.clic_tarifa_confort = localizadores.UrbanRoutesPage.tarifa_confort
        self.clic_numero_telefono = localizadores.UrbanRoutesPage.numero_de_telefono
        self.campo_introduce_numero_telefono = localizadores.UrbanRoutesPage.campo_introduce_numero_telefono
        self.clic_siguiente_numero_de_telefono_ventana = localizadores.UrbanRoutesPage.boton_siguiente_introduce_numero_telefono
        self.codigo_sms = localizadores.UrbanRoutesPage.codigo_sms
        self.clic_boton_confirmar = localizadores.UrbanRoutesPage.confirmar_sms
        self.clic_boton_metodo_de_pago = localizadores.UrbanRoutesPage.metodo_de_pago
        self.clic_agregar_tarjeta = localizadores.UrbanRoutesPage.agregar_tarjeta
        self.numero_de_tarjeta = localizadores.UrbanRoutesPage.numero_de_tarjeta
        self.codigo_de_tarjeta = localizadores.UrbanRoutesPage.codigo_de_tarjeta
        self.agregar = localizadores.UrbanRoutesPage.agregar
        self.mensaje_al_conductor = localizadores.UrbanRoutesPage.mensaje_para_conductor
        self.manta_panuelos = localizadores.UrbanRoutesPage.manta_panuelos
        self.helado = localizadores.UrbanRoutesPage.helado
        self.reservar = localizadores.UrbanRoutesPage.reservar


    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def hacer_clic_pedir_taxi(self): WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.clic_boton_pedir_taxi)).click()

    def llenar_desde_hasta(self):
        self.set_from(data.address_from)
        self.set_to(data.address_to)


    def insert_phone_number(self):
        phone_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.campo_introduce_numero_telefono))
        phone_field.click()
        phone_field.send_keys(data.phone_number)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.clic_siguiente_numero_de_telefono_ventana)
        ).click()

    def select_tarifa_confort(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.clic_tarifa_confort)).click()

    def agregar_tarjeta(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.clic_boton_metodo_de_pago)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.clic_agregar_tarjeta)
        ).click()

        numero_tarjeta_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.numero_de_tarjeta)
        )
        numero_tarjeta_field.send_keys(data.card_number)

        codigo_tarjeta_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.codigo_de_tarjeta)
        )
        codigo_tarjeta_field.send_keys(data.card_code)
        codigo_tarjeta_field.send_keys(Keys.TAB)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.agregar)
        ).click()

    def confirmar_codigo_sms(self):
        code = main.retrieve_phone_code(self.driver)  # Usando la función proporcionada
        self.driver.find_element(*self.codigo_sms).send_keys(code)
        self.driver.find_element(*self.clic_boton_confirmar).click()

    def enviar_mensaje_al_conductor(self):
        self.driver.find_element(*self.mensaje_al_conductor).send_keys(data.message_for_driver)


    def pedir_manta_panuelos(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.manta_panuelos)
        ).click()

    def pedir_helado(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.helado)).click()

    def confirmar_reserva(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.reservar)).click()

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)


    #ASSERT

    def tarifa_seleccionada(self):
        # Devuelve el texto o valor que indica la tarifa seleccionada.
        return self.driver.find_element(*self.clic_tarifa_confort).text

    def obtener_numero_telefono(self):
        # Devuelve el número de teléfono actualmente ingresado.
        return self.driver.find_element(*self.campo_introduce_numero_telefono).get_property('value')

    def tarjeta_agregada_exitosamente(self):
        # Lógica para verificar si la tarjeta fue agregada correctamente.
        return "Tarjeta agregada" in self.driver.page_source

    def obtener_mensaje_enviado(self):
        # Devuelve el mensaje enviado al conductor.
        return self.driver.find_element(*self.mensaje_al_conductor).get_property('value')

    def manta_panuelos_seleccionados(self):
        # Verifica que la opción de manta y pañuelos fue seleccionada.
        return self.driver.find_element(*self.manta_panuelos).is_selected()

    def helado_pedido(self):
        # Verifica que el helado fue pedido correctamente.
        return self.driver.find_element(*self.helado).is_selected()

    def reserva_confirmada(self):
        # Verifica que la reserva fue confirmada correctamente.
        return "Reserva confirmada" in self.driver.page_source













































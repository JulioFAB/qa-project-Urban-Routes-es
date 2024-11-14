import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import metodos
from metodos import UrbanRoutesPage

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # No modificar, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to
        self.routes_page.hacer_clic_pedir_taxi()

    def test_seleccionar_tarifa_confort(self):
        self.routes_page.select_tarifa_confort()

    def test_insertar_numero_telefono(self):
        self.routes_page.insert_phone_number()


    def test_agregar_tarjeta(self):
        self.routes_page.agregar_tarjeta()
        self.routes_page.codigo_de_tarjeta()



    def test_enviar_mensaje_conductor(self):
        self.routes_page.enviar_mensaje_al_conductor()

    def test_pedir_manta_panuelos(cls):      #cambie self por cls
        agregar_manta_panuelos = metodos.UrbanRoutesPage(cls.driver)
        agregar_manta_panuelos.pedir_manta_panuelos()

         #self.routes_page.pedir_manta_panuelos()

    def test_pedir_helado(self):
        self.routes_page.pedir_helado()

    def test_confirmar_reserva(self):
        self.routes_page.confirmar_reserva()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


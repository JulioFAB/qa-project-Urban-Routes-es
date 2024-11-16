# NOMBRE DEL PROYECTO: qa-project-Urban-Routes-es


# PRUEBAS AUTOMATIZADAS DEL PROCESO DE SOLICITAR UN TAXI EN LA APLICACION URBAN ROUTES

Se realizaron 8 pruebas para todo el proceso de solicitar un taxi en la aplicacion, incluyendo detalles de viaje. Las pruebas abarcan:
- Llenado de campos
- Click en botones 
- Eleccion de opciones

## Instalación

Para instalar las librerías necesarias, asegúrate de tener Python. Ejecuta los siguientes comando en tu terminal: 
- pip install pytest
- pip install requests

Ademas deben instalar SELENIUM el cual se puede instalar desde el python packeges
- De selenium se utiliza webdriver la cual funciona para controlar el navegador. Se importa con el comando "from selenium import webdriver"
- Se utiliza import By que nos permite interactuar con el DOM
- Se utiliza para las esperas "import WebDriverWait" que nos da el tiempo de espera para realizar acciones 



Para ejecutar las pruebas se necesita abrir el archivo main.py y actualizar la URL en el archivo data.py
Puedes ejecutar las pruebas desde la terminal con el comando:
- pytest main.py
- o dando clic en el boton run python test 

 Sprint 8 
grupo 14
 Julio Fernando Aguilar Becerra  
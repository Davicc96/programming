# Definición de la clase PC
class PC:
    """
    Clase que representa el ordenador portátil.
    """

    def __init__(self, marca: str, modelo: str, procesador: int, memoria_ram: int, almacenamiento: int):


        """
        Constructor para inicializar los atributos del ordenador.(PARAMETRIZADO)

        :parametro marca: Marca del PC
        :parametro modelo: Modelo del PC
        :parametro procesador: Velocidad del procesador en GHz (entero)
        :parametro memoria_ram: Memoria RAM en GB
        :parametro almacenamiento: Capacidad de almacenamiento en GB
        """
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.memoria_ram = memoria_ram
        self.almacenamiento = almacenamiento

    def install_app(self, app: str):
        """
        Simula la instalación de una aplicación en el PC.

        :param app: Nombre de la aplicación a instalar
        """
        print(f"Instalando la aplicación '{app}' en {self.marca} {self.modelo}...")

# ---------------------------
# Creación de instancias
# ---------------------------

# PC 1
pc1 = PC("Lenovo", "ThinkPad X1", 5, 16, 512)
pc1.install_app("Visual Studio Code")

# PC 2
pc2 = PC("HP", "Probook", 4, 8, 256)
pc2.install_app("Google Chrome")

# PC 3
pc3 = PC("Apple", "MacBook Pro", 6, 32, 1024)
pc3.install_app("Xcode")

class Usuario:
    __email = 'rafaelosnayo@hotmail.com'
    __password = 'qwerty123'

    def __init__(self):
        pass # se pone para finalizar ya que no tiene contenido, si no muestra error

    def login(self,email,password):
        if email == self.__email and password == self.__password:
            print('Bienvenido' + self.__email)
        else:
            print("Error en el inicio de sesión")

print('LOGIN DE USUARIOS')
email = input("Ingrese email: ")
pwd = input("Ingrese Password: ")

usuario = Usuario()
usuario.login(email, pwd)
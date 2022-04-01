# Prueba de clase de metodos estaticos

class MEstaticos:
    @staticmethod
    def func1():
        print("func1()")
    @staticmethod
    def func2(x, y):
        print("Funcion '{}' incvocada. \nParametros=({}, {})".format("func2", x, y))
    @staticmethod
    def func3(a, b, c):
        info = """
        Nombre de la funcion: {nombre}
        Cantidad de Args: {cantidad} 
        Args: {args}
        """
        info = info.format(
            nombre=MEstaticos.func3.__name__,
            cantidad=MEstaticos.func3.__code__.co_argcount,
            args=MEstaticos.func3.__code__.co_varnames
        )
        print(info)
    # Estas lineas son en vez de los decorators
    #func1 = staticmethod(func1)
    #func2 = staticmethod(func2)
    #func3 = staticmethod(func3)

me = MEstaticos()
me.func1()
#Con la sig linea se muestra ejecutar Metodo Estatico desde Obl Class
#MEstaticos.func1()

me.func2(100, 200)
me.func3(5, 10, 15)
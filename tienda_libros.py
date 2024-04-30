class LibroError(Exception):
    pass

class LibroExistenteError(LibroError):
    def __init__(self, titulo, isbn):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn: {self.isbn} ya existe en el catálogo"

class LibroAgotadoError(LibroError):
    def __init__(self, titulo, isbn):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn {self.isbn} esta agotado"

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, titulo, isbn, cantidad_a_comprar, existencias):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias = existencias

    def __str__(self):
        return f"El libro con titulo {self.titulo} y isbn {self.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.existencias}"

class Libro:
    def __init__(self, isbn, titulo, precio, existencias):
        self.isbn = isbn
        self.titulo = titulo
        self.precio = precio
        self.existencias = existencias

class CarroCompras:
    def __init__(self):
        self.items = {}

    def quitar_item(self, isbn):
        del self.items[isbn]

class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catalogo:
            raise LibroExistenteError(titulo, isbn)
        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro

    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)
        if libro.existencias < cantidad:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn, cantidad, libro.existencias)
        self.carrito.items[libro.isbn] = cantidad

    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)

class UIConsola:
    def __init__(self, tienda_libros):
        self.tienda_libros = tienda_libros

    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el isbn del libro que se va a retirar del carrito: ")
        self.tienda_libros.retirar_item_de_carrito(isbn)
        print("Libro retirado del carrito con éxito")

    def agregar_libro_a_carrito_de_compras(self):
        isbn = input("Ingrese el isbn del libro que va a agregar: ")
        cantidad = int(input("Ingrese la cantidad de unidades del libro: "))
        libro = self.tienda_libros.catalogo[isbn]
        self.tienda_libros.agregar_libro_a_carrito(libro, cantidad)

    def adicionar_un_libro_a_catalogo(self):
        isbn = input("Ingrese el ISBN del libro: ")
        titulo = input("Ingrese el título del libro: ")
        precio = float(input("Ingrese el precio del libro: "))
        existencias = int(input("Ingrese las existencias del libro: "))
        self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)




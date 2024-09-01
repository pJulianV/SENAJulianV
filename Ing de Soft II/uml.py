# Clases en python

class Usuario:
    def __init__(self, nombre, correo, contraseña):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

    def registrarse(self):
        print(f'Usuario {self.nombre} registrado con el correo {self.correo}.')

    def iniciarSesion(self):
        print(f'Usuario {self.nombre} ha iniciado sesión.')


class Producto:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def agregarAlCarrito(self):
        print(f'Producto {self.nombre} agregado al carrito.')

    def actualizarStock(self, cantidad):
        print(f'Stock de {self.nombre} actualizado en {cantidad}.')


class Carrito:
    def __init__(self):
        self.listaProductos = []
        self.total = 0.0

    def añadirProducto(self, producto):
        self.listaProductos.append(producto)
        self.total += producto.precio
        print(f'Producto {producto.nombre} añadido al carrito. Total actual: {self.total}.')

    def eliminarProducto(self, producto):
        self.listaProductos.remove(producto)
        self.total -= producto.precio
        print(f'Producto {producto.nombre} eliminado del carrito. Total actual: {self.total}.')


class Pedido:
    def __init__(self, numeroPedido, fecha, estado):
        self.numeroPedido = numeroPedido
        self.fecha = fecha
        self.estado = estado

    def realizarPedido(self):
        print(f'Pedido {self.numeroPedido} realizado con estado {self.estado}.')

    def cancelarPedido(self):
        print(f'Pedido {self.numeroPedido} cancelado.')


class Proveedor:
    def __init__(self, nombre, contacto):
        self.nombre = nombre
        self.contacto = contacto
        self.listaProductos = []

    def enviarProducto(self, producto):
        print(f'Proveedor {self.nombre} ha enviado el producto {producto.nombre}.')

    def actualizarInventario(self):
        print(f'Inventario de {self.nombre} actualizado.')


class Administrador(Usuario):
    def gestionarUsuarios(self):
        print('Gestión de usuarios.')

    def gestionarProductos(self):
        print('Gestión de productos.')

    def verReportes(self):
        print('Visualizando reportes.')


class Plataforma:
    def registrarUsuario(self, usuario):
        usuario.registrarse()

    def procesarPago(self, pedido):
        print(f'Pago procesado para el pedido {pedido.numeroPedido}.')


class InterfazUsuario:
    def mostrarProductos(self):
        print('Mostrando productos.')

    def mostrarCarrito(self):
        print('Mostrando carrito.')


class HerramientasCASE:
    def analizarSistema(self):
        print('Analizando sistema.')

    def documentar(self):
        print('Documentando.')

    def probarSoftware(self):
        print('Probando software.')




# Diagrama de actividades en python



# Proceso de Registro de Usuario
def proceso_registro(usuario):
    print('Inicio del proceso de registro.')
    print('El usuario ingresa su nombre, correo y contraseña.')
    datos_validos = True  # Cambiar a False para simular un error
    if datos_validos:
        usuario.registrarse()
    else:
        print('Error: datos inválidos. Solicitar ingreso nuevamente.')

# Proceso de Agregar Producto al Carrito
def agregar_producto_al_carrito(carrito, producto):
    print('Inicio del proceso de agregar producto al carrito.')
    print('El usuario selecciona un producto.')
    producto.actualizarStock(10)  # Ejemplo de stock disponible
    stock_disponible = True  # Cambiar a False para simular producto no disponible
    if stock_disponible:
        carrito.añadirProducto(producto)
    else:
        print('Producto no disponible.')

# Proceso de Realizar Pedido
def realizar_pedido(carrito):
    print('Inicio del proceso de realizar pedido.')
    print('El usuario revisa los productos en su carrito.')
    print('El usuario confirma el pedido.')
    pedido = Pedido(1, '2024-08-27', 'pendiente')
    pedido.realizarPedido()
    plataforma = Plataforma()
    plataforma.procesarPago(pedido)
    proveedor = Proveedor('Proveedor 1', 'contacto@proveedor.com')
    for producto in carrito.listaProductos:
        proveedor.enviarProducto(producto)

# Proceso de Gestión de Productos por el Administrador
def gestionar_productos(admin):
    print('Inicio del proceso de gestión de productos.')
    admin.gestionarProductos()
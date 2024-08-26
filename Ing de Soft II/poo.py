class Usuario:
    def __init__(self, id_usuario, nombre, email, contraseña, tipo_usuario):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        self.tipo_usuario = tipo_usuario  # Puede ser 'comprador', 'vendedor' o ambos

    def iniciar_sesion(self, email, contraseña):
        # Lógica para iniciar sesión
        pass

    def registrar(self):
        # Lógica para registrar un nuevo usuario
        pass

    def actualizar_perfil(self, nombre, email):
        # Lógica para actualizar el perfil del usuario
        pass


class Producto:
    def __init__(self, id_producto, nombre, descripción, precio, cantidad, categoría, vendedor):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripción
        self.precio = precio
        self.cantidad = cantidad
        self.categoría = categoría
        self.vendedor = vendedor  # Referencia a un objeto Usuario

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def mostrar_detalles(self):
        # Lógica para mostrar los detalles del producto
        pass



class Transacción:
    def __init__(self, id_transacción, comprador, vendedor, producto, cantidad, fecha, estado):
        self.id_transacción = id_transacción
        self.comprador = comprador  # Referencia a un objeto Usuario
        self.vendedor = vendedor  # Referencia a un objeto Usuario
        self.producto = producto  # Referencia a un objeto Producto
        self.cantidad = cantidad
        self.fecha = fecha
        self.estado = estado  # Puede ser 'pendiente', 'completado', 'cancelado'

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_información(self):
        # Lógica para mostrar la información de la transacción
        pass



class Categoría:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

    def agregar_producto(self, producto):
        # Lógica para agregar un producto a esta categoría
        pass

    def eliminar_producto(self, producto):
        # Lógica para eliminar un producto de esta categoría
        pass


class Comentario:
    def __init__(self, id_comentario, autor, contenido, fecha):
        self.id_comentario = id_comentario
        self.autor = autor  # Referencia a un objeto Usuario
        self.contenido = contenido
        self.fecha = fecha

    def mostrar_comentario(self):
        # Lógica para mostrar el comentario
        pass

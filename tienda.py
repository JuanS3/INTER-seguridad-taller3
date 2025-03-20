import os
import json
from datetime import datetime

class SistemaProductos:
    """
    Una clase que maneja todas las operaciones del sistema de productos.
    """
    def __init__(self):
        self.archivo_productos = "productos.txt"
        self.archivo_ventas = "ventas.txt"

    def ejecutar(self):
        """Método principal que ejecuta toda la aplicación."""
        while True:
            print("\n===== SISTEMA DE REGISTRO DE PRODUCTOS =====")
            print("1. Registrar producto")
            print("2. Consultar productos")
            print("3. Actualizar producto")
            print("4. Eliminar producto")
            print("5. Registrar venta")
            print("6. Generar reporte de ventas")
            print("7. Salir")

            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                self.registrar_producto()
            elif opcion == '2':
                self.consultar_productos()
            elif opcion == '3':
                self.actualizar_producto()
            elif opcion == '4':
                self.eliminar_producto()
            elif opcion == '5':
                self.registrar_venta()
            elif opcion == '6':
                self.generar_reporte()
            elif opcion == '7':
                print("¡Gracias por usar el sistema!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def registrar_producto(self):
        """Registra un nuevo producto en el archivo."""
        # Viola SRP: Mezcla la entrada/salida con lógica de negocio
        print("\n--- REGISTRO DE PRODUCTO ---")

        id = input("ID del producto: ")
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        categoria = input("Categoría del producto: ")
        stock = int(input("Stock del producto: "))

        # Viola SRP: Maneja directamente la persistencia
        productos = self.cargar_productos()

        # Verificar si el producto ya existe
        for producto in productos:
            if producto['id'] == id:
                print("ERROR: Ya existe un producto con ese ID.")
                return

        nuevo_producto = {
            'id': id,
            'nombre': nombre,
            'precio': precio,
            'categoria': categoria,
            'stock': stock
        }

        productos.append(nuevo_producto)
        self.guardar_productos(productos)
        print(f"Producto '{nombre}' registrado exitosamente.")

    def consultar_productos(self):
        print("\n--- LISTADO DE PRODUCTOS ---")
        productos = self.cargar_productos()

        if not productos:
            print("No hay productos registrados.")
            return

        print(f"{'ID':<10} {'Nombre':<20} {'Precio':<10} {'Categoría':<15} {'Stock':<10}")
        print("-" * 65)

        for producto in productos:
            print(f"{producto['id']:<10} {producto['nombre']:<20} {producto['precio']:<10.2f} {producto['categoria']:<15} {producto['stock']:<10}")

    def actualizar_producto(self):
        print("\n--- ACTUALIZACIÓN DE PRODUCTO ---")
        id = input("ID del producto a actualizar: ")

        productos = self.cargar_productos()

        # Buscar el producto
        for i, producto in enumerate(productos):
            if producto['id'] == id:
                print(f"Producto encontrado: {producto['nombre']}")

                nombre = input("Nuevo nombre (Enter para mantener): ")
                precio_str = input("Nuevo precio (Enter para mantener): ")
                categoria = input("Nueva categoría (Enter para mantener): ")
                stock_str = input("Nuevo stock (Enter para mantener): ")

                if nombre:
                    producto['nombre'] = nombre
                if precio_str:
                    producto['precio'] = float(precio_str)
                if categoria:
                    producto['categoria'] = categoria
                if stock_str:
                    producto['stock'] = int(stock_str)

                self.guardar_productos(productos)
                print("Producto actualizado exitosamente.")
                return

        print("ERROR: No se encontró un producto con ese ID.")

    def eliminar_producto(self):
        print("\n--- ELIMINACIÓN DE PRODUCTO ---")
        id = input("ID del producto a eliminar: ")

        productos = self.cargar_productos()

        # Buscar el producto
        for i, producto in enumerate(productos):
            if producto['id'] == id:
                productos.pop(i)
                self.guardar_productos(productos)
                print(f"Producto eliminado exitosamente.")
                return

        print("ERROR: No se encontró un producto con ese ID.")

    def registrar_venta(self):
        """Registra una venta de producto."""
        # Viola SRP: Mezcla lógica de ventas con productos
        print("\n--- REGISTRO DE VENTA ---")

        producto_id = input("ID del producto vendido: ")
        cantidad = int(input("Cantidad vendida: "))

        # Verificar si el producto existe y hay stock
        productos = self.cargar_productos()
        producto_encontrado = False

        for i, producto in enumerate(productos):
            if producto['id'] == producto_id:
                if producto['stock'] >= cantidad:
                    producto['stock'] -= cantidad
                    producto_encontrado = True

                    # Registro de venta
                    ventas = self.cargar_ventas()
                    nueva_venta = {
                        'producto_id': producto_id,
                        'cantidad': cantidad,
                        'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'total': producto['precio'] * cantidad
                    }
                    ventas.append(nueva_venta)

                    self.guardar_productos(productos)
                    self.guardar_ventas(ventas)

                    print(f"Venta registrada exitosamente. Total: ${nueva_venta['total']:.2f}")
                else:
                    print(f"ERROR: Stock insuficiente. Stock actual: {producto['stock']}")
                break

        if not producto_encontrado:
            print("ERROR: No se encontró un producto con ese ID.")

    def generar_reporte(self):
        """Genera un reporte de ventas."""
        # Viola SRP: Mezcla lógica de reportes con el sistema de productos
        print("\n--- REPORTE DE VENTAS ---")
        ventas = self.cargar_ventas()

        if not ventas:
            print("No hay ventas registradas.")
            return

        print(f"{'Producto ID':<15} {'Cantidad':<10} {'Fecha':<20} {'Total':<10}")
        print("-" * 55)

        total_ventas = 0
        for venta in ventas:
            print(f"{venta['producto_id']:<15} {venta['cantidad']:<10} {venta['fecha']:<20} ${venta['total']:<10.2f}")
            total_ventas += venta['total']

        print("-" * 55)
        print(f"TOTAL VENTAS: ${total_ventas:.2f}")

    # Viola OCP y SRP: Métodos de persistencia mezclados con lógica de negocio
    def cargar_productos(self):
        """Carga los productos desde el archivo."""
        if not os.path.exists(self.archivo_productos):
            return []

        try:
            with open(self.archivo_productos, 'r') as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            print("Error al leer el archivo de productos.")
            return []

    def guardar_productos(self, productos):
        """Guarda los productos en el archivo."""
        with open(self.archivo_productos, 'w') as archivo:
            json.dump(productos, archivo, indent=4)

    def cargar_ventas(self):
        """Carga las ventas desde el archivo."""
        if not os.path.exists(self.archivo_ventas):
            return []

        try:
            with open(self.archivo_ventas, 'r') as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            print("Error al leer el archivo de ventas.")
            return []

    def guardar_ventas(self, ventas):
        """Guarda las ventas en el archivo."""
        with open(self.archivo_ventas, 'w') as archivo:
            json.dump(ventas, archivo, indent=4)


# Viola LSP: Clase derivada que no es sustituible por la clase base
class ProductoEspecial:
    """
    Clase que representa un tipo especial de producto pero no puede
    ser utilizada como un producto normal.
    """
    def __init__(self, id, nombre, precio, categoria, stock, descuento):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.descuento = descuento

    # Viola LSP: Comportamiento incompatible con la clase base
    def calcular_precio_final(self):
        # Los productos especiales calculan su precio diferente
        return self.precio * (1 - self.descuento)

    # Viola LSP: Método que no existe en la clase base
    def aplicar_descuento(self, porcentaje):
        self.descuento = porcentaje


# Punto de entrada del programa
if __name__ == "__main__":
    sistema = SistemaProductos()
    sistema.ejecutar()

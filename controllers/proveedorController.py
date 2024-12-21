from flask import jsonify
from models.services.proveedorServices import ProveedorServices



class ProveedorController:
    @staticmethod
    def agregar_proveedor(data):
        try:
           # Obtener los datos del cuerpo de la solicitud
            # Validación de los campos obligatorios
            if not data or 'nombre' not in data or 'telefono' not in data or 'email' not in data or 'direccion' not in data:
                return jsonify({'error': 'Datos incompletos'}), 400
            # Llamar al servicio para agregar el nuevo proveedor
            nuevo_proveedor = ProveedorServices.agregar_proveedor(
                data['nombre'],           # Extraemos los datos correctamente
                data['telefono'],
                data['email'],
                data['direccion']
            )
            return jsonify(nuevo_proveedor.serialize()), 201  # Retornar el proveedor agregado en formato JSON
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def actualizar_proveedor(id_proveedor):
        try:
           nombre = data.get('nombre')
           telefono = data.get('telefono')
           email = data.get('email')
           direccion = data.get('direccion') 

           proveedor_actualizado = ProveedorServices.actualizar_proveedor(id_proveedor, nombre = nombre, telefono= telefono, email = email, direccion = direccion)

           if proveedor_actualizado is None:
               return jsonify({'error': 'Proveedor no encontrado'}), 404
            else:
                return jsonify(proveedor_actualizado.serialize()), 200
                
           

    @staticmethod
    def eliminar_proveedor(id_proveedor):
        try:
            # Llamar al servicio para eliminar el proveedor
            proveedor_eliminado = ProveedorServices.eliminar_proveedor(id_proveedor)

            # Si no se encuentra el proveedor, retornamos un error
            if not proveedor_eliminado:
                return jsonify({'error': 'Proveedor no encontrado'}), 404

            return jsonify({'message': 'Proveedor eliminado exitosamente'}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def obtener_proveedor(id_proveedor):
        try:
            # Llamar al servicio para obtener un proveedor por ID
            proveedor = ProveedorServices.obtener_proveedor(id_proveedor)

            # Si no se encuentra el proveedor, retornamos un error
            if not proveedor:
                return jsonify({'error': 'Proveedor no encontrado'}), 404

            return jsonify(proveedor.serialize()), 200  # Retornar el proveedor encontrado

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def obtener_todos_proveedores():
        try:
            # Llamar al servicio para obtener todos los proveedores
            proveedores = ProveedorServices.obtener_todos_proveedores()

            return jsonify([proveedor.serialize() for proveedor in proveedores]), 200  # Retornar todos los proveedores

        except Exception as e:
            return jsonify({'error': str(e)}), 500
# Agenda de Contactos en Python

## Descripción
Este proyecto es una aplicación sencilla de agenda de contactos escrita en Python. Permite a los usuarios gestionar su lista de contactos mediante operaciones básicas como agregar, eliminar, buscar y mostrar todos los contactos. El objetivo de este proyecto es practicar el uso de estructuras de datos y manejo de archivos en Python.

## Funciones
- **Agregar Contacto:** Agrega un nuevo contacto a la agenda.
- **Eliminar Contacto:** Elimina un contacto existente por nombre.
- **Buscar Contacto:** Busca un contacto por nombre.
- **Mostrar Todos los Contactos:** Muestra todos los contactos almacenados en la agenda.

## Cómo Ejecutar
1. Asegúrate de tener Python 3 instalado en tu computadora.
2. Descarga o clona este repositorio en tu máquina local.
3. Abre una terminal o línea de comandos y navega hasta el directorio del proyecto.
4. Ejecuta el programa con el siguiente comando:
   ```bash
   main.py
   ```

## Uso
1. Al ejecutar el programa, verás un menú con las opciones disponibles:
   ```
   Agenda de Contactos
   1. Agregar Contacto
   2. Eliminar Contacto
   3. Buscar Contacto
   4. Mostrar Todos los Contactos
   5. Salir
   ```
2. Elige una opción ingresando el número correspondiente.
3. Sigue las instrucciones para realizar la acción deseada.

## Ejemplo
**Agregar un Contacto:**
```
Ingresa el nombre del contacto: Juan Pérez
Ingresa el número de teléfono del contacto: 123-456-7890
¡Contacto agregado con éxito!
```

**Buscar un Contacto:**
```
Ingresa el nombre a buscar: Juan Pérez
Contacto encontrado: Nombre: Juan Pérez, Teléfono: 123-456-7890
```

**Eliminar un Contacto:**
```
Ingresa el nombre a eliminar: Juan Pérez
¡Contacto eliminado con éxito!
```

**Mostrar Todos los Contactos:**
```
Contactos:
1. Nombre: Alicia Gómez, Teléfono: 987-654-3210
2. Nombre: Roberto Sánchez, Teléfono: 456-789-0123
```

## Estructura de Archivos
- `contact_agenda.py`: El script principal de Python que contiene la funcionalidad de la agenda.

## Mejoras Futuras
- Añadir la funcionalidad para actualizar contactos existentes.
- Guardar los contactos en un archivo para que los datos persistan entre ejecuciones del programa.
- Implementar una interfaz gráfica de usuario (GUI) usando una biblioteca como Tkinter o PyQt.

## Autor
Creado por ulises onofre.


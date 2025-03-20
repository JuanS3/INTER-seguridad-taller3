# Taller de Refactorización: Aplicando Principios SOLID

Este taller tiene como objetivo practicar la refactorización de código aplicando los principios SOLID y mejorando la calidad del código mediante herramientas de análisis estático.
El código proporcionado es un sistema simple de registro de productos para una tienda que utiliza archivos de texto como base de datos. Sin embargo, este código viola intencionalmente varios principios SOLID, lo que lo hace difícil de mantener, extender y probar.

## Objetivos del Taller

1. Identificar las violaciones a los principios SOLID en el código base
2. Refactorizar el código para que cumpla con:

    * SRP (Principio de Responsabilidad Única)
    * OCP (Principio Abierto/Cerrado)
    * LSP (Principio de Sustitución de Liskov)

3. Utilizar Ruff como linter para validar la calidad del código
4. Mejorar la estructura general y las prácticas de programación

## Instalación de Dependencias

Para instalar Ruff, ejecutar:

```bash
pip install ruff
```

## Estructura del Proyecto Actual

* `tienda.py`: Archivo principal con el código a refactorizar
* `productos.txt`: Archivo de texto que almacena los productos (se crea automáticamente)
* `ventas.txt`: Archivo de texto que almacena las ventas (se crea automáticamente)

## Problemas Identificados

El código actual tiene los siguientes problemas:

1. **Violaciones de SRP**:

    * La clase SistemaProductos maneja múltiples responsabilidades
    * Mezcla interfaz de usuario, lógica de negocio y persistencia

2. **Violaciones de OCP**:

    * No hay abstracciones para permitir extensiones sin modificar el código existente
    * La persistencia está fuertemente acoplada a la implementación

3. **Violaciones de LSP**:

    * La clase ProductoEspecial no puede ser utilizada como sustituto de un producto normal
    * Comportamientos incompatibles entre clases

## Actividades del Taller

1. **Análisis**: Identifica todas las violaciones a los principios SOLID en el código.
2. **Diseño**: Crea un diagrama de clases que represente tu solución refactorizada.
3. **Refactorización**: Modifica el código para seguir los principios SOLID.

    * Separa responsabilidades en clases distintas
    * Crea interfaces/clases abstractas para permitir extensiones
    * Asegura que las clases derivadas cumplan con LSP

4. **Validación con Ruff**: Configura y utiliza Ruff para validar que tu código cumple con los estándares de Python.

## Criterios de Evaluación

1. Correcta aplicación de los principios SOLID:

    * **SRP**: Cada clase tiene una única responsabilidad
    * **OCP**: El sistema puede extenderse sin modificar código existente
    * **LSP**: Las clases derivadas pueden sustituir a sus clases base

2. Calidad del código:

    * El código pasa todas las validaciones de Ruff
    * Nombres descriptivos y consistentes
    * Documentación adecuada (docstrings)
    * Manejo apropiado de errores


3. Funcionalidad:

    * El sistema mantiene todas las funcionalidades originales
    * La interfaz de usuario es amigable
    * Los datos se guardan y cargan correctamente

## Entregables

1. Código refactorizado que siga los principios SOLID
2. Informe que explique:

    * Violaciones identificadas en el código original
    * Cambios realizados y justificación
    * Cómo se han aplicado los principios SOLID
    * Capturas de pantalla mostrando los resultados de Ruff

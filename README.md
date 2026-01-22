Visualizador de Árboles AVL en Python

Este proyecto es una herramienta educativa desarrollada para la materia de Algoritmos y Programación II. Consiste en un visualizador gráfico interactivo de un Árbol Binario de Búsqueda Auto-balanceado (AVL), construido íntegramente con la librería estándar de Python.

🚀 Características

    Balanceo Automático: Implementación de las cuatro rotaciones clásicas (Simple Izquierda, Simple Derecha, Doble Izquierda-Derecha y Doble Derecha-Izquierda).

    Interfaz Gráfica Nativa: Desarrollada con tkinter, permitiendo una visualización fluida de la estructura jerárquica.

    Métricas en Tiempo Real: Cada nodo muestra su altura (h) y su factor de equilibrio (b) actualizado tras cada inserción.

    Algoritmo de Dibujo Dinámico: Cálculo recursivo de posiciones en el Canvas para evitar solapamiento de nodos hasta ciertos niveles de profundidad.

🛠️ Tecnologías Utilizadas

    Lenguaje: Python 3.x

    Librería GUI: Tkinter (Librería estándar)

    Paradigma: Programación Orientada a Objetos (POO)

📋 Estructura del Código

El proyecto sigue una arquitectura limpia separando la lógica de datos de la interfaz:

    Node: Clase que representa la entidad mínima de datos, almacenando punteros (left, right), valor y altura.

    AVLTree: Motor lógico que contiene los algoritmos de inserción y los métodos de rotación para mantener la propiedad O(logn).

    AVLVisualizer: Capa de presentación que gestiona el ciclo de vida de la ventana y el renderizado recursivo en el lienzo.

💻 Instalación y Ejecución

Al no requerir dependencias externas, la ejecución es directa:

    Clona este repositorio o descarga el archivo .py.

    Abre una terminal y ejecuta:
```bash
    python main.py
```
```

📖 Casos de Prueba Recomendados

Para verificar el funcionamiento de las rotaciones, inserte los valores en los siguientes órdenes:

    Rotación Simple: 10, 20, 30 (Provoca rotación a la izquierda).

    Rotación Doble: 30, 10, 20 (Provoca rotación Izquierda-Derecha).

Autor: Wilfredo Mouzalli Materia: Algoritmos y Programación Fecha: 2026

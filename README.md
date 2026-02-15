# Juego: Adivina el Número (El softward adivina)
Este programa implementa un juego en Python donde el usuario piensa en un número
entre 1 y 100, y la computadora intenta adivinarlo utilizando lógica condicional
y estructuras repetitivas.
<img width="975" height="1019" alt="image" src="https://github.com/user-attachments/assets/054337c0-7140-4f50-9eea-86302caf9e5f" />


El usuario solo debe indicar si el número propuesto por la computadora es:

- mayor
- menor
- correcto

## Funcionamiento
La computadora aplica una estrategia de búsqueda binaria:

1. Define un rango inicial (1 - 100)
2. Calcula el número intermedio
3. Ajusta los límites según la respuesta del usuario
4. Repite hasta adivinar el número

## Cómo ejecutar el programa

1. Tener Python instalado
2. Abrir la terminal o consola
3. Ejecutar:

```bash
python adivina_numero

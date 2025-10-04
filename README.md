# Juego de Esquivar Obstaculos - Proyecto de Graficacion

## Autor
**Diego Flores Ortiz**

---

## Descripcion del Juego

Este proyecto consiste en un videojuego 2D desarrollado en Python utilizando la libreria Pygame.  
El objetivo del juego es controlar a un personaje (similar a un dinosaurio o figura simple) que corre automaticamente sobre un escenario, mientras aparecen obstaculos que el jugador debe esquivar saltando para evitar perder.  

El juego se inspira en el clasico "juego del dinosaurio" del navegador Google Chrome cuando no hay conexion a internet, pero esta version es una version basica adaptada para practicar los fundamentos de la graficacion por computadora y el uso de Pygame.

---

## Mecanicas del Juego

### Acciones del jugador
- El personaje principal puede saltar al presionar una tecla (por ejemplo, la barra espaciadora).  
- Si el personaje esta en el aire, no puede volver a saltar hasta tocar el suelo nuevamente.  
- El personaje corre de manera automatica hacia la derecha (el fondo se movera para simular desplazamiento).  
- Cada vez que el jugador esquiva un obstaculo, la puntuacion aumenta.  

### Obstaculos
- Los obstaculos apareceran desde el lado derecho de la pantalla y se moveran hacia la izquierda.  
- Cada obstaculo tiene una posicion y velocidad fija.  
- Si el personaje choca con un obstaculo, el juego termina y aparece un mensaje de Game Over.  

### Dificultad
- La velocidad de los obstaculos podra aumentar gradualmente con el tiempo para hacer el juego mas desafiante.  
- No habra multiples niveles ni guardado de puntuacion; solo una partida por intento.  

---

## Limitaciones del Proyecto

- El juego es 2D y no utiliza modelos tridimensionales.  
- No incluye animaciones avanzadas, efectos de particulas ni sonido.  
- No tendra menu principal ni configuraciones.  
- El personaje solo puede **saltar**, no puede agacharse ni moverse lateralmente.  
- Los obstaculos se generan de forma **aleatoria** pero con un limite para no saturar la pantalla.  
- No hay sistema de vidas, una colision termina inmediatamente la partida.  

---

## Elementos Graficos

- El personaje sera una figura simple (por ejemplo, un rectangulo o sprite basico).  
- El fondo podra ser un color solido o una imagen estatica simulando el suelo.  
- Los obstaculos podran representarse con figuras geometricas (rectangulos).  

---

## Controles
- **Barra espaciadora:** Saltar  
- **R:** Reiniciar el juego (opcional)  
- **ESC:** Salir del juego

---

## Tecnologias Utilizadas

- **Python 3.x**
- **Pygame** (para graficos, eventos, y control del juego)

---

## Objetivo Academico

El proposito de este proyecto es aplicar los conocimientos basicos de:
- Graficacion en 2D.  
- Manejo de eventos de teclado.  
- Control de colisiones.  
- Actualizacion de sprites y movimiento en tiempo real.  
- Uso del ciclo principal del juego (game loop).  

---

## Posibles Mejoras Futuras

- Agregar efectos de sonido al saltar o perder.  
- Implementar un sistema de puntuacion maxima.  
- Crear diferentes tipos de obstaculos o fondos.  
- Incluir animacion para el personaje.  
- Agregar un menu de inicio o pantalla de pausa.  



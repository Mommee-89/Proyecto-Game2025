# Dinocode – Documentation (English)

## 1. Overview
**Dinocode** is a fast–paced arcade game inspired by the classic offline dinosaur runner.  
Developed in Python using **Pygame**, the game challenges the player to jump, duck, and avoid ground and aerial obstacles while the speed increases constantly.  
The project also includes a persistent score system using **SQLite**, allowing the best record to remain saved even when closing the game.

---

## 2. Project Structure
```
Dinocode.py        # Main game source code
record.db          # SQLite database containing the saved high score
game_over_image    # PNG/WEBP image displayed on game over (provided by user)
```

---

## 3. Main Features
- Fast and dynamic obstacle generation (ground, wide, low–air, and high–air).
- Player actions:
  - **Jump**
  - **Duck**
- Speed increases as more obstacles are avoided.
- SQLite-based record system with manual reset option.
- On-screen UI:
  - Score
  - Record
  - Speed indicator
- Start instructions and Game Over screen with custom image.

---

## 4. How to Use the Game

### **Controls**
- **Jump:** `SPACE` or `↑`
- **Duck:** `S` or `↓`
- **Reset record:** `C`
- **Restart game:** `R`
- **Exit:** `ESC`

### **How to Run**
1. Install Python 3 and Pygame:
   ```bash
   pip install pygame
   ```
2. Place all project files in the same folder:
   - Dinocode.py  
   - record.db (auto-created if missing)  
   - Game Over image file  
3. Run the game:
   ```bash
   python3 Dinocode.py
   ```

---

## 5. Gameplay Description
- The player controls a neon-style rectangular character.
- Obstacles appear from the right side of the screen at different heights and sizes.
- Avoiding an obstacle grants **1 point**.
- The game becomes faster gradually, increasing difficulty.
- Colliding with any obstacle triggers Game Over and shows:
  - A custom image
  - Final score
  - Prompt to restart

---

## 6. Persistence System (SQLite)
The file **record.db** stores the highest score ever obtained.  
The player may erase it using the `C` key.

---

## 7. Purpose of the Project
This game was developed for academic purposes in the subject **Grafiación**, showcasing:
- Game loop structure
- Graphics rendering with Pygame
- Collision detection
- Animation–style motion
- Database integration
- UI design and event handling

---

# Dinocode – Documentación (Español)

## 1. Descripción General
**Dinocode** es un juego estilo arcade inspirado en el clásico “Dino Runner”.  
Está desarrollado en Python con **Pygame** y desafía al jugador a saltar, agacharse y esquivar obstáculos terrestres y aéreos mientras la velocidad aumenta progresivamente.  
Incluye además un sistema de récord guardado usando **SQLite**, que mantiene la mejor puntuación registrada.

---

## 2. Estructura del Proyecto
```
Dinocode.py        # Código principal del juego
record.db          # Base de datos SQLite donde se guarda el récord
game_over_image    # Imagen mostrada al perder (proporcionada por el usuario)
```

---

## 3. Características Principales
- Generación rápida y variada de obstáculos (suelo, anchos, aéreos bajos y altos).
- Acciones del jugador:
  - **Saltar**
  - **Agacharse**
- Incremento de velocidad por cada obstáculo superado.
- Sistema de récord persistente con opción de borrado.
- Interfaz gráfica con:
  - Obstáculos esquivados
  - Récord guardado
  - Velocidad actual
- Pantalla de inicio con instrucciones y pantalla de Game Over con imagen personalizada.

---

## 4. Cómo Usar el Juego

### **Controles**
- **Saltar:** `ESPACIO` o `↑`
- **Agacharse:** `S` o `↓`
- **Borrar récord:** `C`
- **Reiniciar juego:** `R`
- **Salir:** `ESC`

### **Pasos para Ejecutar**
1. Instalar Python 3 y Pygame:
   ```bash
   pip install pygame
   ```
2. Colocar todos los archivos del proyecto en la misma carpeta:
   - Dinocode.py  
   - record.db (se crea automáticamente si no existe)  
   - Imagen de Game Over  
3. Ejecutar:
   ```bash
   python3 Dinocode.py
   ```

---

## 5. Descripción del Juego
- El jugador controla un personaje rectangular estilo neón.
- Los obstáculos aparecen desde la derecha con diferentes tamaños y alturas.
- Cada obstáculo esquivado suma **1 punto**.
- La velocidad aumenta gradualmente con el tiempo.
- Si el jugador choca, aparece la pantalla de Game Over con:
  - La imagen asignada
  - Los puntos obtenidos
  - Indicaciones para reiniciar

---

## 6. Sistema de Persistencia (SQLite)
El archivo **record.db** almacena el récord más alto alcanzado.  
Puede ser borrado manualmente con la tecla `C`.

---

## 7. Objetivo Académico
Este proyecto fue desarrollado para la materia **Graficación**, demostrando:
- Estructura de un ciclo de juego
- Renderizado con Pygame
- Detección de colisiones
- Movimiento progresivo y dificultad escalonada
- Integración con base de datos
- Manejo de eventos y diseño de interfaz

---

**Autor:** Diego Flores Ortiz  
**Proyecto desarrollado con apoyo de IA para documentación.**

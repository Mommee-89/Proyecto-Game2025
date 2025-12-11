# Diego Flores Ortiz
# Grupo: 5SS
# Materia: Graficacion
# Nombre del juego: Dinocode

import pygame
import random
import sqlite3
import sys

pygame.init()

ANCHO, ALTO = 900, 500
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Dinocode")

clock = pygame.time.Clock()
fuente = pygame.font.SysFont("consolas", 22)
fuente_grande = pygame.font.SysFont("consolas", 30)  
fuente_mediana = pygame.font.SysFont("consolas", 26)
fuente_pequena = pygame.font.SysFont("consolas", 20)

# Cargar imagen de Game Over
try:
    game_over_img = pygame.image.load("c731fd7c073cf6a30f4b3e036f232d14.webp")
    game_over_rect = game_over_img.get_rect(center=(ANCHO // 2, ALTO // 2 - 70))
except pygame.error as e:
    print(f"No se pudo cargar la imagen de Game Over: {e}")
    game_over_img = None

# Colores
NEON_GREEN = (0, 255, 128)
NEON_RED = (255, 60, 60)
NEON_YELLOW = (255, 230, 0)
NEON_BLUE = (60, 180, 255)
NEON_PURPLE = (180, 60, 255)
BLANCO = (255, 255, 255)
FONDO = (10, 10, 20)
COLOR_AGACHADO = (0, 200, 255)

# Configuracion Fisica
SUELO_Y = 400
GRAVEDAD = 2.0
VEL_SALTO = -24
JUGADOR_X = 100

# Tamaños del jugador
ALTO_PIE = 50
ALTO_AGACHADO = 25
ANCHO_JUGADOR = 30

# Base de Datos
def inicializar_bd():
    conn = sqlite3.connect("record.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS datos(record INTEGER)")
    cur.execute("SELECT * FROM datos")
    if cur.fetchone() is None:
        cur.execute("INSERT INTO datos(record) VALUES(0)")
    conn.commit()
    conn.close()

def obtener_record():
    conn = sqlite3.connect("record.db")
    cur = conn.cursor()
    cur.execute("SELECT record FROM datos")
    r = cur.fetchone()[0]
    conn.close()
    return r

def guardar_record(nuevo):
    conn = sqlite3.connect("record.db")
    cur = conn.cursor()
    cur.execute("UPDATE datos SET record = ?", (nuevo,))
    conn.commit()
    conn.close()

def borrar_record():
    conn = sqlite3.connect("record.db")
    cur = conn.cursor()
    cur.execute("UPDATE datos SET record = 0")
    conn.commit()
    conn.close()

inicializar_bd()

def juego():
    # Variables Jugador
    jugador = pygame.Rect(JUGADOR_X, SUELO_Y - ALTO_PIE, ANCHO_JUGADOR, ALTO_PIE)
    vel_y = 0
    en_suelo = True
    esta_agachado = False
    game_over = False

    # Variables Obstaculos
    obstaculos = []
    tiempo_spawn = pygame.time.get_ticks()
    
    velocidad_juego = 8.0
    velocidad_maxima = 45.0
    
    puntos = 0
    record = obtener_record()

    while True:
        # EVENTOS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                if event.key == pygame.K_c:
                    borrar_record()
                    record = 0
                
                if not game_over:
                    if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and en_suelo:
                        vel_y = VEL_SALTO
                        en_suelo = False
                        esta_agachado = False
                    
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if en_suelo and not esta_agachado:
                            esta_agachado = True
                            jugador.height = ALTO_AGACHADO
                            jugador.y = SUELO_Y - ALTO_AGACHADO
                
                else:
                    if event.key == pygame.K_r:
                        return juego()

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and esta_agachado:
                    esta_agachado = False
                    jugador.y -= (ALTO_PIE - ALTO_AGACHADO)
                    jugador.height = ALTO_PIE

        # LOGICA
        if not game_over:
            vel_y += GRAVEDAD
            jugador.y += vel_y

            if jugador.bottom >= SUELO_Y:
                jugador.bottom = SUELO_Y
                vel_y = 0
                en_suelo = True

            # SPAWN OBSTACULOS
            ahora = pygame.time.get_ticks()
            frecuencia_spawn = max(300, 1100 - (velocidad_juego * 25))
            
            if ahora - tiempo_spawn > frecuencia_spawn:
                if random.random() < 0.99:
                    tipo = random.choice(["suelo", "ancho", "aereo_bajo", "aereo_alto"])
                    rect = None

                    if tipo == "suelo":
                        alto = random.randint(40, 60)
                        rect = pygame.Rect(ANCHO, SUELO_Y - alto, 30, alto)
                        color = NEON_RED

                    elif tipo == "ancho":
                        alto = random.randint(35, 50)
                        rect = pygame.Rect(ANCHO, SUELO_Y - alto, random.randint(70, 90), alto)
                        color = NEON_PURPLE

                    elif tipo == "aereo_bajo":
                        rect = pygame.Rect(ANCHO, SUELO_Y - 50, 40, 30)
                        color = NEON_YELLOW

                    elif tipo == "aereo_alto":
                        rect = pygame.Rect(ANCHO, SUELO_Y - 110, 40, 70)
                        color = NEON_YELLOW

                    obstaculos.append({
                        "rect": rect,
                        "color": color,
                        "x": float(rect.x)
                    })

                tiempo_spawn = ahora

            # Mover obstaculos
            for o in obstaculos[:]:
                o["x"] -= velocidad_juego
                o["rect"].x = int(o["x"])

                if o["rect"].right < 0:
                    obstaculos.remove(o)
                    puntos += 1

                    if velocidad_juego < velocidad_maxima:
                        velocidad_juego += 0.2

            # Colisiones
            hitbox = jugador.inflate(-8, -8)
            for o in obstaculos:
                if hitbox.colliderect(o["rect"]):
                    game_over = True
                    if puntos > record:
                        guardar_record(puntos)
                        record = puntos

        # DIBUJADO
        pantalla.fill(FONDO)
        pygame.draw.line(pantalla, NEON_BLUE, (0, SUELO_Y), (ANCHO, SUELO_Y), 3)

        pygame.draw.rect(pantalla, COLOR_AGACHADO if esta_agachado else NEON_GREEN, jugador)

        for o in obstaculos:
            pygame.draw.rect(pantalla, o["color"], o["rect"])
            pygame.draw.rect(pantalla, BLANCO, o["rect"], 1)

        texto_puntos = fuente.render(f"OBSTACULOS: {puntos:03}", True, BLANCO)
        texto_record = fuente.render(f"RECORD: {record:03}", True, BLANCO)
        texto_vel = fuente.render(f"VELOCIDAD: {velocidad_juego:.1f}", True, NEON_BLUE)
        
        pantalla.blit(texto_puntos, (ANCHO - 250, 20))
        pantalla.blit(texto_record, (ANCHO - 250, 50))
        pantalla.blit(texto_vel, (20, 20))

        # INSTRUCCIONES AL INICIO
        if puntos == 0 and not game_over:
            instrucciones = [
                "CONTROLES DEL JUEGO",
                "SALTAR: [ESPACIO] o [↑]",
                "AGACHARSE: [S] o [↓]",
                "BORRAR RECORD: [C]",
                "REINICIAR: [R]",
                "SALIR: [ESC]"
            ]

            y = ALTO//2 - 80
            for linea in instrucciones:
                texto = fuente_pequena.render(linea, True, (180, 180, 180))
                pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, y))
                y += 22

        # GAME OVER
        if game_over:
            if game_over_img:
                pantalla.blit(game_over_img, game_over_rect)

            texto_go = fuente_grande.render("GAME OVER", True, NEON_RED)
            pantalla.blit(texto_go, (ANCHO//2 - texto_go.get_width()//2, ALTO//2))

            texto_r = fuente_mediana.render("Presiona R para reiniciar", True, BLANCO)
            pantalla.blit(texto_r, (ANCHO//2 - texto_r.get_width()//2, ALTO - 60))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    juego()

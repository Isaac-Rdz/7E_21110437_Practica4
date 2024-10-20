import pygame

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Clue")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Personajes, armas y locaciones
characters = [
    ("Isaac", "Ingeniero"),
    ("Jonathan", "Militar"),
    ("Mauricio", "Maestro"),
    ("Samantha", "Escritora"),
    ("Esmeralda", "Científica"),
]

weapons = [
    "Cuchillo",
    "Revólver",
    "Cinta adhesiva",
    "Pistola",
    "Veneno",
]

locations = [
    "Biblioteca",
    "Cocina",
    "Salón",
    "Comedor",
    "Jardín",
]

# Historias personalizadas
def get_story(character, weapon, location):
    stories = {
        ("Isaac", "Cuchillo", "Biblioteca"): "Isaac apuñaló a su rival en la biblioteca durante una investigación fallida.",
        ("Isaac", "Revólver", "Biblioteca"): "Isaac disparó al intruso en la biblioteca después de descubrirlo husmeando entre sus libros.",
        ("Isaac", "Cinta adhesiva", "Biblioteca"): "Isaac inmovilizó a su oponente con cinta adhesiva mientras buscaba pruebas.",
        ("Isaac", "Pistola", "Biblioteca"): "Isaac usó su pistola para silenciar a un ladrón en la biblioteca.",
        ("Isaac", "Veneno", "Biblioteca"): "Isaac envenenó la bebida de un rival en la biblioteca tras una acalorada discusión.",

        ("Isaac", "Cuchillo", "Jardín"): "Isaac apuñaló a un testigo en el jardín durante un oscuro encuentro.",
        ("Isaac", "Revólver", "Jardín"): "Isaac disparó a su adversario en el jardín tras descubrir un secreto.",
        ("Isaac", "Cinta adhesiva", "Jardín"): "Isaac utilizó cinta adhesiva para inmovilizar a su rival en el jardín.",
        ("Isaac", "Pistola", "Jardín"): "Isaac disparó a un enemigo en el jardín después de un trato fallido.",
        ("Isaac", "Veneno", "Jardín"): "Isaac envenenó la comida de un rival en el jardín.",

        ("Isaac", "Cuchillo", "Salón"): "Isaac apuñaló a su crítico en el salón tras una amarga discusión.",
        ("Isaac", "Revólver", "Salón"): "Isaac disparó a un rival en el salón, celoso de su éxito.",
        ("Isaac", "Cinta adhesiva", "Salón"): "Isaac utilizó cinta adhesiva para inmovilizar a un rival en el salón.",
        ("Isaac", "Pistola", "Salón"): "Isaac disparó en el salón durante una pelea artística.",
        ("Isaac", "Veneno", "Salón"): "Isaac envenenó a un crítico de arte en el salón durante una exposición.",

        ("Isaac", "Cuchillo", "Cocina"): "Isaac apuñaló a su enemigo en la cocina mientras preparaba una cena.",
        ("Isaac", "Revólver", "Cocina"): "Isaac disparó a un rival en la cocina tras una fuerte discusión.",
        ("Isaac", "Cinta adhesiva", "Cocina"): "Isaac utilizó cinta adhesiva para inmovilizar a su rival en la cocina.",
        ("Isaac", "Pistola", "Cocina"): "Isaac disparó en la cocina tras descubrir un secreto oculto.",
        ("Isaac", "Veneno", "Cocina"): "Isaac envenenó la comida de su rival en la cocina.",

        ("Isaac", "Cuchillo", "Comedor"): "Isaac apuñaló a un traidor en el comedor durante una cena.",
        ("Isaac", "Revólver", "Comedor"): "Isaac disparó a un espía en el comedor mientras cenaban.",
        ("Isaac", "Cinta adhesiva", "Comedor"): "Isaac inmovilizó a su adversario con cinta adhesiva en el comedor.",
        ("Isaac", "Pistola", "Comedor"): "Isaac disparó en el comedor para proteger un secreto.",
        ("Isaac", "Veneno", "Comedor"): "Isaac envenenó a un rival en el comedor, acabando con la competencia.",

        ("Jonathan", "Cuchillo", "Biblioteca"): "Jonathan apuñaló a su rival en la biblioteca durante una investigación fallida.",
        ("Jonathan", "Revólver", "Biblioteca"): "Jonathan disparó al intruso en la biblioteca después de descubrirlo husmeando entre sus libros.",
        ("Jonathan", "Cinta adhesiva", "Biblioteca"): "Jonathan inmovilizó a su oponente con cinta adhesiva mientras buscaba pruebas.",
        ("Jonathan", "Pistola", "Biblioteca"): "Jonathan usó su pistola para silenciar a un ladrón en la biblioteca.",
        ("Jonathan", "Veneno", "Biblioteca"): "Jonathan envenenó la bebida de un rival en la biblioteca tras una acalorada discusión.",

        ("Jonathan", "Cuchillo", "Jardín"): "Jonathan apuñaló a un testigo en el jardín durante un oscuro encuentro.",
        ("Jonathan", "Revólver", "Jardín"): "Jonathan disparó a su adversario en el jardín tras descubrir un secreto.",
        ("Jonathan", "Cinta adhesiva", "Jardín"): "Jonathan utilizó cinta adhesiva para inmovilizar a su rival en el jardín.",
        ("Jonathan", "Pistola", "Jardín"): "Jonathan disparó a un enemigo en el jardín después de un trato fallido.",
        ("Jonathan", "Veneno", "Jardín"): "Jonathan envenenó la comida de un rival en el jardín.",

        ("Jonathan", "Cuchillo", "Salón"): "Jonathan apuñaló a su crítico en el salón tras una amarga discusión.",
        ("Jonathan", "Revólver", "Salón"): "Jonathan disparó a un rival en el salón, celoso de su éxito.",
        ("Jonathan", "Cinta adhesiva", "Salón"): "Jonathan utilizó cinta adhesiva para inmovilizar a un rival en el salón.",
        ("Jonathan", "Pistola", "Salón"): "Jonathan disparó en el salón durante una pelea artística.",
        ("Jonathan", "Veneno", "Salón"): "Jonathan envenenó a un crítico de arte en el salón durante una exposición.",

        ("Jonathan", "Cuchillo", "Cocina"): "Jonathan apuñaló a su enemigo en la cocina mientras preparaba una cena.",
        ("Jonathan", "Revólver", "Cocina"): "Jonathan disparó a un rival en la cocina tras una fuerte discusión.",
        ("Jonathan", "Cinta adhesiva", "Cocina"): "Jonathan utilizó cinta adhesiva para inmovilizar a su rival en la cocina.",
        ("Jonathan", "Pistola", "Cocina"): "Jonathan disparó en la cocina tras descubrir un secreto oculto.",
        ("Jonathan", "Veneno", "Cocina"): "Jonathan envenenó la comida de su rival en la cocina.",

        ("Jonathan", "Cuchillo", "Comedor"): "Jonathan apuñaló a un traidor en el comedor durante una cena.",
        ("Jonathan", "Revólver", "Comedor"): "Jonathan disparó a un espía en el comedor mientras cenaban.",
        ("Jonathan", "Cinta adhesiva", "Comedor"): "Jonathan inmovilizó a su adversario con cinta adhesiva en el comedor.",
        ("Jonathan", "Pistola", "Comedor"): "Jonathan disparó en el comedor para proteger un secreto.",
        ("Jonathan", "Veneno", "Comedor"): "Jonathan envenenó a un rival en el comedor, acabando con la competencia.",
        
        ("Mauricio", "Cuchillo", "Biblioteca"): "Mauricio apuñaló a su rival en la biblioteca durante una investigación fallida.",
        ("Mauricio", "Revólver", "Biblioteca"): "Mauricio disparó al intruso en la biblioteca después de descubrirlo husmeando entre sus libros.",
        ("Mauricio", "Cinta adhesiva", "Biblioteca"): "Mauricio inmovilizó a su oponente con cinta adhesiva mientras buscaba pruebas.",
        ("Mauricio", "Pistola", "Biblioteca"): "Mauricio usó su pistola para silenciar a un ladrón en la biblioteca.",
        ("Mauricio", "Veneno", "Biblioteca"): "Mauricio envenenó la bebida de un rival en la biblioteca tras una acalorada discusión.",

        ("Mauricio", "Cuchillo", "Jardín"): "Mauricio apuñaló a un testigo en el jardín durante un oscuro encuentro.",
        ("Mauricio", "Revólver", "Jardín"): "Mauricio disparó a su adversario en el jardín tras descubrir un secreto.",
        ("Mauricio", "Cinta adhesiva", "Jardín"): "Mauricio utilizó cinta adhesiva para inmovilizar a su rival en el jardín.",
        ("Mauricio", "Pistola", "Jardín"): "Mauricio disparó a un enemigo en el jardín después de un trato fallido.",
        ("Mauricio", "Veneno", "Jardín"): "Mauricio envenenó la comida de un rival en el jardín.",

        ("Mauricio", "Cuchillo", "Salón"): "Mauricio apuñaló a su crítico en el salón tras una amarga discusión.",
        ("Mauricio", "Revólver", "Salón"): "Mauricio disparó a un rival en el salón, celoso de su éxito.",
        ("Mauricio", "Cinta adhesiva", "Salón"): "Mauricio utilizó cinta adhesiva para inmovilizar a un rival en el salón.",
        ("Mauricio", "Pistola", "Salón"): "Mauricio disparó en el salón durante una pelea artística.",
        ("Mauricio", "Veneno", "Salón"): "Mauricio envenenó a un crítico de arte en el salón durante una exposición.",

        ("Mauricio", "Cuchillo", "Cocina"): "Mauricio apuñaló a su enemigo en la cocina mientras preparaba una cena.",
        ("Mauricio", "Revólver", "Cocina"): "Mauricio disparó a un rival en la cocina tras una fuerte discusión.",
        ("Mauricio", "Cinta adhesiva", "Cocina"): "Mauricio utilizó cinta adhesiva para inmovilizar a su rival en la cocina.",
        ("Mauricio", "Pistola", "Cocina"): "Mauricio disparó en la cocina tras descubrir un secreto oculto.",
        ("Mauricio", "Veneno", "Cocina"): "Mauricio envenenó la comida de su rival en la cocina.",

        ("Mauricio", "Cuchillo", "Comedor"): "Mauricio apuñaló a un traidor en el comedor durante una cena.",
        ("Mauricio", "Revólver", "Comedor"): "Mauricio disparó a un espía en el comedor mientras cenaban.",
        ("Mauricio", "Cinta adhesiva", "Comedor"): "Mauricio inmovilizó a su adversario con cinta adhesiva en el comedor.",
        ("Mauricio", "Pistola", "Comedor"): "Mauricio disparó en el comedor para proteger un secreto.",
        ("Mauricio", "Veneno", "Comedor"): "Mauricio envenenó a un rival en el comedor, acabando con la competencia.",
        
        ("Samantha", "Cuchillo", "Biblioteca"): "Samantha apuñaló a su rival en la biblioteca durante una investigación fallida.",
        ("Samantha", "Revólver", "Biblioteca"): "Samantha disparó al intruso en la biblioteca después de descubrirlo husmeando entre sus libros.",
        ("Samantha", "Cinta adhesiva", "Biblioteca"): "Samantha inmovilizó a su oponente con cinta adhesiva mientras buscaba pruebas.",
        ("Samantha", "Pistola", "Biblioteca"): "Samantha usó su pistola para silenciar a un ladrón en la biblioteca.",
        ("Samantha", "Veneno", "Biblioteca"): "Samantha envenenó la bebida de un rival en la biblioteca tras una acalorada discusión.",

        ("Samantha", "Cuchillo", "Jardín"): "Samantha apuñaló a un testigo en el jardín durante un oscuro encuentro.",
        ("Samantha", "Revólver", "Jardín"): "Samantha disparó a su adversario en el jardín tras descubrir un secreto.",
        ("Samantha", "Cinta adhesiva", "Jardín"): "Samantha utilizó cinta adhesiva para inmovilizar a su rival en el jardín.",
        ("Samantha", "Pistola", "Jardín"): "Samantha disparó a un enemigo en el jardín después de un trato fallido.",
        ("Samantha", "Veneno", "Jardín"): "Samantha envenenó la comida de un rival en el jardín.",

        ("Samantha", "Cuchillo", "Salón"): "Samantha apuñaló a su crítico en el salón tras una amarga discusión.",
        ("Samantha", "Revólver", "Salón"): "Samantha disparó a un rival en el salón, celoso de su éxito.",
        ("Samantha", "Cinta adhesiva", "Salón"): "Samantha utilizó cinta adhesiva para inmovilizar a un rival en el salón.",
        ("Samantha", "Pistola", "Salón"): "Samantha disparó en el salón durante una pelea artística.",
        ("Samantha", "Veneno", "Salón"): "Samantha envenenó a un crítico de arte en el salón durante una exposición.",

        ("Samantha", "Cuchillo", "Cocina"): "Samantha apuñaló a su enemigo en la cocina mientras preparaba una cena.",
        ("Samantha", "Revólver", "Cocina"): "Samantha disparó a un rival en la cocina tras una fuerte discusión.",
        ("Samantha", "Cinta adhesiva", "Cocina"): "Samantha utilizó cinta adhesiva para inmovilizar a su rival en la cocina.",
        ("Samantha", "Pistola", "Cocina"): "Samantha disparó en la cocina tras descubrir un secreto oculto.",
        ("Samantha", "Veneno", "Cocina"): "Samantha envenenó la comida de su rival en la cocina.",

        ("Samantha", "Cuchillo", "Comedor"): "Samantha apuñaló a un traidor en el comedor durante una cena.",
        ("Samantha", "Revólver", "Comedor"): "Samantha disparó a un espía en el comedor mientras cenaban.",
        ("Samantha", "Cinta adhesiva", "Comedor"): "Samantha inmovilizó a su adversario con cinta adhesiva en el comedor.",
        ("Samantha", "Pistola", "Comedor"): "Samantha disparó en el comedor para proteger un secreto.",
        ("Samantha", "Veneno", "Comedor"): "Samantha envenenó a un rival en el comedor, acabando con la competencia.",
        
        ("Esmeralda", "Cuchillo", "Biblioteca"): "Esmeralda apuñaló a su rival en la biblioteca durante una investigación fallida.",
        ("Esmeralda", "Revólver", "Biblioteca"): "Esmeralda disparó al intruso en la biblioteca después de descubrirlo husmeando entre sus libros.",
        ("Esmeralda", "Cinta adhesiva", "Biblioteca"): "Esmeralda inmovilizó a su oponente con cinta adhesiva mientras buscaba pruebas.",
        ("Esmeralda", "Pistola", "Biblioteca"): "Esmeralda usó su pistola para silenciar a un ladrón en la biblioteca.",
        ("Esmeralda", "Veneno", "Biblioteca"): "Esmeralda envenenó la bebida de un rival en la biblioteca tras una acalorada discusión.",

        ("Esmeralda", "Cuchillo", "Jardín"): "Esmeralda apuñaló a un testigo en el jardín durante un oscuro encuentro.",
        ("Esmeralda", "Revólver", "Jardín"): "Esmeralda disparó a su adversario en el jardín tras descubrir un secreto.",
        ("Esmeralda", "Cinta adhesiva", "Jardín"): "Esmeralda utilizó cinta adhesiva para inmovilizar a su rival en el jardín.",
        ("Esmeralda", "Pistola", "Jardín"): "Esmeralda disparó a un enemigo en el jardín después de un trato fallido.",
        ("Esmeralda", "Veneno", "Jardín"): "Esmeralda envenenó la comida de un rival en el jardín.",

        ("Esmeralda", "Cuchillo", "Salón"): "Esmeralda apuñaló a su crítico en el salón tras una amarga discusión.",
        ("Esmeralda", "Revólver", "Salón"): "Esmeralda disparó a un rival en el salón, celoso de su éxito.",
        ("Esmeralda", "Cinta adhesiva", "Salón"): "Esmeralda utilizó cinta adhesiva para inmovilizar a un rival en el salón.",
        ("Esmeralda", "Pistola", "Salón"): "Esmeralda disparó en el salón durante una pelea artística.",
        ("Esmeralda", "Veneno", "Salón"): "Esmeralda envenenó a un crítico de arte en el salón durante una exposición.",

        ("Esmeralda", "Cuchillo", "Cocina"): "Esmeralda apuñaló a su enemigo en la cocina mientras preparaba una cena.",
        ("Esmeralda", "Revólver", "Cocina"): "Esmeralda disparó a un rival en la cocina tras una fuerte discusión.",
        ("Esmeralda", "Cinta adhesiva", "Cocina"): "Esmeralda utilizó cinta adhesiva para inmovilizar a su rival en la cocina.",
        ("Esmeralda", "Pistola", "Cocina"): "Esmeralda disparó en la cocina tras descubrir un secreto oculto.",
        ("Esmeralda", "Veneno", "Cocina"): "Esmeralda envenenó la comida de su rival en la cocina.",

        ("Esmeralda", "Cuchillo", "Comedor"): "Esmeralda apuñaló a un traidor en el comedor durante una cena.",
        ("Esmeralda", "Revólver", "Comedor"): "Esmeralda disparó a un espía en el comedor mientras cenaban.",
        ("Esmeralda", "Cinta adhesiva", "Comedor"): "Esmeralda inmovilizó a su adversario con cinta adhesiva en el comedor.",
        ("Esmeralda", "Pistola", "Comedor"): "Esmeralda disparó en el comedor para proteger un secreto.",
        ("Esmeralda", "Veneno", "Comedor"): "Esmeralda envenenó a un rival en el comedor, acabando con la competencia.",
    }
    
    return stories.get((character[0], weapon, location), "No hay historia disponible.")

# Función para mostrar opciones y recoger la selección
def select_option(options, title):
    selected_index = 0
    while True:
        screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        title_text = font.render(title, True, BLACK)
        screen.blit(title_text, (50, 20))
        
        for i, option in enumerate(options):
            color = BLACK if i == selected_index else (150, 150, 150)
            option_text = font.render(option[0] if isinstance(option, tuple) else option, True, color)
            screen.blit(option_text, (50, 100 + i * 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(options)
                elif event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected_index]

# Función principal
def main():
    running = True
    selected_character = None
    selected_weapon = None
    selected_location = None

    while running:
        # Elegir personaje
        selected_character = select_option(characters, "Elige un Personaje:")
        if selected_character is None:
            return

        # Elegir arma
        selected_weapon = select_option(weapons, "Elige un Arma:")
        if selected_weapon is None:
            return

        # Elegir locación
        selected_location = select_option(locations, "Elige una Locación:")
        if selected_location is None:
            return

        # Mostrar resultado
        screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        story = get_story(selected_character, selected_weapon, selected_location)
        narrative = f"¡Se ha cometido un asesinato!\n\n" \
                    f"El culpable es: {selected_character[0]} ({selected_character[1]})\n" \
                    f"El arma utilizada: {selected_weapon}\n" \
                    f"Locación del crimen: {selected_location}\n\n" \
                    f"Historia:\n"\
                    f"{story}\n\n" \
                    f"Presiona ESC para salir."
        
        for i, line in enumerate(narrative.split('\n')):
            text = font.render(line, True, BLACK)
            screen.blit(text, (50, 50 + i * 40))

        pygame.display.flip()

        # Esperar a que el usuario presione ESC para salir
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break
            if not running:
                break

    pygame.quit()

# Ejecutar el juego
if __name__ == "__main__":
    main()

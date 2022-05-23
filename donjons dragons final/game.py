import pygame
import pytmx
import pyscroll
from health import *
from player import Player


class Game:

    def __init__(self):
        # Démarrage
        self.running = True
        self.status = 0
        self.map = "world"

        # Affichage de la fenêtre
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Donjons et dragons")

        # Charger la carte classique
        tmx_data = pytmx.util_pygame.load_pygame("carteVraie.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Charger bouton play

        # Générer le joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)
        self.mid_health = mid_health()
        self.full_health = full_health()

        # Définir le logo du jeu
        pygame.display.set_icon(self.player.get())

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_house = tmx_data.get_object_by_name("enter_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # Porte de la maison2
        enter_house2 = tmx_data.get_object_by_name("enter_house2")
        self.enter_house2_rect = pygame.Rect(enter_house2.x, enter_house2.y, enter_house2.width, enter_house2.height)

        # Porte de la maison3
        enter_house3 = tmx_data.get_object_by_name("enter_house3")
        self.enter_house3_rect = pygame.Rect(enter_house3.x, enter_house3.y, enter_house3.width, enter_house3.height)

        # Porte de la maison4
        enter_house4 = tmx_data.get_object_by_name("enter_house4")
        self.enter_house4_rect = pygame.Rect(enter_house4.x, enter_house4.y, enter_house4.width, enter_house4.height)

        # Porte de la maison5
        enter_house5 = tmx_data.get_object_by_name("enter_house5")
        self.enter_house5_rect = pygame.Rect(enter_house5.x, enter_house5.y, enter_house5.width, enter_house5.height)

        # Porte de la maison6
        enter_house6 = tmx_data.get_object_by_name("enter_house6")
        self.enter_house6_rect = pygame.Rect(enter_house6.x, enter_house6.y, enter_house6.width, enter_house6.height)

        # Porte de la maison7
        enter_house7 = tmx_data.get_object_by_name("enter_house7")
        self.enter_house7_rect = pygame.Rect(enter_house7.x, enter_house7.y, enter_house7.width, enter_house7.height)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            self.running = False
        elif pressed[pygame.K_UP]:
            self.player.move_player("up")
        elif pressed[pygame.K_DOWN]:
            self.player.move_player("down")
        elif pressed[pygame.K_RIGHT]:
            self.player.move_player("right")
        elif pressed[pygame.K_LEFT]:
            self.player.move_player("left")

    def switch_house(self):
        self.map = "house"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("pieceDragon.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_house = tmx_data.get_object_by_name("exit_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # Intérieur
        spawn_house_point = tmx_data.get_object_by_name("spawn_house")
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y - 20

    def switch_world(self):
        self.map = "world"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("carteVraie.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_house = tmx_data.get_object_by_name("enter_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # Intérieur
        spawn_house_point = tmx_data.get_object_by_name("enter_house_exit")
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y + 20

    def switch_house2(self):
        self.map = "house2"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("PieceMechant.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_house2 = tmx_data.get_object_by_name("exit_house2")
        self.enter_house2_rect = pygame.Rect(enter_house2.x, enter_house2.y, enter_house2.width, enter_house2.height)

        # Intérieur
        spawn_house_point2 = tmx_data.get_object_by_name("spawn_house2")
        self.player.position[0] = spawn_house_point2.x
        self.player.position[1] = spawn_house_point2.y - 20

    def switch_house3(self):
        self.map = "house3"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("pieceDragon.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_house3 = tmx_data.get_object_by_name("exit_house3")
        self.enter_house3_rect = pygame.Rect(enter_house3.x, enter_house3.y, enter_house3.width, enter_house3.height)

        # Intérieur
        spawn_house3_point = tmx_data.get_object_by_name("spawn_house3")
        self.player.position[0] = spawn_house3_point.x
        self.player.position[1] = spawn_house3_point.y - 20

    def switch_world3(self):
        self.map = "world"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("carteVraie.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_house3 = tmx_data.get_object_by_name("enter_house3")
        self.enter_house3_rect = pygame.Rect(enter_house3.x, enter_house3.y, enter_house3.width, enter_house3.height)

        # Intérieur
        spawn_house3_point = tmx_data.get_object_by_name("enter_house_exit3")
        self.player.position[0] = spawn_house3_point.x
        self.player.position[1] = spawn_house3_point.y + 20

    def switch_house4(self):
        self.map = "house4"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("PieceMechant.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_house4 = tmx_data.get_object_by_name("exit_house4")
        self.enter_house4_rect = pygame.Rect(enter_house4.x, enter_house4.y, enter_house4.width, enter_house4.height)

        # Intérieur
        spawn_house_point4 = tmx_data.get_object_by_name("spawn_house4")
        self.player.position[0] = spawn_house_point4.x
        self.player.position[1] = spawn_house_point4.y - 20

    def switch_house5(self):
        self.map = "house5"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("pieceRien.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_house5 = tmx_data.get_object_by_name("exit_house5")
        self.enter_house5_rect = pygame.Rect(enter_house5.x, enter_house5.y, enter_house5.width, enter_house5.height)

        # Intérieur
        spawn_house5_point = tmx_data.get_object_by_name("spawn_house5")
        self.player.position[0] = spawn_house5_point.x
        self.player.position[1] = spawn_house5_point.y - 20

    def switch_world5(self):
        self.map = "world"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("carteVraie.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_house5 = tmx_data.get_object_by_name("enter_house5")
        self.enter_house5_rect = pygame.Rect(enter_house5.x, enter_house5.y, enter_house5.width, enter_house5.height)

        # Intérieur
        spawn_house5_point = tmx_data.get_object_by_name("enter_house_exit5")
        self.player.position[0] = spawn_house5_point.x
        self.player.position[1] = spawn_house5_point.y + 20

    def switch_house6(self):
        self.map = "house6"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("pieceTresorFinale.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_house6 = tmx_data.get_object_by_name("exit_house6")
        self.enter_house6_rect = pygame.Rect(enter_house6.x, enter_house6.y, enter_house6.width, enter_house6.height)

        # Intérieur
        spawn_house6_point = tmx_data.get_object_by_name("spawn_house6")
        self.player.position[0] = spawn_house6_point.x
        self.player.position[1] = spawn_house6_point.y - 20

    def switch_house7(self):
        self.map = "house7"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("pieceMechant.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=20)
        self.group.add(self.player)

        # Porte de la maison
        enter_house7 = tmx_data.get_object_by_name("exit_house4")
        self.enter_house7_rect = pygame.Rect(enter_house7.x, enter_house7.y, enter_house7.width, enter_house7.height)

        # Intérieur
        spawn_house7_point = tmx_data.get_object_by_name("spawn_house4")
        self.player.position[0] = spawn_house7_point.x
        self.player.position[1] = spawn_house7_point.y - 20

    def update(self):
        self.group.update()

        # Vérifier l'entrée de la maison
        if self.map == "world" and self.player.feet.colliderect(self.enter_house_rect):
            self.switch_house()

        if self.map == "house" and self.player.feet.colliderect(self.enter_house_rect):
            self.switch_world()
            self.status += 1

        # Vérifier l'entrée de la maison 2
        if self.map == "world" and self.player.feet.colliderect(self.enter_house2_rect):
            self.switch_house2()

        if self.map == "house2" and self.player.feet.colliderect(self.enter_house2_rect):
            self.status += 2

        # Vérifier l'entrée de la maison 3
        if self.map == "world" and self.player.feet.colliderect(self.enter_house3_rect):
            self.switch_house3()

        if self.map == "house3" and self.player.feet.colliderect(self.enter_house3_rect):
            self.switch_world3()
            self.status += 1

        # Vérifier l'entrée de la maison 4
        if self.map == "world" and self.player.feet.colliderect(self.enter_house4_rect):
            self.switch_house4()

        if self.map == "house4" and self.player.feet.colliderect(self.enter_house4_rect):
            self.status += 2

        # Vérifier l'entrée de la maison 5
        if self.map == "world" and self.player.feet.colliderect(self.enter_house5_rect):
            self.switch_house5()

        if self.map == "house5" and self.player.feet.colliderect(self.enter_house5_rect):
            self.switch_world5()

        # Vérifier l'entrée de la maison 6
        if self.map == "world" and self.player.feet.colliderect(self.enter_house6_rect):
            self.switch_house6()

        if self.map == "house6" and self.player.feet.colliderect(self.enter_house6_rect):
            self.status -= 10

        # Vérifier l'entrée de la maison 7
        if self.map == "world" and self.player.feet.colliderect(self.enter_house7_rect):
            self.switch_house7()

        if self.map == "house7" and self.player.feet.colliderect(self.enter_house7_rect):
            self.status += 2

        # Vérification des collisions
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):
        clock = pygame.time.Clock()

        ecran_accueil = pygame.image.load("HOMESCREEN.png")
        game_over = pygame.image.load("gameover.png")
        play_space = pygame.image.load("pressSpace2.png")
        play_space_rect = play_space.get_rect()
        victoire = pygame.image.load("victory2.jpg")

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.status = 1

            if self.status == 1:
                self.player.save_location()
                self.handle_input()
                self.update()
                self.group.center(self.player.rect.center)
                self.group.draw(self.screen)
                self.full_health.render(self.screen)

            elif self.status == 2:
                self.player.save_location()
                self.handle_input()
                self.update()
                self.group.center(self.player.rect.center)
                self.group.draw(self.screen)
                self.mid_health.render(self.screen)

            elif self.status >= 3:
                self.screen.blit(game_over, (0, 0))


            elif self.status < 0:
                self.screen.blit(victoire, (0, 0))

            else:
                self.screen.blit(ecran_accueil, (0, 0))
                self.screen.blit(play_space, (60, 500))

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()

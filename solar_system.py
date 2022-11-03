import sys, pygame, requests, json
pygame.font.init()

screenW, screenH = 1600, 1000
screen = pygame.display.set_mode((screenW,screenH))
print(pygame.display.get_window_size())


# ICI ON DEFINIT DES TRUCS
response = requests.get("https://api.le-systeme-solaire.net/rest.php/bodies?data=id%2CequaRadius%2Cdensity%2Cgravity%2CisPlanet%2CsideralOrbit%2Cperihelion%2Crel&filter%5B%5D=isPlanet%2Ceq%2Ctrue")
reponseData = json.loads(response.text)

print(response.status_code)


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



# class Background(pygame.sprite.Sprite):
#     def __init__(self, image_file, location):
#         pygame.sprite.Sprite.__init__(self)  
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location

# BackGround = Background('background.jpg', [0,0])

my_font = pygame.font.SysFont('Albany', 30)

image_soleil = pygame.image.load("Sun.png")

image_soleil = pygame.transform.scale(image_soleil,(150, 150))


class Planet:
    def __init__(self, id, equaRadius, density, gravity, color):
        self.id = id
        self.equaRadius = equaRadius/1000
        self.density = density
        self.gravity = gravity
        self.color = color


#Uranus
uranus = Planet(reponseData["bodies"][0]["id"],reponseData["bodies"][0]["equaRadius"],reponseData["bodies"][0]["density"],reponseData["bodies"][0]["gravity"],(255,255,255))
print(uranus.id)

#Neptune
neptune = Planet(reponseData["bodies"][1]["id"],reponseData["bodies"][1]["equaRadius"],reponseData["bodies"][1]["density"],reponseData["bodies"][1]["gravity"],(255,255,255))
print(neptune.id)

#Jupiter
jupiter = Planet(reponseData["bodies"][2]["id"],reponseData["bodies"][2]["equaRadius"],reponseData["bodies"][2]["density"],reponseData["bodies"][2]["gravity"],(167,132,32))
print(jupiter.id)

#Mars
mars = Planet(reponseData["bodies"][3]["id"],reponseData["bodies"][3]["equaRadius"],reponseData["bodies"][3]["density"],reponseData["bodies"][3]["gravity"],(255,255,255))
print(mars.id)

#Mercure
mercure = Planet(reponseData["bodies"][4]["id"],reponseData["bodies"][4]["equaRadius"],reponseData["bodies"][4]["density"],reponseData["bodies"][4]["gravity"],(170,112,65))
print(neptune.id)

#Saturne
saturne = Planet(reponseData["bodies"][5]["id"],reponseData["bodies"][5]["equaRadius"],reponseData["bodies"][5]["density"],reponseData["bodies"][5]["gravity"],(211,189,56))
print(neptune.id)

#Terre
terre = Planet(reponseData["bodies"][6]["id"],reponseData["bodies"][6]["equaRadius"],reponseData["bodies"][6]["density"],reponseData["bodies"][6]["gravity"],(25,153,218))
print(terre.id)

#Venus
venus = Planet(reponseData["bodies"][7]["id"],reponseData["bodies"][7]["equaRadius"],reponseData["bodies"][7]["density"],reponseData["bodies"][7]["gravity"],(184,20,18))
print(neptune.id)


play = True
clock = pygame.time.Clock()

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            pass
            # print(event.pos)
        if event.type == pygame.KEYUP:
            print(event.key, event.unicode, event.scancode)
            if event.key == pygame.K_ESCAPE:
                play = False

    screen.fill([0, 0, 0])
    
    screen.blit(image_soleil, (screenW/2 - 75 , screenH/2 - 75))
    
    # screen.blit(BackGround.image, BackGround.rect)
    
    #Neptune
    pygame.draw.circle(screen, neptune.color, (50,screenH/2), neptune.equaRadius)
    
    #Uranus
    pygame.draw.circle(screen, uranus.color, (150,screenH/2), uranus.equaRadius)
    
    #Saturne
    pygame.draw.circle(screen, saturne.color, (300,screenH/2), saturne.equaRadius)
    
    #Jupiter
    pygame.draw.circle(screen, jupiter.color, (475,screenH/2), jupiter.equaRadius)
    
    #Mars
    pygame.draw.circle(screen, mars.color, (610,screenH/2), mars.equaRadius)
    
    #Terre
    pygame.draw.circle(screen, terre.color, (640,screenH/2), terre.equaRadius)
    
    #Venus
    pygame.draw.circle(screen, venus.color, (670,screenH/2), venus.equaRadius)
    
    #Mercure
    pygame.draw.circle(screen, mercure.color, (700,screenH/2), mercure.equaRadius)
    
    
    text_surface = my_font.render('Some Text', True, (255, 255, 255))
    screen.blit(text_surface, (0,0))
 
    # ICI ON AFFICHE ET ON BOUGE DES TRUCS

    clock.tick(60)
    pygame.display.flip()
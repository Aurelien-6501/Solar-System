import sys, pygame, requests, json, random
pygame.font.init()

screenW, screenH = 1600, 1000
screen = pygame.display.set_mode((screenW,screenH))
print(pygame.display.get_window_size())
screen.fill([0, 0, 0])

# APPEL API
response = requests.get("https://api.le-systeme-solaire.net/rest.php/bodies?data=id%2CequaRadius%2Cdensity%2Cgravity%2CisPlanet%2CsideralOrbit%2Cperihelion%2Crel&filter%5B%5D=isPlanet%2Ceq%2Ctrue")
if response.status_code == 400 :
    print("error" + response.status_code)
else:
    print(response.status_code)
    
reponseData = json.loads(response.text)



# COLORS
    
COLOR_NEPTUNE = (10,148,190)
COLOR_URANUS = (62,184,221)
COLOR_SATURNE = (229,157,43)
COLOR_JUPITER = (227,118,25)
COLOR_MARS = (227,62,25)
COLOR_TERRE = (25,153,218)
COLOR_VENUS = (184,20,18)
COLOR_MERCURE = (170,112,65)


def getColorOfPlanet(planetName):
    match planetName:
        case 'neptune':
            return COLOR_NEPTUNE
        case 'uranus':
            return COLOR_URANUS
        case 'saturne':
            return COLOR_SATURNE
        case 'jupiter':
            return COLOR_JUPITER
        case 'mars':
            return COLOR_MARS
        case 'terre':
            return COLOR_TERRE
        case 'venus':
            return COLOR_VENUS
        case 'mercure':
            return COLOR_MERCURE
        case _:
            return "0"

def getPositionOfPlanet(planetName):
    match planetName:
        case 'neptune':
            return 250
        case 'uranus':
            return 400
        case 'saturne':
            return 600
        case 'jupiter':
            return 820
        case 'mars':
            return 1000
        case 'terre':
            return 1100
        case 'venus':
            return 1200
        case 'mercure':
            return 1275
        case _:
            return "error position"

# BACKGROUND AVEC IMAGE
# class Background(pygame.sprite.Sprite):
#     def __init__(self, image_file, location):
#         pygame.sprite.Sprite.__init__(self)  
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location

# BackGround = Background('background.jpg', [0,0])


my_font = pygame.font.SysFont('Albany', 30)

image_soleil = pygame.image.load("Images\Sun.png")

image_soleil = pygame.transform.scale(image_soleil,(150, 150))


class Planet:
    def __init__(self, id, equaRadius, density, gravity, perihelion, color, position):
        self.id = id
        self.equaRadius = equaRadius/1000
        self.density = density
        self.gravity = gravity
        self.perihelion = perihelion
        self.color = color
        self.position = position

class Star:
    def __init__(self, starX, starY, starRadius):
        self.starX = starX
        self.starY = starY
        self.starRadius = starRadius
        
#Etoile
max = 200
min = 0
while min < max: 
    etoile = Star(random.randint(0,screenW), random.randint(0,screenH), 2 )   
    pygame.draw.circle(screen, (255,255,255), (etoile.starX, etoile.starY), etoile.starRadius)
    min += 1

# Planete
planetList = []
for planet in reponseData["bodies"]:
    print(planet["id"])
    print(planet["equaRadius"])
    print(planet["density"])
    print(planet["gravity"])

    planetList.append(Planet(planet["id"], planet["equaRadius"], planet["density"], planet["gravity"], planet["perihelion"], getColorOfPlanet(planet["id"]), getPositionOfPlanet(planet["id"])))


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

    
    
    screen.blit(image_soleil, (1400 - 75 , screenH/2 - 75))
    
    # screen.blit(BackGround.image, BackGround.rect)
    

    #DRAW PLANETE
    for planet in planetList:
        pygame.draw.circle(screen, planet.color, (getPositionOfPlanet(planet.id),screenH/2), planet.equaRadius)  
    
    text_surface = my_font.render('Some Text', True, (255, 255, 255))
    screen.blit(text_surface, (0,0))
 

    clock.tick(60)
    pygame.display.flip()
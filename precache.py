from pygame import display, image, transform, time
WIDTH_SCREEN = 800
HEIGHT_SCREEN = 600
FPS = 60
screen = display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
display.set_caption('Car Game')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
GREEN_2 = (0, 255, 0)

carImg = image.load("images/car1.png")
carImg = transform.scale(carImg, (60, 80))

carImg_2 = image.load("images/car2.png")
carImg_2 = transform.scale(carImg_2, (45, 80))

carImg_3 = image.load("images/car3.png")
carImg_3 = transform.scale(carImg_3, (45, 80))

car_width = 60

clock = time.Clock()

## python -m pip install pygame
import pygame

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# نسخه اول بازی را به شکلی تغییر دادیم تا توپ بتواند با کلیدهای
# کیبورد در هر دو جهت حرکت کند

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# یک پنجره میسازیم و عنوان و سایز آن را مشخص میکنیم
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Our Simple Game Part4")
clock = pygame.time.Clock()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# جای توپ و سرعت حرکت آن را مشخص میکنیم
x, y, speed = 245, 245, +10

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# یک حلقه نامحدود داریم که در هر چرخه رویدادهای بازی را بررسی کرده
# منطق بازی را بروزرسانی میکند و همینطور صفحه بازی را دوباره رسم
# میکند
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # با توجه به کلیدهای کیبورد جای توپ را حرکت میدهیم
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # مشخص میکنیم توپ در محور ایکس نباید از صفحه خارج شود
    if x > 490:
        x = 490
    if x < 10:
        x = 10

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # مشخص میکنیم توپ در محور وآی نباید از صفحه خارج شود
    if y > 490:
        y = 490
    if y < 10:
        y = 10

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ۶۰ فریم در ثانیه
    clock.tick(60)

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # پاکسازی صفحه با یک رنگ دلخواه
    screen.fill((255, 0, 127))

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # در اخر با مختصات جدید بر روی صفحه یک دایره رسم میکنیم
    pygame.draw.circle(screen, (127, 255, 0), (x, y), 10)
    pygame.display.update()

## python -m pip install pygame
import pygame


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# نسخه اول بازی را به شکلی تغییر دادیم که اینبار یک توپ در صفحه به
# سمت بالا و پایین حرکت کند اما بتوانیم با کلیدهای سمت چپ و راست
# کیبورد توپ را بر روی محور ایکس حرکت دهیم
# حرکت توپ بر روی محور وآی بصورت اتوماتیک و این حرکت بر روی محور
# ایکس با کلید های کیبورد خواهد بود

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# یک پنجره میسازیم و عنوان و سایز آن را مشخص میکنیم
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Our Simple Game Part3")
clock = pygame.time.Clock()


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# جای توپ را در صفحه مختصات مشخص کرده و مشخص میکنیم با چه سرعتی بر
# روی هر محور جابجا شود
x, y, y_movement, x_movement = 245, 245, +10, 8


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
    # رویدادهای کیبورد را دریافت میکنیم، آیا کلید سمت چپ و راست
    # صدا زده شده اند یا خیر
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= x_movement
    if keys[pygame.K_RIGHT]:
        x += x_movement

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # شرطی که مشخص میکند توپ اجازه ندارد از صفحه بازی خارج شود
    # البته در محور ایکس
    if x > 500:
        x = 490
    if x < 0:
        x = 10

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # توپ بصورت اتوماتیک در محور وآی حرکت میکند و اگر به بالا یا
    # پایین صفحه برسید تغییر جهت میدهد
    y += y_movement
    if y > 500:
        y -= y_movement
        y_movement = -y_movement
    elif y < 0:
        y -= y_movement
        y_movement = -y_movement

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

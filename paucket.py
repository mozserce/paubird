import pygame
import random
import sys

# Başlat
pygame.init()
genislik, yukseklik = 1000, 600
ekran = pygame.display.set_mode((genislik, yukseklik))
saat = pygame.time.Clock()

# Renkler
beyaz = (255, 255, 255)
mavi = (117, 167, 150)

# Arkaplan
arka_plan = pygame.image.load("pictures/background.jpeg")
arka_plan = pygame.transform.scale(arka_plan, (genislik, yukseklik))

# Roket
roket_x = 300
roket_y = 300
roket_y_hiz = 0
yercekimi = 0.5
ziplama = -4   

roket_resmi = pygame.image.load("pictures/rocket.png")
roket_resmi = pygame.transform.scale(roket_resmi, (80, 80))

# Duvar
duvar_resmi = pygame.image.load("pictures/wall.png")
duvar_resmi = pygame.transform.scale(duvar_resmi, (60, 400))
duvarlar = []
duvar_genislik = 60
duvar_bosluk = 150

# Ufo
ufo_resmi = pygame.image.load("pictures/ufo.png") 
ufo_resmi = pygame.transform.scale(ufo_resmi, (80, 80))

ufo_var = False
ufo_x = genislik
ufo_y = random.randint(100, 500)
ufo_timer = 0
ufo_hiz = 5

ufo_patlama_animasyonu = False
ufo_patlama_index = 0
ufo_patlama_pos = (0, 0)

# Patlama Animasyonu
bonus_patlama_animasyonu = False
bonus_patlama_index = 0
bonus_patlama_pos = (0, 0)

patlama_resimleri = [pygame.image.load(f"pictures/Flash/flash{0}{i}.png") for i in range(8)]
patlama_resimleri = [pygame.transform.scale(img, (60, 60)) for img in patlama_resimleri]

# Ates Animasyonu
ates_resmi = [pygame.image.load(f"pictures/Flame/asd{i}.png") for i in range(9)]
ates_resmii = [pygame.transform.scale(img, (108, 60)) for img in ates_resmi]

# Bonus/(nisangah)

bonus_var = False
bonus_x = 1000
bonus_y = random.randint(100, 500)
bonus_size = 80
bonus_timer = 0

bonus_efekt_var = False
bonus_efekt_timer = 0
bonus_efekt_pos = (0, 0)

bonus_resmi = pygame.image.load("pictures/nisangah.png")
bonus_resmi = pygame.transform.scale(bonus_resmi, (bonus_size, bonus_size))

skor = 0
font = pygame.font.SysFont(None, 40, bold=True)
i = 0 

# GAME OVER
yazi = font.render("GAME OVER", True, beyaz)
buton_rect = pygame.Rect(400, 200, 200, 80)

# Your Score
yazi_skor = font.render("Your Score:", True, beyaz)
buton_skor = pygame.Rect(380, 125, 200, 80)


def yeni_duvar():
    yukseklik_duvar = random.randint(100, 400)
    duvarlar.append({'x': genislik, 'y': yukseklik_duvar})

yeni_duvar()

oyun_bitti = False
while True:
    i += 1
    ekran.blit(arka_plan, (0, 0))

    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if etkinlik.type == pygame.KEYDOWN and not oyun_bitti:
            if etkinlik.key == pygame.K_SPACE:
                roket_y_hiz = ziplama

    if oyun_bitti:
        pygame.draw.rect(ekran, mavi, buton_rect, border_radius=20)
        yazi_rect = yazi.get_rect(center=buton_rect.center)
        yazi_skor0 = yazi_skor.get_rect(center=buton_skor.center)
        ekran.blit(yazi, yazi_rect)
        ekran.blit(font.render("Your Score:  "+str(skor), True, beyaz), yazi_skor0)

    else:
        if bonus_patlama_animasyonu:
            bonus_patlama_index += 1
            if bonus_patlama_index >= len(patlama_resimleri):
                bonus_patlama_animasyonu = False

        if bonus_efekt_var:
            bonus_efekt_timer -= 1
            if bonus_efekt_timer <= 0:
                bonus_efekt_var = False

        bonus_timer += 1
        if bonus_timer > 300 and not bonus_var:
            bonus_var = True
            bonus_x = genislik
            bonus_y = random.randint(100, 500)
            bonus_timer = 0

        if bonus_var:
            bonus_x -= 4
            if bonus_x + bonus_size < 0:
                bonus_var = False

            roket_rect = pygame.Rect(roket_x, roket_y, 50, 50)
            bonus_rect = pygame.Rect(bonus_x, bonus_y, bonus_size, bonus_size)
            if roket_rect.colliderect(bonus_rect):
                en_yakin_duvar = None
                for duvar in duvarlar:
                    if duvar['x'] > roket_x:
                        en_yakin_duvar = duvar
                        break
                if en_yakin_duvar:
                    duvarlar.remove(en_yakin_duvar)
                skor += 3
                bonus_var = False
                bonus_patlama_animasyonu = True
                bonus_patlama_index = 0
                bonus_patlama_pos = (bonus_x, bonus_y)

        # UFO Yönetimi
        ufo_timer += 1
        if ufo_timer > 180 and not ufo_var:
            ufo_var = True
            ufo_x = genislik
            ufo_y = random.randint(100, 500)
            ufo_timer = 0

        if ufo_var:
            ufo_x -= ufo_hiz
            if ufo_x + 80 < 0:
                ufo_var = False

            roket_rect = pygame.Rect(roket_x, roket_y, 50, 50)
            ufo_rect = pygame.Rect(ufo_x, ufo_y, 80, 80)
            if roket_rect.colliderect(ufo_rect):
                ufo_var = False
                oyun_bitti = True
                ufo_patlama_animasyonu = True
                ufo_patlama_index = 0
                ufo_patlama_pos = (ufo_x, ufo_y)

        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_SPACE]:
            roket_y_hiz = ziplama

        roket_y_hiz += yercekimi
        roket_y += roket_y_hiz

        # Duvar Ekleme-Çıkarma İşlemleri
        for duvar in duvarlar:
            duvar['x'] -= 3

        if duvarlar[-1]['x'] < 500:
            yeni_duvar()

        if duvarlar[0]['x'] < -duvar_genislik:
            duvarlar.pop(0)

        if duvarlar[0]['x'] + 60 == 202:
            skor += 1

        for duvar in duvarlar:
            if duvar['x'] < roket_x + 50 < duvar['x'] + duvar_genislik:
                if roket_y < duvar['y'] or roket_y > duvar['y'] + duvar_bosluk:
                    oyun_bitti = True
        if roket_y > yukseklik or roket_y < 0:
            oyun_bitti = True

    # Ekrana Yazdırma
    ekran.blit(roket_resmi, (roket_x, roket_y))
    ekran.blit(ates_resmii[i % len(ates_resmii)], (roket_x - 93, roket_y + 8))

    if bonus_var:
        ekran.blit(bonus_resmi, (bonus_x, bonus_y))

    if bonus_patlama_animasyonu and bonus_patlama_index < len(patlama_resimleri):
        ekran.blit(patlama_resimleri[bonus_patlama_index], bonus_patlama_pos)

    for duvar in duvarlar:
        ust_duvar_yukseklik = duvar['y']
        alt_duvar_yukseklik = yukseklik - (duvar['y'] + duvar_bosluk)
        ust_duvar_y = duvar['y'] - 400
        alt_duvar_y = duvar['y'] + duvar_bosluk

        ekran.blit(duvar_resmi, (duvar['x'], ust_duvar_y))
        ekran.blit(pygame.transform.flip(duvar_resmi, False, True), (duvar['x'], alt_duvar_y))

    if ufo_var:
        ekran.blit(ufo_resmi, (ufo_x, ufo_y))

    if ufo_patlama_animasyonu and ufo_patlama_index < len(patlama_resimleri):
        ekran.blit(patlama_resimleri[ufo_patlama_index], ufo_patlama_pos)
        ufo_patlama_index += 1
        if ufo_patlama_index >= len(patlama_resimleri):
            ufo_patlama_animasyonu = False

    skor_yazi = font.render(f"Score: {skor}", True, beyaz)
    ekran.blit(skor_yazi, (10, 10))

    pygame.display.flip()
    saat.tick(60)
   
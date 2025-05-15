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
mavi = (0, 150, 255)
yesil = (0, 200, 0)
kirmizi = (255, 0, 0)
SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)
MAVI = (0, 150, 255)

# Oyuncu
kus_x = 300
kus_y = 300
kus_y_hiz = 0
yercekimi = 0.5
ziplama = -8    

ates_resmi =[pygame.image.load("newgame\\asd.png"),pygame.image.load("newgame\\asd0.png"),pygame.image.load("newgame\\asd1.png"),pygame.image.load("newgame\\asd2.png"),pygame.image.load("newgame\\asd3.png"),pygame.image.load("newgame\\asd4.png"),pygame.image.load("newgame\\asd5.png"),pygame.image.load("newgame\\asd6.png"),pygame.image.load("newgame\\asd7.png"),pygame.image.load("newgame\\asd8.png")] 
ates_resmii =[pygame.transform.scale(ates_resmi[0], (108, 36)),pygame.transform.scale(ates_resmi[1], (108, 36)),pygame.transform.scale(ates_resmi[2], (108, 36)),pygame.transform.scale(ates_resmi[3], (108, 36)),pygame.transform.scale(ates_resmi[4], (108, 36)),pygame.transform.scale(ates_resmi[5], (108, 36)),pygame.transform.scale(ates_resmi[6], (108, 36)),pygame.transform.scale(ates_resmi[7], (108, 36))]

ates_x = 195
ates_y = 295
ates_y_hiz = 0

# Borular
boru_genislik = 60
boru_bosluk = 150
borular = []

def yeni_boru():
    yukseklik = random.randint(100, 400)
    borular.append({'x': genislik, 'y': yukseklik})

# Başlangıç borusu
yeni_boru()

# Skor
skor = 0
font = pygame.font.SysFont(None, 40, bold=True)
i = 0 


# Dikdörtgen (oval kenarlı) GAMEOVER butonu
yazi = font.render("GAME OVER", True, beyaz)
buton_rect = pygame.Rect(400, 200, 200, 80)

#Yeniden Başlat Butonu 
yazi_try = font.render("TRY", True, beyaz)
buton_try = pygame.Rect(400, 280, 100, 40)

#Skor Butonu 
yazi_skor = font.render("Your Score:", True, SIYAH) 
buton_skor = pygame.Rect(400, 120, 200, 80)



# Oyun döngüsü
oyun_bitti = False
while True:
    i += 1
          
    ekran.fill(mavi)

    # Etkinlikler
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if etkinlik.type == pygame.KEYDOWN and not oyun_bitti:
            if etkinlik.key == pygame.K_SPACE:
                kus_y_hiz = ziplama
                ates_y_hiz = ziplama

    if oyun_bitti:
                   
        # Oval kenarlı dikdörtgen çiz
        pygame.draw.rect(ekran, yesil, buton_rect, border_radius=20)
        #pygame.draw.rect(ekran, kirmizi, buton_try, border_radius=30)
        # Yazıyı ortala
        yazi_rect = yazi.get_rect(center=buton_rect.center)
        #yazi_try0  = yazi_try.get_rect(center=buton_try.center)
        yazi_skor0 = yazi_skor.get_rect(center=buton_skor.center)
        ekran.blit(yazi, yazi_rect)
        #ekran.blit(yazi_try, yazi_try0)
        ekran.blit(font.render("Your Score:  "+str(skor), True, SIYAH), yazi_skor0)

    if not oyun_bitti:
        # Fizik
        kus_y_hiz += yercekimi
        kus_y += kus_y_hiz
        ates_y_hiz += yercekimi
        ates_y += ates_y_hiz

        # Boruların hareketi
        for boru in borular:
            boru['x'] -= 3 # oyunun temel hizi

        # Boru yenileme
        if borular[-1]['x'] < 500:  # burada borularin birbirleri arasindaki mesafeleri belirleniyor
            yeni_boru() 
            for boru in borular:
                print(boru)
            

        # Boru temizleme
        if borular[0]['x'] < -boru_genislik:
            borular.pop(0)
        
        if borular[0]['x'] + 60 == 202 : # skor kazanma olayi BURAYA BORULARIN ARASINA YAKINA BI SEY KONUP ORADAN GECERSE DAHA FAZLA SKOR ALINMASI SAGLANABILIR
            skor +=1

        # Çarpışma kontrolü
        for boru in borular:
            if boru['x'] < kus_x + 30 < boru['x'] + boru_genislik:
                if kus_y < boru['y'] or kus_y > boru['y'] + boru_bosluk:
                    oyun_bitti = True
        if kus_y > yukseklik or kus_y < 0:

            oyun_bitti = True

            

            # BIR END GAME EKLEMESI YAPILICAK

    # Oyuncu çiz
    pygame.draw.rect(ekran, kirmizi, (kus_x, kus_y, 30, 30))
    if i % 8 == 1 :
        ekran.blit(ates_resmii[0], (ates_x, ates_y))
    if i % 8 == 2 :
        ekran.blit(ates_resmii[1], (ates_x, ates_y))
    if i % 8 == 3 :
        ekran.blit(ates_resmii[2], (ates_x, ates_y))
    if i % 8 == 4 :
        ekran.blit(ates_resmii[3], (ates_x, ates_y))
    if i % 8 == 5 :
        ekran.blit(ates_resmii[4], (ates_x, ates_y))
    if i % 8 == 6 :
        ekran.blit(ates_resmii[5], (ates_x, ates_y))
    if i % 8 == 7 :
        ekran.blit(ates_resmii[6], (ates_x, ates_y))
    if i % 8 == 0 :
        ekran.blit(ates_resmii[7], (ates_x, ates_y))


    # Borular çiz
    for boru in borular:
        pygame.draw.rect(ekran, kirmizi, (boru['x'], 0, boru_genislik, boru['y']))
        pygame.draw.rect(ekran, kirmizi, (boru['x'], boru['y'] + boru_bosluk, boru_genislik, yukseklik))

    # Skor
    skor_yazi = font.render(f"Score: {skor}", True, kirmizi)
    
    ekran.blit(skor_yazi, (10, 10))

    # Ekranı güncelle
    pygame.display.flip()
    saat.tick(60)

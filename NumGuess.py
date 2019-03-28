# -*- coding: cp1251 -*-
import random, pygame, sys

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([200, 100])
Ahoy = pygame.mixer.Sound("Ahoy.wav")
Ahoy.set_volume(0.5)
WhatsYerGuess = pygame.mixer.Sound("WhatsYerGuess.wav")
WhatsYerGuess.set_volume(0.5)
TooLow = pygame.mixer.Sound("TooLow.wav")
TooLow.set_volume(0.5)
TooHigh = pygame.mixer.Sound("TooHigh.wav")
TooHigh.set_volume(0.5)
AvastGotIt = pygame.mixer.Sound("AvastGotIt.wav")
AvastGotIt.set_volume(0.5)
NoMore = pygame.mixer.Sound("NoMore.wav")
NoMore.set_volume(0.5)
secret = random.randint(1, 99)
guess = 0
tries = 0
print "�� �� ������! � ������� ����� �������, � � ���� ���� ������!"
print "��� ����� �� 1 �� 99. � ��� ���� 6 �������."
Ahoy.play()
pygame.time.delay(8000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running - False
    while guess != secret and tries < 6:
        WhatsYerGuess.play()
        guess = input("���� �������? ")
        if guess < secret:
            print "��� ������� ����, ���������� ���!"
            TooLow.play()
            pygame.time.delay(1800)
        elif guess > secret:
            print "��� ������� �����, ���������� �����!"
            TooHigh.play()
            pygame.time.delay(1800)
        tries = tries + 1

    if guess == secret:
        print "������! �� ������ ��� ������!"
        AvastGotIt.play()
        pygame.time.delay(3200)   # wait for the sound to finish playing
        running = False
    else:
        print "������� ���������!"
        NoMore.play()
        pygame.time.delay(3700)
        print "��� ����� ", secret
        running = False

pygame.quit()

#Bibliotecas
import pygame, sys, os, random
from pygame.locals import *


#Alinhamento de tela
os.environ['SDL_VIDEO_CENTERED'] = '1'

#musica e efeitos sonoros
pygame.init()
pygame.mixer.music.load('musica2.mp3')
pygame.mixer.music.play(-1)
pygame.event.wait()
pygame.mixer.music.set_volume(0.05)

#acertos e erros(sons)

moeda= pygame.mixer.Sound('smw_coin.wav')
erro= pygame.mixer.Sound('errou.wav')

#acertos e erros (imagens)
acertou = pygame.image.load('imagens/EducaDev/sistema/acertou.png.')



#Tela de seleção de disciplinas
def inicio1():
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 590))
    pygame.display.set_caption('EducaDevQuiz')



    #Cores
    preto = (0, 0, 0)

    #Imagens
    b1 = pygame.image.load('imagens/EducaDev/sistema/botao_grande.png')
    b2 = pygame.image.load('imagens/EducaDev/sistema/botao_grande.png')
    fundo = pygame.image.load('imagens/EducaDev/sistema/plano_fundo.png')
    voltar = pygame.image.load('imagens/EducaDev/sistema/seta.png')

    #Textos
    fonte1 = pygame.font.SysFont('Arial Black', 30)
    fonte2 = pygame.font.SysFont('Arial', 22)
    logica = fonte1.render('logica', 1, preto)
    matematica = fonte1.render('Matemática', 1, preto)
    menu = fonte2.render('Menu Principal', 1, preto)


    #Loop
    while True:

        #Eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        print('Voltar selecionado')
                    elif x > 100 and x < 350 and y > 330 and y < 430:
                        inicio2('logica')
                    elif x > 500 and x < 750 and y > 330 and y < 430:
                        inicio2('matemática')

                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        print('Menu Principal selecionado')

        #Objetos e tela
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(b1,(100, 330))
        b1.blit(logica, (75, 20))
        tela.blit(b2,(500, 330))
        b2.blit(matematica, (31, 20))
        tela.blit(menu, (725, 570))
        pygame.display.update()




#Tela de seleção de níveis
def inicio2(disciplina):
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('EducaDevQuiz')

    #Cores
    preto = (0, 0, 0,)

    #Imagens
    b1 = pygame.image.load('imagens/EducaDev/sistema/botao_pequeno.png')
    b2 = pygame.image.load('imagens/EducaDev/sistema/botao_pequeno.png')
    b3 = pygame.image.load('imagens/EducaDev/sistema/botao_pequeno.png')
    b4 = pygame.image.load('imagens/EducaDev/sistema/botao_pequeno.png')
    fundo = pygame.image.load('imagens/EducaDev/sistema/plano_fundo.png')
    voltar = pygame.image.load('imagens/EducaDev/sistema/seta.png')
    acertou= pygame.image.load('imagens/EducaDev/sistema/acertou.png')

    #Textos
    fonte1 = pygame.font.SysFont('Arial Black', 45)
    fonte2 = pygame.font.SysFont('Arial', 20)
    facil = fonte1.render('Fácil', 1, preto)
    medio = fonte1.render('Médio', 1, preto)
    dificil = fonte1.render('Difícil', 1, preto)
    ajuda = fonte1.render('Ajuda', 1, preto)
    menu = fonte2.render('Menu Principal', 1, preto)

    #Loop
    while True:
        
        #Eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        inicio1()
                    elif x > 150 and x < 350 and y > 305 and y < 385:
                        jogo(disciplina, 'fácil')
                    elif x > 500 and x < 700 and y > 305 and y < 385:
                        jogo(disciplina, 'médio')
                    elif x > 150 and x < 350 and y > 430 and y < 510:
                        jogo(disciplina, 'difícil')
                    elif x > 500 and x < 700 and y > 430 and y < 510:
                        ajuda1(disciplina)
                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        inicio1()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    ajuda1(disciplina)

        #Objetos e tela
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(b1,(150, 305))
        b1.blit(facil, (36, 2))
        tela.blit(b2, (500, 305))
        b2.blit(medio, (25, 2))
        tela.blit(b3, (150, 430))
        b3.blit(dificil, (26, 2))
        tela.blit(b4, (500, 430))
        b4.blit(ajuda, (28, 2))
        tela.blit(menu, (725, 570))
        pygame.display.update()

#Tela de ajuda
def ajuda1(disciplina):
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('EducaDevQuiz')

    #Cores
    preto = (0, 0, 0)

    #Imagens
    fundo = pygame.image.load('imagens/EducaDev/sistema/plano_fundo.png')
    voltar = pygame.image.load('imagens/EducaDev/sistema/seta.png')
    ajuda = pygame.image.load('imagens/EducaDev/sistema/ajuda.png')

    #Textos
    fonte = pygame.font.SysFont('Arial', 20)
    menu = fonte.render('Menu Principal', 1, preto)

    #Loop
    while True:

        #Eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        inicio2(disciplina)
                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        inicio1()

        #Objetos e tela
        pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(menu, (725, 570))
        tela.blit(ajuda, (50, 250))
        pygame.display.update()

#Jogo
def jogo(disciplina, nivel):
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('EducaDevQuiz')

    #Cores
    preto = (0, 0, 0)
    verde = (0, 255, 0)
    azul = (0, 78, 152)
    amarelo = (255, 238, 0)
    vermelho = (226, 0, 37)
    cor = preto

    #Imagens
    fundo = pygame.image.load('imagens/EducaDev/sistema/plano_fundo.png')
    voltar = pygame.image.load('imagens/EducaDev/sistema/seta.png')
    pista = pygame.image.load('imagens/EducaDev/sistema/pista.png')

    #Textos
    fonte = pygame.font.SysFont('Arial', 20)
    menu = fonte.render('Menu Principal', 1, preto)

    #pista
    posicoes = [(90, 290), (140, 290), (190, 290), (250, 290), (300, 290), (370, 290), (450, 290), (520, 290), (620, 290), (640, 290), (700, 290)]
    posicao = 0
    px = posicoes[0][0]
    py = posicoes[0][1]
    movimentos = ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']
    movimento = False

    #perguntas
    if disciplina == 'logica':
        if nivel == 'fácil':
            perguntas = {'1': [pygame.image.load('imagens/EducaDev/facil/logica/p1.png'), pygame.image.load('imagens/EducaDev/facil/logica/a1.png'), pygame.K_b],
                         '2': [pygame.image.load('imagens/EducaDev/facil/logica/p2.png'), pygame.image.load('imagens/EducaDev/facil/logica/a2.png'), pygame.K_a],
                         '3': [pygame.image.load('imagens/EducaDev/facil/logica/p3.png'), pygame.image.load('imagens/EducaDev/facil/logica/a3.png'), pygame.K_a],
                         '4': [pygame.image.load('imagens/EducaDev/facil/logica/p4.png'), pygame.image.load('imagens/EducaDev/facil/logica/a4.png'), pygame.K_d],
                         '5': [pygame.image.load('imagens/EducaDev/facil/logica/p5.png'), pygame.image.load('imagens/EducaDev/facil/logica/a5.png'), pygame.K_a],
                         '6': [pygame.image.load('imagens/EducaDev/facil/logica/p6.png'), pygame.image.load('imagens/EducaDev/facil/logica/a6.png'), pygame.K_a],
                         '7': [pygame.image.load('imagens/EducaDev/facil/logica/p7.png'), pygame.image.load('imagens/EducaDev/facil/logica/a7.png'), pygame.K_d],
                         '8': [pygame.image.load('imagens/EducaDev/facil/logica/p8.png'), pygame.image.load('imagens/EducaDev/facil/logica/a8.png'), pygame.K_c],
                         '9': [pygame.image.load('imagens/EducaDev/facil/logica/p9.png'), pygame.image.load('imagens/EducaDev/facil/logica/a9.png'), pygame.K_d],
                         '10': [pygame.image.load('imagens/EducaDev/facil/logica/p10.png'), pygame.image.load('imagens/EducaDev/facil/logica/a10.png'), pygame.K_b]}
        elif nivel == 'médio':
            perguntas = {'1': [pygame.image.load('imagens/EducaDev/medio/logica/p1.png'), pygame.image.load('imagens/EducaDev/medio/logica/a1.png'), pygame.K_c],
                         '2': [pygame.image.load('imagens/EducaDev/medio/logica/p2.png'), pygame.image.load('imagens/EducaDev/medio/logica/a2.png'), pygame.K_b],
                         '3': [pygame.image.load('imagens/EducaDev/medio/logica/p3.png'), pygame.image.load('imagens/EducaDev/medio/logica/a3.png'), pygame.K_b],
                         '4': [pygame.image.load('imagens/EducaDev/medio/logica/p4.png'), pygame.image.load('imagens/EducaDev/medio/logica/a4.png'), pygame.K_c],
                         '5': [pygame.image.load('imagens/EducaDev/medio/logica/p5.png'), pygame.image.load('imagens/EducaDev/medio/logica/a5.png'), pygame.K_b],
                         '6': [pygame.image.load('imagens/EducaDev/medio/logica/p6.png'), pygame.image.load('imagens/EducaDev/medio/logica/a6.png'), pygame.K_b],
                         '7': [pygame.image.load('imagens/EducaDev/medio/logica/p7.png'), pygame.image.load('imagens/EducaDev/medio/logica/a7.png'), pygame.K_a],
                         '8': [pygame.image.load('imagens/EducaDev/medio/logica/p8.png'), pygame.image.load('imagens/EducaDev/medio/logica/a8.png'), pygame.K_b],
                         '9': [pygame.image.load('imagens/EducaDev/medio/logica/p9.png'), pygame.image.load('imagens/EducaDev/medio/logica/a9.png'), pygame.K_a],
                         '10': [pygame.image.load('imagens/EducaDev/medio/logica/p10.png'), pygame.image.load('imagens/EducaDev/medio/logica/a10.png'), pygame.K_d]}
        elif nivel == 'difícil':
            perguntas = {'1': [pygame.image.load('imagens/EducaDev/dificil/logica/p1.png'), pygame.image.load('imagens/EducaDev/dificil/logica/a1.png'), pygame.K_a],
                         '2': [pygame.image.load('imagens/EducaDev/dificil/logica/p2.png'), pygame.image.load('imagens/EducaDev/dificil/logica/a2.png'), pygame.K_a],
                         '3': [pygame.image.load('imagens/EducaDev/dificil/logica/p3.png'), pygame.image.load('imagens/EducaDev/dificil/logica/a3.png'), pygame.K_a],
                         '4': [pygame.image.load('imagens/EducaDev/dificil/logica/p4.png'), pygame.image.load('imagens/EducaDev/dificil/logica/a4.png'), pygame.K_d],
                         '5': [pygame.image.load('imagens/EducaDev/dificil/logica/p5.png'), pygame.image.load('imagens/EducaDev/dificil/logica/a5.png'), pygame.K_a],
                         '6': [pygame.image.load('imagens/EducaDev/dificil/logica/p6.png'), pygame.image.load('imagens/EducaDev/dificil/logica/a6.png'), pygame.K_c],
                         '7': [pygame.image.load('imagens/EducaDev/dificil/logica/p7.png'), pygame.image.load('imagens/EducaDev/dificil/logica/a7.png'), pygame.K_d],
                         '8': [pygame.image.load('imagens/EducaDev/dificil/logica/p8.png'), pygame.image.load('imagens/EducaDev/dificil/logica/a8.png'), pygame.K_a],
                         '9': [pygame.image.load('imagens/EducaDev/dificil/logica/p9.png'), pygame.image.load('imagens/EducaDev/dificil/logica/a9.png'), pygame.K_a],
                         '10': [pygame.image.load('imagens/EducaDev/dificil/logica/p10.png'), pygame.image.load('imagens/EducaDev/dificil/logica/a10.png'), pygame.K_c]}
    elif disciplina == 'matemática':
        if nivel == 'fácil':
            perguntas = {'1': [pygame.image.load('imagens/EducaDev/facil/matematica/p1.png'), pygame.image.load('imagens/EducaDev/facil/matematica/a1.png'), pygame.K_b],
                         '2': [pygame.image.load('imagens/EducaDev/facil/matematica/p2.png'), pygame.image.load('imagens/EducaDev/facil/matematica/a2.png'), pygame.K_c],
                         '3': [pygame.image.load('imagens/EducaDev/facil/matematica/p3.png'), pygame.image.load('imagens/EducaDev/facil/matematica/a3.png'), pygame.K_c],
                         '4': [pygame.image.load('imagens/EducaDev/facil/matematica/p4.png'), pygame.image.load('imagens/EducaDev/facil/matematica/a4.png'), pygame.K_a],
                         '5': [pygame.image.load('imagens/EducaDev/facil/matematica/p5.png'), pygame.image.load('imagens/EducaDev/facil/matematica/a5.png'), pygame.K_d],
                         '6': [pygame.image.load('imagens/EducaDev/facil/matematica/p6.png'), pygame.image.load('imagens/EducaDev/facil/matematica/a6.png'), pygame.K_a],
                         '7': [pygame.image.load('imagens/EducaDev/facil/matematica/p7.png'), pygame.image.load('imagens/EducaDev/facil/matematica/a7.png'), pygame.K_c],
                         '8': [pygame.image.load('imagens/EducaDev/facil/matematica/p8.png'), pygame.image.load('imagens/EducaDev/facil/matematica/a8.png'), pygame.K_d],
                         '9': [pygame.image.load('imagens/EducaDev/facil/matematica/p9.png'), pygame.image.load('imagens/EducaDev/facil/matematica/a9.png'), pygame.K_c],
                         '10': [pygame.image.load('imagens/EducaDev/facil/matematica/p10.png'), pygame.image.load('imagens/EducaDev/facil/matematica/a10.png'), pygame.K_c]}
        elif nivel == 'médio':
            perguntas = {'1': [pygame.image.load('imagens/EducaDev/medio/matematica/p1.png'), pygame.image.load('imagens/EducaDev/medio/matematica/a1.png'), pygame.K_c],
                         '2': [pygame.image.load('imagens/EducaDev/medio/matematica/p2.png'), pygame.image.load('imagens/EducaDev/medio/matematica/a2.png'), pygame.K_c],
                         '3': [pygame.image.load('imagens/EducaDev/medio/matematica/p3.png'), pygame.image.load('imagens/EducaDev/medio/matematica/a3.png'), pygame.K_a],
                         '4': [pygame.image.load('imagens/EducaDev/medio/matematica/p4.png'), pygame.image.load('imagens/EducaDev/medio/matematica/a4.png'), pygame.K_b],
                         '5': [pygame.image.load('imagens/EducaDev/medio/matematica/p5.png'), pygame.image.load('imagens/EducaDev/medio/matematica/a5.png'), pygame.K_b],
                         '6': [pygame.image.load('imagens/EducaDev/medio/matematica/p6.png'), pygame.image.load('imagens/EducaDev/medio/matematica/a6.png'), pygame.K_a],
                         '7': [pygame.image.load('imagens/EducaDev/medio/matematica/p7.png'), pygame.image.load('imagens/EducaDev/medio/matematica/a7.png'), pygame.K_a],
                         '8': [pygame.image.load('imagens/EducaDev/medio/matematica/p8.png'), pygame.image.load('imagens/EducaDev/medio/matematica/a8.png'), pygame.K_b],
                         '9': [pygame.image.load('imagens/EducaDev/medio/matematica/p9.png'), pygame.image.load('imagens/EducaDev/medio/matematica/a9.png'), pygame.K_a],
                         '10': [pygame.image.load('imagens/EducaDev/medio/matematica/p10.png'), pygame.image.load('imagens/EducaDev/medio/matematica/a10.png'), pygame.K_c]}
        elif nivel == 'difícil':
            perguntas = {'1': [pygame.image.load('imagens/EducaDev/dificil/matematica/p1.png'), pygame.image.load('imagens/EducaDev/dificil/matematica/a1.png'), pygame.K_b],
                         '2': [pygame.image.load('imagens/EducaDev/dificil/matematica/p2.png'), pygame.image.load('imagens/EducaDev/dificil/matematica/a2.png'), pygame.K_d],
                         '3': [pygame.image.load('imagens/EducaDev/dificil/matematica/p3.png'), pygame.image.load('imagens/EducaDev/dificil/matematica/a3.png'), pygame.K_b],
                         '4': [pygame.image.load('imagens/EducaDev/dificil/matematica/p4.png'), pygame.image.load('imagens/EducaDev/dificil/matematica/a4.png'), pygame.K_d],
                         '5': [pygame.image.load('imagens/EducaDev/dificil/matematica/p5.png'), pygame.image.load('imagens/EducaDev/dificil/matematica/a5.png'), pygame.K_c],
                         '6': [pygame.image.load('imagens/EducaDev/dificil/matematica/p6.png'), pygame.image.load('imagens/EducaDev/dificil/matematica/a6.png'), pygame.K_b],
                         '7': [pygame.image.load('imagens/EducaDev/dificil/matematica/p7.png'), pygame.image.load('imagens/EducaDev/dificil/matematica/a7.png'), pygame.K_c],
                         '8': [pygame.image.load('imagens/EducaDev/dificil/matematica/p8.png'), pygame.image.load('imagens/EducaDev/dificil/matematica/a8.png'), pygame.K_d],
                         '9': [pygame.image.load('imagens/EducaDev/dificil/matematica/p9.png'), pygame.image.load('imagens/EducaDev/dificil/matematica/a9.png'), pygame.K_b],
                         '10': [pygame.image.load('imagens/EducaDev/dificil/matematica/p10.png'), pygame.image.load('imagens/EducaDev/dificil/matematica/a10.png'), pygame.K_a]}
    sorteio = random.randint(1, len(perguntas))
    sorteados = []
    sorteados.append(sorteio)
    colorm = colort = correto = incorreto = False
    
    #Loop
    while True:

        #Eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x > 48 and x < 802 and y > 435 and y < 463 and colort == False:
                    colorm = True
                    evento = 'a'
                elif x > 48 and x < 802 and y > 464 and y < 492 and colort == False:
                    colorm = True
                    evento = 'b'
                elif x > 48 and x < 802 and y > 493 and y < 521 and colort == False:
                    colorm = True
                    evento = 'c'
                elif x > 48 and x < 802 and y > 522 and y < 550 and colort == False:
                    colorm = True
                    evento = 'd'
                else:
                    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                    colorm = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        inicio2(disciplina)
                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        inicio1()
                    elif x > 48 and x < 802 and y > 435 and y < 463:
                        colort = True
                        evento = 'a'
                        if perguntas[str(sorteio)][2] == pygame.K_a:
                            correto = True
                        else:
                            incorreto = True
                    elif x > 48 and x < 802 and y > 464 and y < 492:
                        colort = True
                        evento = 'b'
                        if perguntas[str(sorteio)][2] == pygame.K_b:
                            correto = True
                        else:
                            incorreto = True
                    elif x > 48 and x < 802 and y > 493 and y < 521:
                        colort = True
                        evento = 'c'
                        if perguntas[str(sorteio)][2] == pygame.K_c:
                            correto = True
                        else:
                            incorreto = True
                    elif x > 48 and x < 802 and y > 522 and y < 550:
                        colort = True
                        evento = 'd'
                        if perguntas[str(sorteio)][2] == pygame.K_d:
                            correto = True
                        else:
                            incorreto = True
            if event.type == pygame.KEYDOWN:
                if posicao != len(posicoes) - 1:
                    if event.key == K_a:
                        colort = True
                        evento = 'a'
                        if perguntas[str(sorteio)][2] == pygame.K_a:
                            correto = True
                        else:
                            incorreto = True
                    elif event.key == K_b:
                        colort = True
                        evento = 'b'
                        if perguntas[str(sorteio)][2] == pygame.K_b:
                            correto = True
                        else:
                            incorreto = True
                    elif event.key == K_c:
                        colort = True
                        evento = 'c'
                        if perguntas[str(sorteio)][2] == pygame.K_c:
                            correto = True
                        else:
                            incorreto = True
                    elif event.key == K_d:
                        colort = True
                        evento = 'd'
                        if perguntas[str(sorteio)][2] == pygame.K_d:
                            correto = True
                        else:
                            incorreto = True
                    else:
                        fim1(disciplina)
            if correto == True:
                cor = verde
                if movimentos[posicao] == 'b':
                    a = py
                    b = posicoes[posicao + 1][1]
                    tipo = 'b'
                    moeda.play()
                elif movimentos[posicao] == 'c':
                    b = py
                    a = posicoes[posicao + 1][1]
                    tipo = 'c'
                    moeda.play()

                elif movimentos[posicao] == 'd':
                    a = px
                    b = posicoes[posicao + 1][0]
                    tipo = 'd'
                    moeda.play()
                elif movimentos[posicao] == 'e':
                    b = px
                    a = posicoes[posicao + 1][0]
                    tipo = 'e'
                    moeda.play()
                movimento = True
                posicao += 1
                pygame.event.set_blocked(pygame.KEYDOWN)
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                correto = False
            if incorreto == True:
                if posicao != 0:
                    cor = vermelho
                    if movimentos[posicao - 1] == 'b':
                        b = py
                        a = posicoes[posicao - 1][1]
                        tipo = 'c'
                        erro.play()
                    elif movimentos[posicao - 1] == 'c':
                        a = py
                        b = posicoes[posicao - 1][1]
                        tipo = 'b'
                        erro.play()
                    elif movimentos[posicao - 1] == 'd':
                        b = px
                        a = posicoes[posicao - 1][0]
                        tipo = 'e'
                        erro.play()
                    elif movimentos[posicao - 1] == 'e':
                        a = px
                        b = posicoes[posicao - 1][0]
                        tipo = 'e'
                        erro.play()
                    movimento = True
                    posicao -= 1
                    pygame.event.set_blocked(pygame.KEYDOWN)
                    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                else:
                    sorteio = random.randint(1, len(perguntas))
                    while sorteio in sorteados:
                        if len(sorteados) == len(perguntas):
                            sorteados = []
                        sorteio = random.randint(1, len(perguntas))
                    sorteados.append(sorteio)
                    pygame.draw.rect(tela, vermelho, (px, py, 20, 20))
                    pygame.display.update()
                    pygame.time.delay(500)
                incorreto = False

        #Objetos e tela
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(menu, (725, 570))
        tela.blit(perguntas[str(sorteio)][0], (40, 40))
        tela.blit(pista, (40, 185))
        tela.blit(perguntas[str(sorteio)][1], (40, 425))
        pygame.draw.rect(tela, cor, (px, py, 19, 19))
        if movimento == True:
            if tipo == 'b':
                if a + 5 > b:
                    py += 1
                    a = py
                else:
                    py += 5
                    a = py
            elif tipo == 'c':
                if a + 5 > b:
                    py -= 1
                    b = py
                else:
                    py -= 5
                    b = py
            elif tipo == 'd':
                if a + 5 > b:
                    px += 1
                    a = px
                else:
                    px += 5
                    a = px
            elif tipo == 'e':
                if a + 5 > b:
                    px -= 1
                    b = px
                else:
                    px -= 5
                    b = px
            if a == b:
                cor = preto
                movimento = False
                colort = False
                colotm = True
                pygame.event.set_allowed(None)
                if posicao == len(posicoes) - 1:
                    i = 0
                    pygame.display.update()
                    while i < 50:
                        pygame.time.delay(300)
                        pygame.display.update()
                        i += 10
                    fim1(disciplina)
                sorteio = random.randint(1, len(perguntas))
                while sorteio in sorteados:
                    if len(sorteados) == len(perguntas):
                        sorteados = []
                    sorteio = random.randint(1, len(perguntas))
                sorteados.append(sorteio)
        if colorm == True:
            if evento == 'a':
                pygame.draw.circle(tela, azul, (67, 447), 13)
            elif evento == 'b':
                pygame.draw.circle(tela, amarelo, (67, 477), 13)
            elif evento == 'c':
                pygame.draw.circle(tela, vermelho, (67, 507), 13)
            elif evento == 'd':
                pygame.draw.circle(tela, verde, (67, 537), 13)
            if movimento == True and colort == True:
                colorm = False
        if colort == True:
            if evento == 'a':
                pygame.draw.circle(tela, azul, (67, 447), 13)
            elif evento == 'b':
                pygame.draw.circle(tela, amarelo, (67, 477), 13)
            elif evento == 'c':
                pygame.draw.circle(tela, vermelho, (67, 507), 13)
            elif evento == 'd':
                pygame.draw.circle(tela, verde, (67, 537), 13)
            if posicao == 0 and movimento == False:
                colort = False
        pygame.display.update()

def fim1(disciplina):
    #Inicialização
    pygame.init()
    tela = pygame.display.set_mode((850, 600))
    pygame.display.set_caption('EducaDevQuiz')

    #Cores
    preto = (0, 0, 0)

    #Imagens
    estrela = pygame.image.load('imagens/EducaDev/sistema/0estrelas.png')
    parabens = pygame.image.load('imagens/EducaDev/sistema/parabens.png')
    fim = pygame.image.load('imagens/EducaDev/sistema/fim.png')
    fundo = pygame.image.load('imagens/EducaDev/sistema/fundoliso.png')
    voltar = pygame.image.load('imagens/EducaDev/sistema/seta.png')

    #Textos
    fonte1 = pygame.font.SysFont('Arial Black', 25)
    fonte2 = pygame.font.SysFont('Arial', 20)
    avalie = fonte1.render('Gostou do jogo?', 1, preto)
    menu = fonte2.render('Menu Principal', 1, preto)

    votado = False

    #Loop
    while True:

        #Eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if votado == False:
                    if x > 275 and x < 335 and y > 490 and y < 560:
                        estrela = pygame.image.load('imagens/EducaDev/sistema/1estrelas.png')
                    elif x > 335 and x < 395 and y > 490 and y < 560:
                        estrela = pygame.image.load('imagens/EducaDev/sistema/2estrelas.png')
                    elif x > 395 and x < 455 and y > 490 and y < 560:
                        estrela = pygame.image.load('imagens/EducaDev/sistema/3estrelas.png')
                    elif x > 455 and x < 515 and y > 490 and y < 560:
                        estrela = pygame.image.load('imagens/EducaDev/sistema/4estrelas.png')
                    elif x > 515 and x < 575 and y > 490 and y < 560:
                        estrela = pygame.image.load('imagens/EducaDev/sistema/5estrelas.png')
                    else:
                        estrela = pygame.image.load('imagens/EducaDev/sistema/0estrelas.png')
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 10 and x < 40 and y > 10 and y < 40:
                        inicio2(disciplina)
                    elif x > 725 and x < 830 and y > 570 and y < 590:
                        inicio1()
                    if votado == False:
                        if x > 275 and x < 335 and y > 490 and y < 560:
                            estrela = pygame.image.load('imagens/EducaDev/sistema/1estrelas.png')
                            votado = True
                        elif x > 335 and x < 395 and y > 490 and y < 560:
                            estrela = pygame.image.load('imagens/EducaDev/sistema/2estrelas.png')
                            votado = True
                        elif x > 395 and x < 455 and y > 490 and y < 560:
                            estrela = pygame.image.load('imagens/EducaDev/sistema/3estrelas.png')
                            votado = True
                        elif x > 455 and x < 515 and y > 490 and y < 560:
                            estrela = pygame.image.load('imagens/EducaDev/sistema/4estrelas.png')
                            votado = True
                        elif x > 515 and x < 575 and y > 490 and y < 560:
                            estrela = pygame.image.load('imagens/EducaDev/sistema/5estrelas.png')
                            votado = True

        #Objetos e tela
        #pygame.time.Clock().tick(30)
        tela.blit(fundo, (0, 0))
        tela.blit(voltar, (10, 10))
        tela.blit(parabens, (217, 60))
        tela.blit(fim, (40, 180))
        tela.blit(avalie, (315, 450))
        pygame.draw.rect(tela, preto, (275, 485, 300, 5))
        tela.blit(estrela, (275, 490))
        tela.blit(menu, (725, 570))
        pygame.display.update()

inicio1()

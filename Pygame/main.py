import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA = 800   # Largura da tela
ALTURA = 600    # Altura da tela
tela = pygame.display.set_mode((LARGURA, ALTURA)) # Cria a tela e define o tamanho
pygame.display.set_caption("Jogo Básico Pygame") # Define o título da janela

# Cores RGB
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)

# Posição e tamanho do retângulo
retangulo_x = 0
retangulo_y = 0
# Tamanho do retângulo
retangulo_largura = 50
retangulo_altura = 50
velocidade = 5

# Relógio para controlar o FPS
clock = pygame.time.Clock()

# Loop principal do jogo
rodando = True
while rodando:
    # Processa eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Lógica do jogo
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        retangulo_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        retangulo_x += velocidade
    if teclas[pygame.K_UP]:
        retangulo_y -= velocidade
    if teclas[pygame.K_DOWN]:
        retangulo_y += velocidade
    if teclas[pygame.K_ESCAPE]:
        rodando = False
    if teclas[pygame.K_SPACE]:
        retangulo_x = 0
        retangulo_y = 0
        
    # Limita o retângulo dentro da tela
    retangulo_x = max(0, min(retangulo_x, LARGURA - retangulo_largura))
    retangulo_y = max(0, min(retangulo_y, ALTURA - retangulo_altura))
    
    # Renderização
    tela.fill(PRETO)  # Preenche a tela com preto
    
    # Desenha o retângulo
    pygame.draw.rect(tela, AZUL, (retangulo_x, retangulo_y, retangulo_largura, retangulo_altura))
    
    # Atualiza a tela
    pygame.display.flip()
    
    # Controla a taxa de quadros por segundo
    clock.tick(60)

# Encerra o Pygame
pygame.quit()
sys.exit()
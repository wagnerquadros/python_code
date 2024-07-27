import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das constantes
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Criação da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Definição das fontes
font = pygame.font.SysFont(None, 50)

# Classe para representar a bola
class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
    
    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), BALL_RADIUS)
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        if self.y <= BALL_RADIUS or self.y >= HEIGHT - BALL_RADIUS:
            self.dy *= -1
    
    def collide_with_paddle(self, paddle):
        if (self.x - BALL_RADIUS <= paddle.x + PADDLE_WIDTH and
            paddle.y <= self.y <= paddle.y + PADDLE_HEIGHT):
            self.dx *= -1

# Classe para representar as paletas
class Paddle:
    def __init__(self, x):
        self.x = x
        self.y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    
    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))
    
    def move_up(self):
        self.y -= PADDLE_SPEED
        if self.y < 0:
            self.y = 0
    
    def move_down(self):
        self.y += PADDLE_SPEED
        if self.y > HEIGHT - PADDLE_HEIGHT:
            self.y = HEIGHT - PADDLE_HEIGHT

# Função para desenhar a pontuação
def draw_score(score):
    score_text = font.render(str(score), True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

def main():
    clock = pygame.time.Clock()
    ball = Ball()
    left_paddle = Paddle(20)
    right_paddle = Paddle(WIDTH - PADDLE_WIDTH - 20)
    score_left = 0
    score_right = 0

    # Loop principal do jogo
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    left_paddle.move_up()
                elif event.key == pygame.K_s:
                    left_paddle.move_down()
                elif event.key == pygame.K_UP:
                    right_paddle.move_up()
                elif event.key == pygame.K_DOWN:
                    right_paddle.move_down()
        
        # Movimentação da bola
        ball.move()
        ball.collide_with_paddle(left_paddle)
        ball.collide_with_paddle(right_paddle)

        # Verificação dos pontos
        if ball.x <= 0:
            score_right += 1
            ball = Ball()
        elif ball.x >= WIDTH:
            score_left += 1
            ball = Ball()

        # Limpeza da tela
        screen.fill(BLACK)

        # Desenho dos elementos
        ball.draw()
        left_paddle.draw()
        right_paddle.draw()
        draw_score(score_left)
        draw_score(score_right)

        # Atualização da tela
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

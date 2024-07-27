import pygame
import sys
import numpy as np

class CPU:
    def __init__(self):
        self.pc = 0
        self.sp = 0
        self.a = 0
        self.x = 0
        self.y = 0
        self.status = 0
        self.memory = [0] * 65536

    def load_rom(self, rom_data, start_address):
        for i in range(len(rom_data)):
            self.memory[start_address + i] = rom_data[i]

    def read_memory(self, address):
        return self.memory[address]

    def write_memory(self, address, value):
        self.memory[address] = value

    def fetch(self):
        opcode = self.read_memory(self.pc)
        self.pc += 1
        return opcode

    def execute(self, opcode):
        pass  # Implemente a interpretação dos opcodes aqui

class GPU:
    def __init__(self, screen):
        self.screen = screen
        self.memory = [0] * 160 * 192  # Ajustando o tamanho da lista de memória
        self.palette = [(0, 0, 0), (255, 255, 255)]
        self.scanline = 00

    def write_memory(self, address, value):
        self.memory[address] = value

    def draw_scanline(self):
        for x in range(160):
            pixel_value = self.memory[self.scanline * 160 + x]
            color = self.palette[pixel_value]
            self.screen.set_at((x, self.scanline), color)

    def render_frame(self):
        for scanline in range(192):
            self.draw_scanline()
            self.scanline = (self.scanline + 1) % 192
            pygame.display.flip()

class Sound:
    def __init__(self):
        pygame.mixer.init()
        self.sample_rate = 44100
        self.volume = 0.5
        self.channel = pygame.mixer.Channel(0)

    def play_tone(self, frequency, duration):
        num_samples = int(self.sample_rate * duration / 1000)
        decay = np.exp(-np.arange(num_samples) / (self.sample_rate * 0.5))
        samples = (np.sin(2 * np.pi * frequency * np.arange(num_samples) / self.sample_rate) * decay).astype(np.int16)
        sound = pygame.sndarray.make_sound(samples)
        self.channel.set_volume(self.volume)
        self.channel.play(sound)

    def play_sound_effect(self, effect):
        if effect == "explosion":
            self.play_tone(440, 100)
        elif effect == "shoot":
            self.play_tone(220, 50)

class Emulator:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Atari 2600 Emulator")

        self.clock = pygame.time.Clock()
        self.running = True
        self.keys = {}
        self.cpu = CPU()
        self.gpu = GPU(self.screen)
        self.sound = Sound()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.keys[event.key] = True
            elif event.type == pygame.KEYUP:
                self.keys[event.key] = False

    def load_rom(self, rom_file):
        with open(rom_file, "rb") as file:
            rom_data = file.read()
        self.cpu.load_rom(rom_data, 0x8000)

    def run(self):
        while self.running:
            self.handle_events()

            if self.keys.get(pygame.K_ESCAPE):
                self.running = False

            self.screen.fill((0, 0, 0))
            self.gpu.render_frame()
            pygame.display.flip()  # Atualiza a tela após renderizar o frame
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    emulator = Emulator()
    rom_file = "roms/Megamania.bin"  # Substitua "my_rom.bin" pelo caminho da sua ROM
    emulator.load_rom(rom_file)
    emulator.run()

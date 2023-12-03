import threading
import time
import random


class Interrupt:
    def __init__(self, type, priority):
        self.type = type
        self.priority = priority


class OperatingSystem:
    def __init__(self):
        self.interrupt_vector = []
        self.lock = threading.Lock()
        self.busy = False

    def handle_interrupt(self, interrupt):
        with self.lock:
            self.interrupt_vector.append(interrupt)
            self.interrupt_vector.sort(key=lambda x: x.priority, reverse=True)

    def run(self):
        while True:
            with self.lock:
                if not self.interrupt_vector:
                    continue

                interrupt = self.interrupt_vector.pop(0)
                print(f"Handling {interrupt.type} interrupt with priority {interrupt.priority}")
                self.busy = True
                time.sleep(random.uniform(0.5, 2.0))
                self.busy = False


def generate_interrupts():
    os = OperatingSystem()
    os_thread = threading.Thread(target=os.run)
    os_thread.start()

    types = ["Disk", "Network", "USB", "Mouse"]
    priorities = [1, 2, 3, 4]

    for i in range(10):
        interrupt_type = random.choice(types)
        priority = random.choice(priorities)
        interrupt = Interrupt(interrupt_type, priority)
        print(f"Generating {interrupt.type} interrupt with priority {interrupt.priority}")
        os.handle_interrupt(interrupt)
        time.sleep(random.uniform(0.1, 0.5))


if __name__ == "__main__":
    generate_interrupts_thread = threading.Thread(target=generate_interrupts)
    generate_interrupts_thread.start()
    generate_interrupts_thread.join()

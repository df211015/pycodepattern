from facadePattern.cpu import CPU
from facadePattern.disk import Disk
from facadePattern.memory import Memory


class Computer:
    def __init__(self):
        self._cpu = CPU()
        self._memory = Memory()
        self._disk = Disk()

    def run(self):
        self._cpu.run()
        self._memory.run()
        self._disk.run()

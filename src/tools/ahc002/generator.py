from pathlib import Path

from ..interface.generator import IGenerator
from .io import Input


class Generator(IGenerator):
    def __init__(self, seed: int):
        super().__init__()
        self.seed = seed

    def _gen(self):
        input_path = Path(f"./in/{self.seed:04}.txt")
        s = ""
        with open(input_path, "r") as f:
            for line in f:
                s += line
        return Input.from_str(s)


def gen_input(seed: int):
    return Generator(seed)()

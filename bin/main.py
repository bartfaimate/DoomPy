import pygame as pg
import sys
from pathlib import Path
sys.path.append(Path(__file__).parents[1].joinpath("lib").as_posix())


from doompy.game import Game


if __name__ == '__main__':
    game = Game()
    game.run()

from typing import NoReturn

from dice_game_abstract.dice_base import Dice
from dice_game_abstract.dice_board_base import DiceBoardBase


class DummyDice(DiceBoardBase):

    def check_winner(self) -> bool:
        return len(set(dice.face for dice in self._dice)) == 1

    def roll(self) -> None:
        if self._position:
            for pos in self._position:
                self._dice[pos].roll()
            self._position = set()
        else:
            for dice in self._dice:
                dice.roll()

    def plus(self, adjust: int) -> "DiceBoardBase":
        self._adjust = adjust
        return self

    def pos_to_be_rolled(self, pos: list[int]) -> "DiceBoardBase" | NoReturn:
        
        try:
            if not all(0 <= n - 1 < len(self._dice) for n in pos):
                raise IndexError("Some positions are out of range")
            else:
                self._position = set([i - 1 for i in pos])  # remove duplicate values
                return self
        except IndexError as e:
            print(e)   
            return NoReturn 

    def __add__(self, other: Dice) -> None:
        if isinstance(other(), Dice):  # type: ignore
            self._dice += [other()]  # type: ignore

    @property
    def total(self) -> int:
        return sum(self._dice) + self._adjust  # type: ignore

    @property  # getter
    def dice(self) -> list[Dice]:
        return self._dice

    @dice.setter  # setter
    def dice(self, _) -> NoReturn:
        raise NotImplementedError  # keyword in Python

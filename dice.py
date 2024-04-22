from random import randint
from typing import Union

from dice_game_abstract.dice_base import Dice


class D4(Dice):
    def roll(self) -> None:
        self.face = randint(1, 4)

    def __add__(self, other: Union["Dice", int]) -> Union[int, None]:  # type: ignore
        return super().__add__(other)

    def __radd__(self, other: Union["Dice", int]) -> Union[int, None]:  # type: ignore
        return super().__add__(other)


class D6(Dice):
    def roll(self) -> None:
        self.face = randint(1, 6)

    def __add__(self, other: Union["Dice", int]) -> Union[int, None]:  # type: ignore
        return super().__add__(other)

    def __radd__(self, other: Union["Dice", int]) -> Union[int, None]:  # type: ignore
        return super().__add__(other)


class D8(Dice):
    def roll(self) -> None:
        self.face = randint(1, 8)

    def __add__(self, other: Union["Dice", int]) -> Union[int, None]:  # type: ignore
        return super().__add__(other)

    def __radd__(self, other: Union["Dice", int]) -> Union[int, None]:  # type: ignore
        return super().__add__(other)

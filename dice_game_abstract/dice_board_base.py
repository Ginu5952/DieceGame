import abc

from .dice_base import Dice


class DiceBoardBase(abc.ABC):
    def __init__(self, *dice_class: type[Dice]) -> None:
        self._dice: list[Dice] = [dice() for dice in dice_class]  # type: ignore
        self._adjust: int = 0
        self._position: set[int] = set()

    @abc.abstractmethod
    def check_winner(self) -> bool: ...

    @property
    @abc.abstractmethod
    def total(self) -> int: ...

    @abc.abstractmethod
    def roll(self) -> None: ...

    @abc.abstractmethod
    def plus(self, adjust: int) -> "DiceBoardBase": ...

    @abc.abstractmethod
    def pos_to_be_rolled(self, pos: list[int]) -> "DiceBoardBase": ...

    @abc.abstractmethod
    def __add__(self, other: Dice) -> None: ...

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        dice_classes = ", ".join(
            [dice.__class__.__name__ for dice in self._dice]
        )  # D4, D6, D8
        return f"{cls_name}({dice_classes})"

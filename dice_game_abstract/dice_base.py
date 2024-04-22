import abc
from typing import Union  # |


class Dice(abc.ABC):
    def __init__(self) -> None:
        self.face: int
        self.roll()

    @abc.abstractmethod
    def roll(self) -> None: ...  #d4,d6,d8

    def __repr__(self) -> str:
        return str(self.face)

    def __add(self, other: Union["Dice", int]) -> Union[int, None]:  # type: ignore
        if isinstance(other, int):
            return self.face + other
        elif isinstance(other, Dice):  # type: ignore
            return self.face + other.face
        return None

    @abc.abstractmethod
    def __add__(self, other: Union["Dice", int]) -> Union[int, None]:  # type: ignore
        return self.__add(other)  # type: ignore

    @abc.abstractmethod
    def __radd__(self, other: Union["Dice", int]) -> Union[int, None]:  # type: ignore
        return self.__add(other)  # type: ignore

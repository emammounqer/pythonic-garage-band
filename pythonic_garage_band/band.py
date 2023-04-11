from abc import ABC, abstractmethod
from typing import ClassVar


class Musician(ABC):

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"musician named {self.name}, playing {self.get_instrument()}"

    def play_solo(self):
        return f"{self.name} plays solo {self.get_instrument()}"

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_instrument(self):
        pass


class Guitarist(Musician):

    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"Guitarist('{self.name}')"

    def get_instrument(self):
        return "Guitar"


class Bassist(Musician):

    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"Bassist('{self.name}')"

    def get_instrument(self):
        return "Bass"


class Drummer(Musician):

    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"Drummer('{self.name}')"

    def get_instrument(self):
        return "Drums"


class Band:

    instances: ClassVar[list['Band']] = []

    def __init__(self, name: str, members: list[Musician] = []):
        self.name = name
        self.members = members

        self.instances.append(self)

    def play_solos(self):
        for member in self.members:
            print(member.play_solo())

    def __str__(self):
        return f"Band {self.name} has {len(self.members)} members"

    def __repr__(self):
        return f"Band('{self.name}', {self.members})"

    @classmethod
    def to_list(cls):
        return cls.instances

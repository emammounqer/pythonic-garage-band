from abc import ABC, abstractmethod
from typing import ClassVar


class Musician(ABC):

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def get_instrument(self) -> str:
        pass

    @abstractmethod
    def play_solo(self) -> str:
        pass


class Guitarist(Musician):

    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):

    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):

    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"


class Band:

    instances: ClassVar[list['Band']] = []

    def __init__(self, name: str, members: list[Musician] = []):
        self.name = name
        self.members = members

        Band.instances.append(self)

    def play_solos(self):
        return [member.play_solo() for member in self.members]

    def __str__(self):
        return f"Band {self.name} has {len(self.members)} members"

    def __repr__(self):
        return f"Band('{self.name}', {self.members})"

    @classmethod
    def to_list(cls):
        return cls.instances

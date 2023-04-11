from typing import ClassVar
from musician import Musician


class Band:

    all_bands: ClassVar[list['Band']] = []

    def __init__(self, name: str, members: list[Musician] = []):
        self.name = name
        self.members = members

        self.all_bands.append(self)

    def play_solos(self):
        for member in self.members:
            print(member.play_solo())

    def __str__(self):
        return f"Band {self.name} has {len(self.members)} members"

    def __repr__(self):
        return f"Band('{self.name}', {self.members})"

    @classmethod
    def to_list(cls):
        return cls.all_bands

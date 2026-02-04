

from dataclasses import dataclass

@dataclass
class Artista:
    name: str
    id: int
    opere: int

    def __str__(self):
        return f"{self.id} ({self.name})"

    def __repr__(self):
        return f"{self.id} ({self.name})"

    def __hash__(self):
        return hash(self.id)

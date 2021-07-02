import enum

class SiteEnum(enum.Enum):
    Alternate = 1
    Coolblue = 2
    Azerty = 3
    Megekko = 4

    def __str__(self) -> str:
        return str(self.value)
class Animals:
    def __init__(self, name="", weight=0):
        self.name = name
        self.weight = weight

    def feed(self, value):
        self.weight += value
        return "покормили"

    def do_voice(self):
        pass

    def do_personal_action(self):
        pass


class EggLaying(Animals):  # несущие яйца
    def do_eggs(self):
        return "несет яйца"

    def do_personal_action(self):
        return self.do_eggs() + ", " + self.do_voice()


class Shearing(Animals):  # Стригущиеся
    def do_shave(self):
        return "cтрижется"

    def do_personal_action(self):
        return self.do_shave() + ", " + self.do_voice()


class Milking(Animals):  # доящиеся
    def do_milk(self):
        return "доится"

    def do_personal_action(self):
        return self.do_milk() + ", " + self.do_voice()


class Chicken(EggLaying):
    representative = "Курица"

    def do_voice(self):
        return "говорит Кококо"


class Goose(EggLaying):
    representative = "Гусь"

    def do_voice(self):
        return "говорит Га-га"


class Duck(EggLaying):
    representative = "Утка"

    def do_voice(self):
        return "говорит Кря-кря"


class Sheep(Shearing, Milking):
    representative = "Овца"

    def do_voice(self):
        return "говорит Бееее"

    def do_personal_action(self):
        return self.do_shave() + " и " + self.do_milk() + ", " + self.do_voice()


class Cow(Milking):
    representative = "Корова"

    def do_voice(self):
        return "говорит Муууу"


class Goat(Milking, Shearing):
    representative = "Коза"

    def do_voice(self):
        return "говорит Мееее"

    def do_personal_action(self):
        return self.do_shave() + " и " + self.do_milk() + ", " + self.do_voice()


feed_value = 2
farm = [
    Chicken("Ко-ко", 6),
    Chicken("Кукареку", 7),
    Goose("Белый", 12),
    Goose("Серый", 14),
    Duck("Кряква", 8),
    Sheep("Шон", 80),
    Sheep("Долли", 90),
    Cow("Лепешка", 150),
    Goat("Дереза", 60),
    Goat("Копытце", 70),
]

max_weight = sum_weight = 0
for animal in farm:
    print(
        f'{animal.representative} "{animal.name}" - это животное, которое {animal.do_personal_action()}, вес = {animal.weight}, и мы его {animal.feed(feed_value)} на {feed_value}'
    )
    sum_weight += animal.weight
    if animal.weight > max_weight:
        max_weight = animal.weight
        represent = animal.representative
print(f"Вес всех животных = {sum_weight}")
print(f"Самое тяжелое животное - это {represent} с весом = {max_weight}")
# Задача №1 "Ферма Дядюшки Джо"

# Родительский класс "Домашние животные"

class Pets:
    def __init__(self, kind, name, animal_says, weight_anim):
        self.kind = kind
        self.name = name
        self.animal_says = animal_says
        self.weight = weight_anim

    def set_feed(self, food):
        self.weight += food
        return self.kind + " " + self.name + " накормлена"

    def get_kind(self):
        return self.kind

    def get_name(self):
        return self.name

    def get_animal_says(self):
        return self.animal_says

    def get_weight(self):
        return self.weight
    

class Goose(Pets):
    
    def __init__(self, kind, name, animal_says, weight_anim, product):
        Pets.__init__(self, kind, name, animal_says, weight_anim)
        self.product = product

    def get_product(self):
        return self.product


class Cow(Pets):

    def __init__(self, kind, name, animal_says, weight_anim, product):
        Pets.__init__(self, kind, name, animal_says, weight_anim)
        self.product = product

    def get_product(self):
        return self.product
    

class Sheep(Pets):

    def __init__(self, kind, name, animal_says, weight_anim, product):
        Pets.__init__(self, kind, name, animal_says, weight_anim)
        self.product = product

    def get_product(self):
        return self.product
    

class Chicken(Pets):

    def __init__(self, kind, name, animal_says, weight_anim, product):
        Pets.__init__(self, kind, name, animal_says, weight_anim)
        self.product = product

    def get_product(self):
        return self.product


class Goat(Pets):

    def __init__(self, kind, name, animal_says, weight_anim, product):
        Pets.__init__(self, kind, name, animal_says, weight_anim)
        self.product = product

    def get_product(self):
        return self.product
    

class Duck(Pets):

    def __init__(self, kind, name, animal_says, weight_anim, product):
        Pets.__init__(self, kind, name, animal_says, weight_anim)
        self.product = product

    def get_product(self):
        return self.product
    

animal_dict = {'Серый': Goose("Гусь", "Серый", "га-га-га", 3.8, "яйца"),
               'Белый': Goose("Гусь", "Белый", "га-га-га", 2.8, "яйца"),
               'Манька': Cow("Корова", "Манька", "муууу", 720, "молоко"),
               'Барашек': Sheep("Баран", "Барашек", "беэээ", 160, "шерсть"),
               'Кудрявый': Sheep("Баран", "Кудрявый", "беэээ", 160, "шерсть"),
               'Ко-ко': Chicken("Курица", "Ко-ко", "ко-ко- ко", 2.8, "яйца"),
               'Кукареку': Chicken("Курица", "Кукареку", "ко-ко- ко", 2.8, "яйца"),
               'Рога': Goat("Коза", "Рога", "меэээээ", 170, "молоко"),
               'Копыта': Goat("Коза", "Копыта", "меэээ", 170, "молоко"),
               'Кряква': Duck("Утка", "Кряква", "кря-кря-кря", 3.1, "яйца")}

for anim in animal_dict:
    kind_anim = animal_dict[anim].get_kind()
    name_anim = animal_dict[anim].get_name()
    animal_says_anim = animal_dict[anim].get_animal_says()
    weight_anim_anim = animal_dict[anim].get_weight()
    product_anim = animal_dict[anim].get_product()
    print(f"{kind_anim} по имени {name_anim} говорит {animal_says_anim}\nвесит {weight_anim_anim} кг. "
          f"и дает {product_anim}\n")

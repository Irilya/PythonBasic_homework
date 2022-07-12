class Aqua:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Shtorm('Шторм')
        elif isinstance(other, Fire):
            return Steam('Пар')
        elif isinstance(other, Earth):
            return Mud('Грязь')
        else:
            return None


class Air:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Воздух'

    def __add__(self, other):
        if isinstance(other, Aqua):
            return Shtorm('Шторм')
        elif isinstance(other, Fire):
            return Lightning("Молния")
        elif isinstance(other, Earth):
            return Dust('Пыль')
        elif isinstance(other, Lightning):
            return BallLightning('Шаровая молния')
        else:
            return None


class Fire:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Огонь'

    def __add__(self, other):
        if isinstance(other, Aqua):
            return Steam('Пар')
        elif isinstance(other, Air):
            return Lightning("Молния")
        elif isinstance(other, Earth):
            return Lava('Лава')
        elif isinstance(other, Lightning):
            return Explosion('Взрыв')
        else:
            return None


class Earth:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Земля'

    def __add__(self, other):
        if isinstance(other, Aqua):
            return Mud('Грязь')
        elif isinstance(other, Air):
            return Dust('Пыль')
        elif isinstance(other, Fire):
            return Lava('Лава')
        else:
            return None


class Hurricane:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Жуткий ураган'

    def __add__(self, other):
        return None


class Dust:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Пыль'

    def __add__(self, other):
        return None


class Lightning:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Молния'

    def __add__(self, other):
        if isinstance(other, Shtorm):
            return Hurricane('Ураган')
        elif isinstance(other, Air):
            return BallLightning('Шаровая молния')
        elif isinstance(other, Fire):
            return Explosion('Взрыв')
        else:
            return None


class BallLightning:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'***Искрящая шаровая молния***'

    def __add__(self, other):
        return None


class Explosion:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'***<Бах-Бух Взрыв Бух-Бах>***'

    def __add__(self, other):
        return None


class Shtorm:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Шторм'

    def __add__(self, other):
        if isinstance(other, Lightning):
            return Hurricane('Ураган')
        else:
            return None


class Steam:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Пар'

    def __add__(self, other):
        return None


class Mud:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Грязь'

    def __add__(self, other):
        return None


class Lava:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Лава>'

    def __add__(self, other):
        return None


a1 = Lava('Лава')
a2 = Steam('Пар')
a3 = a1 + a2
c1 = Lightning('Молния')
c2 = Air('Воздух')
c3 = c1 + c2
b1 = Fire('Огонь')
b2 = Lightning('Молния')
b3 = b2 + b1
print(a1, '+', a2, '=', a3)
print(c1, '+', c2, '=', c3)
print(b1, '+', b2, '=', b3)
# ААААААААА!!!!  Какая классная штука!!!

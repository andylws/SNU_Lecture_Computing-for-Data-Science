'''P1'''


class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other):
        return self.area > other.area

    def population_density(self):
        return self.population / self.area


'''P2'''


class Continent:
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries

    def total_population(self):
        tot = 0
        for i in self.countries:
            tot += i.population
        return tot


'''P3'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist_sq(p1, p2):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2


class Shape:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def is_square(self):
        d2 = dist_sq(self.p1, self.p2)  # from p1 to p2
        d3 = dist_sq(self.p1, self.p3)  # from p1 to p3
        d4 = dist_sq(self.p1, self.p4)  # from p1 to p4
        if d2 == 0 or d3 == 0 or d4 == 0:
            return False
        if d2 == d3 and 2 * d2 == d4 and 2 * dist_sq(self.p2, self.p4) == dist_sq(self.p2, self.p3):
            return True
        if d3 == d4 and 2 * d3 == d2 and 2 * dist_sq(self.p3, self.p2) == dist_sq(self.p3, self.p4):
            return True
        if d2 == d4 and 2 * d2 == d3 and 2 * dist_sq(self.p2, self.p3) == dist_sq(self.p2, self.p4):
            return True
        return False


'''P4'''


class Calculator:
    def __init__(self):
        self.result = 0
        self.op = '+'  # 맨 처음 입력하는 숫자는 더해야 함
        self.num = '0'  # 숫자 기록
        self.is_num = True  # 이전에 클릭한 것이 숫자인지 아닌지

    def digit(self, num):
        self.num += str(num)
        self.is_num = True

    def plus(self):
        # 이전에 클릭한 것이 숫자인데 + 혹은 -를 누르면
        # 그 숫자 이전의 + 혹은 -를 반영해야함
        if self.is_num == True:
            if self.op == '+':
                self.result += int(self.num)
            else:
                self.result -= int(self.num)
            # 반영했으니 숫자는 다시 0으로
            self.num = '0'
        self.op = '+'
        self.is_num = False

    def minus(self):
        # plus와 마찬가지로 동작
        if self.is_num == True:
            if self.op == '+':
                self.result += int(self.num)
            else:
                self.result -= int(self.num)
            self.num = '0'
        self.op = '-'
        self.is_num = False

    def clear(self):
        self.result = 0
        self.op = '+'
        self.num = '0'
        self.is_num = True

    def equal(self):
        if self.op == '+':
            self.result += int(self.num)
        else:
            self.result -= int(self.num)
        return self.result

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Shape:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def getDistanceList(self):
        distance_list = []
        points = [self.p1, self.p2, self.p3, self.p4]

        for i in range(len(points)):
            j = len(points) - 1
            while j > i:
                distance = ((points[i].x - points[j].x)**2 +
                            (points[i].y - points[j].y)**2)**0.5
                distance_list.append(distance)
                j = j - 1

        return distance_list

    def is_square(self):
        distance_list = self.getDistanceList()

        if 0 in distance_list:
            return False

        num_of_same_d = []
        for distance in distance_list:
            num_of_same_d.append(distance_list.count(distance))
        num_of_same_d.sort()

        if num_of_same_d == [2, 2, 4, 4, 4, 4]:
            return True
        else:
            return False

        return

        # return: boolean

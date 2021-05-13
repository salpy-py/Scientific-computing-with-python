import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        data_list = list(kwargs.keys())
        req_lst = list(kwargs.values())
        for y in range(len(data_list)):
            for x in range(req_lst[y]):
                self.contents.append(data_list[y])

    def draw(self, number):
        num_list = list()
        if number > len(self.contents):
            return self.contents
        else:
            for x in range(number):
                random_range = random.randrange(len(self.contents))
                num_list.append(self.contents.pop(random_range))
            self.contents = self.contents
            x = sorted(num_list)
            return x


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    list_r = list()
    for k, v in expected_balls.items():
        for _ in range(v):
            list_r.append(k)
    filter = []
    for x in range(num_experiments):
        exp_copy = copy.deepcopy(hat)
        result = exp_copy.draw(num_balls_drawn)
        my_dictionary = dict()
        number_list = []
        for item in result:
            k, v = f'{item}', result.count(item)
            my_dictionary[k] = v
        name = list(my_dictionary.keys())
        canti = list(my_dictionary.values())
        for y in range(len(name)):
            for x in range(canti[y]):
                number_list.append(name[y])
        filter.append(sorted(number_list))

    M = 0
    for xa in filter:
        i = 0
        res_while = []
        while i < len(list_r):
            if list_r[i] in xa:
                xa.pop(xa.index(list_r[i]))
                res_while.append(True)
            else:
                res_while.append(False)
            i += 1
        if False not in res_while:
            M += 1
    return float(M/num_experiments)


# calling funtions and creating objects
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
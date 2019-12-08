'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''
import collections
from collections import namedtuple
from ways import load_map_from_csv
import random
import csv

JUNCTION_NUMBER_INDEX = 0
JUNCTION_LINKS_INDEX = 3
LINK_TARGER_INDEX = 1


def create_100_problems(junctions):
    problems = []
    for i in range(100):
        random_junction = random.choice(junctions)[JUNCTION_NUMBER_INDEX]
        random_steps = 1  # random.randrange(100, 200)
        target_junction = go_n_steps(junctions, random_junction, random_steps)

        problems.append((random_junction, target_junction))
    return problems

    # for junction in junctions:
    #     links = junction[JUNCTION_LINKS_INDEX]
    #     random_neighbor = random.choice(links)[LINK_TARGER_INDEX]
    #     print(junction[0], random_neighbor)
    #     pass


def go_n_steps(junctions, junction_number, n):
    print(junction_number, end=",")
    cur_junction_number = junction_number
    for i in range(n):
        junction = junctions[cur_junction_number]
        links = junction[JUNCTION_LINKS_INDEX]
        cur_junction_number = random.choice(links)[
            LINK_TARGER_INDEX]  # change the current junction number to its neighbor
    print(cur_junction_number)
    return cur_junction_number


def save_to_csv(sources_and_targets_list):
    writer = csv.writer(open("q3answer/problems.csv", 'w', newline=''))
    for source, target in sources_and_targets_list:
        writer.writerow((source, target))

    print("done! :P")


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    print("hi")
    roads = load_map_from_csv()
    junctions = roads.junctions()
    problems = create_100_problems(junctions)
    save_to_csv(problems)
print(neighbors)

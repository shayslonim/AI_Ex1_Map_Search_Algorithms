'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''
import collections
from collections import namedtuple
from ways import load_map_from_csv


# def helper_count_links(junctions):
#     LINKS_INDEX = 3
#     LINK_SOURCE, LINK_TARGET = 0, 1
#     links_count = 0
#     # calculate number of links
#     for junction in junctions:
#         link_list = junction[LINKS_INDEX]
#         for link in link_list:
#             # print("This is the link")
#             # print(link)
#             source, target = link[LINK_SOURCE], link[LINK_TARGET]
#             if source < target:
#                 links_count += 1
#     # finish calculation number of links
#     return links_count


def helper_outgoing_branching_factor(junctions):
    LINKS_INDEX = 3
    branching_factors = [len(junction[LINKS_INDEX]) for junction in junctions]
    minimal = min(branching_factors)
    maximal = max(branching_factors)
    average = sum(branching_factors) / len(branching_factors)
    # for junction in junctions:
    #     links = junction[LINKS_INDEX]
    #     branching_factor = len(links)
    #     if min is None or branching_factor > min:
    #         min =
    return (maximal, minimal, average)


def helper_link_distance(junctions):
    LINKS_INDEX = 3
    DISTANCE_INDEX = 2
    branching_factors = [link[DISTANCE_INDEX] for junction in junctions for link in junction[LINKS_INDEX]]
    minimal = min(branching_factors)
    maximal = max(branching_factors)
    average = sum(branching_factors) / len(branching_factors)
    # for junction in junctions:
    #     links = junction[LINKS_INDEX]
    #     branching_factor = len(links)
    #     if min is None or branching_factor > min:
    #         min =
    return (maximal, minimal, average)


def helper_link_type_histogram(junctions):
    LINKS_INDEX = 3
    TYPE_INDEX = 3
    # links = [link for junction in junctions for link in junction[LINKS_INDEX]]
    histogram = collections.Counter()
    #   for (link in links):
    for junction in junctions:
        for link in junction[LINKS_INDEX]:
            road_type = link[TYPE_INDEX]
            histogram[road_type] += 1
    return dict(histogram)


def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])

    junctions = roads.junctions()
    links_count = len([link for junction in junctions for link in junction])  # helper_count_links(junctions)
    return {
        'Number of junctions': len(junctions),
        'Number of links': links_count,
        'Outgoing branching factor': helper_outgoing_branching_factor(junctions),
        'Link distance': helper_link_distance(junctions),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram': helper_link_type_histogram(junctions),  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    print_stats()

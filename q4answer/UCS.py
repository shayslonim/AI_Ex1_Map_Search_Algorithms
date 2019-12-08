from queue import PriorityQueue

JUNCTION_NUMBER_INDEX = 0
LINKS_INDEX = 3
TARGET_INDEX = 1


# def best_first_graph_search(start_junction, goal_junction, f):
#     frontier = PriorityQueue(f)  # Priority Queue
#     frontier.put(start_junction)
#     closed_list = set()
#
#     while frontier:
#         cur_junction = frontier.get()
#         if cur_junction[JUNCTION_NUMBER_INDEX] == goal_junction[JUNCTION_NUMBER_INDEX]:
#             return cur_junction
#         closed_list.add(cur_junction.state)
#         for child in cur_junction.expand(problem):
#             if child.state not in closed_list and child not in frontier:
#                 frontier.put(child)
#             elif child in frontier and f(child) < frontier[child]:
#                 del frontier[child]
#                 frontier.put(child)
#     return None

def junction_neighbors(junctions, junction):
    # Explanation:
    # for every link in the junction, get the neighbors' index, using that index return the neighbor junction itself.
    # link[TARGET_INDEX] is each neighbor's index
    # Therefore:
    # junctions[link[TARGET_INDEX] is the neighbor itself
    return [junctions[link[TARGET_INDEX]] for link in junction[LINKS_INDEX]]


def ucs(junctions_collection, start_junction, goal_junction, cost_function):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start_junction, None))

    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)

            if node == goal_junction:
                return node
            for neighbor in junction_neighbors(junctions_collection, node):
                if neighbor not in visited:
                    total_cost = cost + cost_function(node, neighbor)
                    queue.put((total_cost, neighbor, node))

if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1


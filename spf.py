#!/usr/bin/python3

#        |----------|     |--------|                    #
#        |Costa Rica|--2--|Colombia|\                   #
#        |----------|     |--------| 6                  #
#            /       \         |      \                 #
# |-------| 1         \        |       \                #
# | Mexico|/           1       |        \|---------|    #
# |-------|\            \      1        /|Venezuela|    #
#           2            \     |       / |---------|    #
#            \            \    |      /                 #
#          |-------|      |--------| 2                  #
#          |  Peru |---1--| Chile  |/                   #
#          |-------|      |--------|                    #


def dijsktra(nodes,links, initial):
    current_node = initial
    shortest_paths = {initial: (None, 0)}
    visited = []
    while current_node not in visited:
        visited.append(current_node)
        destinations = nodes[current_node]
        weight_to_current_node = shortest_paths[current_node][1]
        for next_node in destinations:
            weight = links[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        next_destinations = {}
        for node in shortest_paths:
            if node not in visited:
                next_destinations[node] = shortest_paths[node]
        if not next_destinations:
            return shortest_paths
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    return shortest_paths

nodes = {
    'mexico': ['costa_rica', 'peru'],
    'costa_rica': ['mexico', 'colombia', 'chile'],
    'peru': ['mexico', 'chile'], 
    'colombia': ['costa_rica', 'chile','venezuela'], 
    'venezuela': ['colombia', 'chile'], 
    'chile': ['colombia', 'venezuela', 'peru']
    }

links = {
    ('mexico', 'costa_rica'): 1,
    ('costa_rica', 'mexico'): 1,
    ('mexico', 'peru'): 2,
    ('peru', 'mexico'): 2,
    ('costa_rica','colombia'): 2,
    ('colombia', 'costa_rica'): 2,
    ('costa_rica','chile'): 1,
    ('chile', 'costa_rica'): 1,
    ('colombia', 'chile'): 1,
    ('chile', 'colombia'): 1,
    ('venezuela', 'chile'): 2,
    ('chile', 'venezuela'): 2,
    ('peru', 'chile'): 1,
    ('chile', 'peru'): 1,
    ('venezuela', 'colombia'): 6,
    ('colombia', 'venezuela'): 6,
    }

shortest_paths = dijsktra(nodes,links,'mexico')
for i in shortest_paths.items():
    print(i)

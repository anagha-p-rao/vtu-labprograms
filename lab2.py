 def Cost(H, condition, weight = 1):
    cost = {}
    if 'AND' in condition:
        AND_nodes = condition['AND']
        Path_A = ' AND '.join(AND_nodes)
        PathA = sum(H[node]+weight for node in AND_nodes)
        cost[Path_A] = PathA

    if 'OR' in condition:
        OR_nodes = condition['OR']
        Path_B =' OR '.join(OR_nodes)
        PathB = min(H[node]+weight for node in OR_nodes)
        cost[Path_B] = PathB
    return cost


# Update the cost
def update_cost(H, Conditions, weight=1):
    Main_nodes = list(Conditions.keys()) # [A, B, C, D, G]
    Main_nodes.reverse()
    least_cost= {}
    for key in Main_nodes:
        condition = Conditions[key]
        print(key,':', Conditions[key],'>>>', Cost(H, condition, weight)) # printing 
        c = Cost(H, condition, weight) 
        print(c, key)
        H[key] = min(c.values())
        least_cost[key] = Cost(H, condition, weight)
    return least_cost


# Print the shortest path
def shortest_path(Start,Updated_cost, H):
    Path = Start
    if Start in Updated_cost.keys():
        Min_cost = min(Updated_cost[Start].values())
        key = list(Updated_cost[Start].keys())
        values = list(Updated_cost[Start].values())
        Index = values.index(Min_cost)

        # FIND MINIMIMUM PATH KEY
        Next = key[Index].split()
        # ADD TO PATH FOR OR PATH
        if len(Next) == 1:
            Start =Next[0]
            Path += ' = ' +shortest_path(Start, Updated_cost, H)

        # ADD TO PATH FOR AND PATH
        else:
            Path +='=('+key[Index]+') '
            Start = Next[0]
            Path += '[' +shortest_path(Start, Updated_cost, H) + ' + '
            Start = Next[-1]
            Path += shortest_path(Start, Updated_cost, H) + ']'
    return Path

# Heuristic values of Nodes 
H1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1}

Conditions = {
'A': {'AND': ['B', 'C'],'OR': ['D']},
'B': {'OR': ['G', 'H']},
'C': {'OR': ['J']},
'D': {'AND': ['E', 'F']},
'G': {'OR': ['I']}
}

# weight
weight = 1
# Updated cost
print('Updated Cost :')
Updated_cost = update_cost(H1, Conditions, weight=1)

print('\nShortest Path :\n',shortest_path('A', Updated_cost,H1))

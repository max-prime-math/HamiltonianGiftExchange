import networkx as nx
import matplotlib.pyplot as plt
import math

family = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
badpairs = [('A', 'B'), ('D', 'C'),('G', 'H'), ('E', 'F'), ('B','A'), ('C','D'),('H','G'), ('F','E')]
year2020 = [
    ('A', 'C'), 
    ('B', 'G'), 
    ('C', 'H'),
    ('D', 'B'), 
    ('E', 'A'), 
    ('G', 'E'), 
    ('H', 'D')
]

year2021 = [
    ('A', 'H'), 
    ('B', 'E'), 
    ('C', 'A'), 
    ('D','F'), 
    ('E', 'G'), 
    ('F', 'C'), 
    ('G', 'D'), 
    ('H', 'B')
]

year2022 = [
    ('A', 'E'), 
    ('B', 'D'), 
    ('C', 'G'), 
    ('D', 'A'), 
    ('E', 'H'), 
    ('F', 'B'), 
    ('G', 'F'), 
    ('H', 'C')
]

year2023 = [
    ('A', 'D'), 
    ('D', 'E'), 
    ('E', 'C'), 
    ('C', 'B'), 
    ('B', 'H'), 
    ('H', 'F'), 
    ('F', 'G'), 
    ('G', 'A')
]

prevYears = [year2023,year2022,year2021,year2020]

graph = nx.DiGraph()

# Add nodes to the graph
graph.add_nodes_from(family)

# Add directed edges from each node to every other node
for i in range(len(family)):
    for j in range(len(family)):
        if i != j:
            graph.add_edge(family[i], family[j])

# Delete edges in badpairs
for edge in badpairs:
    graph.remove_edge(*edge)

# Remove pairs from previous years
for year in prevYears:
    for edge in year:
        graph.remove_edge(*edge)

nx.draw(graph, with_labels=True, arrows=True)
plt.show()

# Big program


def find_hamiltonian_cycle(graph, start_node, current_node, visited, path):
    visited[current_node] = True
    path.append(current_node)

    if len(path) == len(graph):
        # Check if the last node has an edge to the starting node
        if graph.has_edge(current_node, start_node):
            path.append(start_node)
            return True

    for neighbor in graph.successors(current_node):
        if not visited[neighbor]:
            if find_hamiltonian_cycle(graph, start_node, neighbor, visited, path):
                return True

    visited[current_node] = False
    path.pop()
    return False

def find_hamiltonian_cycle_wrapper(graph):
    visited = {node: False for node in graph}
    path = []

    # Try to find a Hamiltonian cycle starting from each node
    for node in graph:
        if find_hamiltonian_cycle(graph, node, node, visited, path):
            return path

    return None

cycle = find_hamiltonian_cycle_wrapper(graph)

if cycle:
    print('Hamiltonian Cycle:', cycle)
else:
    print('No Hamiltonian Cycle found.')

def remove_last_element(lst):
    if lst:
        lst.pop()

def visualize_path_with_graph(graph, path):
    pos = nx.circular_layout(graph)  # Circular layout for nodes

    # Draw the graph
    nx.draw_networkx(graph, pos, with_labels=True)

    # Highlight the nodes and edges in the path
    path_nodes = set(path)
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    path_edges.append((path[-1], path[0]))  # Add the edge back to the starting node for a cycle

    nx.draw_networkx_nodes(graph, pos, nodelist=path_nodes, node_color='r')
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='r', width=2.0)

    # Display the plot
    plt.axis('off')
    plt.show()

def visualize_path(graph, path):
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    path_edges.append((path[-1], path[0]))  # Add edge from last node to first node to complete the cycle

    path_graph = nx.DiGraph()
    path_graph.add_edges_from(path_edges)

    num_nodes = len(path)
    angle = 2 * math.pi / num_nodes

    # Compute the positions of nodes on a circle
    pos = {node: (math.cos(i * angle), math.sin(i * angle)) for i, node in enumerate(path)}

    # Draw only the node labels
    nx.draw_networkx_labels(graph, pos, labels={node: node for node in path}, font_color='k')

    # Draw the subgraph with only the path edges
    nx.draw_networkx_edges(
        path_graph,
        pos,
        edge_color='blue',
        width=1,
        arrows=True,
        connectionstyle='arc3,rad=0.1',
        arrowstyle='-|>',
        arrowsize=10,
    )

    # Display the plot
    plt.axis('off')
    plt.show()


def generate_relationships(path):
    relationships = []

    for i in range(len(path) - 1):
        relationships.append(f'{path[i]} gets {path[i+1]}')

    relationships.append(f'{path[-1]} gets {path[0]}')

    print(relationships)

def generate_ordered_pairs(path):
    ordered_pairs = []

    for i in range(len(path) - 1):
        ordered_pairs.append((path[i], path[i + 1]))

    # Add the pair between the last and first element to complete the cycle
    ordered_pairs.append((path[-1], path[0]))

    print(ordered_pairs)

generate_ordered_pairs(cycle[0:8])
generate_relationships(cycle[0:8])
visualize_path(graph,cycle[0:8])

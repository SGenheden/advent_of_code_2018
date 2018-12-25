
import networkx as nx

from utils import read_input, define_grid


tools_allowed = {
    0: [0, 1],
    1 : [1, 2],
    2: [0, 2]
}


def define_graph(grid):
    graph = nx.Graph()
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            tools = tools_allowed[grid[x, y]]
            graph.add_node((x, y, tools[0]))
            graph.add_node((x, y, tools[1]))
            graph.add_edge((x, y, tools[0]), (x, y, tools[1]), weight=7)
    add_edges(grid, graph)
    return graph


def add_edges(grid, graph):
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            target = grid[x, y]
            if x < grid.shape[0] - 1:
                source = grid[x+1, y]
                for toola in tools_allowed[source]:
                    for toolb in tools_allowed[target]:
                        if toola == toolb:
                            graph.add_edge((x, y, toola), (x+1, y, toolb), weight=1)
            if y < grid.shape[1] - 1:
                source = grid[x, y+1]
                for toola in tools_allowed[source]:
                    for toolb in tools_allowed[target]:
                        if toola == toolb:
                            graph.add_edge((x, y, toola), (x, y+1, toolb), weight=1)


if __name__ == "__main__":
    depth, targetx, targety = read_input()
    grid = define_grid(targetx, targety, depth, padding=10)
    graph = define_graph(grid)
    p = nx.shortest_path(graph, (0,0,0), (targetx, targety,0), weight='weight', method='bellman-ford')
    duration = sum([graph.edges[v, u]['weight'] for v, u in zip(p[0:-1], p[1:])])
    print(f"The shortest duration is {duration}")

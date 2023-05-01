'''
graph: 
vertex(vertices):
edge(edges):
adjacent:
'''
from typing import Iterable

class Vertex:
    def __init__(self, val, adjacent:dict=None):
        self.val = val
        self.adjacent = {} if adjacent is None else adjacent

    def get_adjacent(self, adj_vertex):
        '''
        check if adjacent vertex
        return edge attributes if they are adjacent
        '''
        return self.adjacent.get(adj_vertex)
    
    def set_adjacent(self, adj_vertax, edge):
        if adj_vertax not in self.adjacent:
            self.adjacent[adj_vertax] = edge
    
    def remove_adjacent(self, adj_vertax)->bool:
        if adj_vertax in self.adjacent:
            del self.adjacent[adj_vertax]
            return True
        return False


class Edge:
    def __init__(self, **kwargs):
        # default all connections are equal
        self._dist = 1
        for k, v in kwargs.items():
            setattr(self, k, float(v))


class WeightedGraph:
    def __init__(self):
        '''
        key: vertex, value: vertices
        '''
        self.nodes = {}

    def get_node_values(self):
        return list(self.nodes)

    def get_nodes(self):
        return list(self.nodes.values())
    
    def get_node(self, val):
        return self.nodes.get(val)

    def delete_vertex(self, val)->bool:
        '''
        '''
        if val in self.nodes:
            del self.nodes[val]
            return True
        return False
        
    def add_vertex(self, val)->Vertex:
        '''
        add new vertex if that doesn't exist
        return new vertex or old vertex
        '''
        if val not in self.nodes:
            self.nodes[val] = Vertex(val)
        return self.nodes[val]

    def add_adjacent_pair(self, val, adj_val, **kwargs)->Edge:
        '''
        add new vertex if that doesn't exist
        add adjacent if that exists but new edges are added
        **kwargs are attributes of edges
        '''
        node = self.add_vertex(val)
        adj = self.add_vertex(adj_val)
        edge = Edge(**kwargs)
        node.set_adjacent(adj, edge)
        return edge

    def remove_adjacent(self, val1, val2):
        '''
        only remove connection
        don't remove nodes pair
        '''
        if val1 in self.nodes and val2 in self.nodes:
            ver1 = self.nodes[val1]
            ver2 = self.nodes[val2]
            return ver1.remove_adjacent(ver2)
        return False

    def get_adjacents(self, val)->list:
        if val in self.nodes:
            return self.nodes[val].adjacent
        return None
    
    def feed(self, adj_pairs:list, directed=False):
        '''
        add adjacent pairs into graph
        '''
        for val1, val2 in adj_pairs:
            self.add_adjacent_pair(val1, val2)
            if not directed:
                self.add_adjacent_pair(val2, val1)

    def feed_weighted(self, adj_pairs:list, directed=False):
        '''
        add adjacent pairs into graph
        '''
        for val1, val2, weight in adj_pairs:
            self.add_adjacent_pair(val1, val2, weight=weight)
            if not directed:
                self.add_adjacent_pair(val2, val1, weight=weight)

    def depth_first_traverse(self, path:list, edges:list,\
            end_vertex:Vertex)->Iterable:
        '''
        suppose both vertex exist
        path = [start_vertex]
        '''
        last_vertex = path[-1]
        if last_vertex == end_vertex:
            yield path, edges
        for vertex, edge in last_vertex.adjacent.items():
            if vertex not in path:
                yield from self.depth_first_traverse(
                    path + [vertex,], edges + [edge,], end_vertex)
    
    def breadth_first_traverse(self, start_vertex:Vertex, \
            end_vertex:Vertex)->list:
        '''
        '''
        paths, pool = [], [([start_vertex,], []),]
        while pool:
            path, edges = pool.pop(0)
            last_vertex = path[-1]
            if last_vertex == end_vertex:
                if path not in paths:
                    paths.append((path, edges))
            else:
                for vertex, edge in last_vertex.adjacent.items():
                    if vertex not in path:
                        pool.append(
                            (path + [vertex,], edges + [edge,])
                        )
        return paths

    def calculate_distance(self, edges, evaluate:str=None):
        evaluate = '_dist' if evaluate is None else evaluate
        return sum(
            [getattr(e, evaluate) for e in edges]
        )



    def shortest_distance_dfs(self, start:str, \
            end:str, evaluate:str=None)->list:
        '''
        depth first sarch
        '''
        shortest_path, shortest_dist = [], None
        start_vertex = self.get_node(start)
        end_vertex = self.get_node(end)
        if start_vertex and end_vertex:
            path = [start_vertex,]
            edges = []
            iters = self.depth_first_traverse(
                path, edges, end_vertex
            )
            for path, edges in iters:
                dist = self.calculate_distance(edges, evaluate)
                if shortest_dist is None or dist < shortest_dist:
                    shortest_dist = dist
                    shortest_path = path
            shortest_path = [v.val for v in shortest_path]
            return shortest_path, shortest_dist

    def shortest_distance_bfs(self, start:str, \
            end:str, evaluate:str=None)->list:
        '''
        breadth first sarch
        '''
        shortest_path, shortest_dist = [], None
        start_vertex = self.get_node(start)
        end_vertex = self.get_node(end)
        if start_vertex and end_vertex:
            iters = self.breadth_first_traverse(
                start_vertex, end_vertex
            )
            for path, edges in iters:
                dist = self.calculate_distance(edges, evaluate)
                if shortest_dist is None or dist < shortest_dist:
                    shortest_dist = dist
                    shortest_path = path
            shortest_path = [v.val for v in shortest_path]
            return shortest_path, shortest_dist




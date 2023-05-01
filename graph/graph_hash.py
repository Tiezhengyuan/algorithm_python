'''
graph: data is in hash table
'''
from typing import Iterable

class GraphHash:
    def __init__(self, data:dict):
        '''
        key: vertex, value: vertices
        '''
        self.data = data
    
    def depth_first_search(self, path:list, end_vertex:str)->Iterable:
        '''
        path = [start_vertext,]
        return all possible paths
        '''
        last_vertext = path[-1]
        if last_vertext == end_vertex:
            yield path

        for v in self.data.get(last_vertext, []):
            # doesn't allow circle path
            if v not in path:
                yield from self.depth_first_search(
                    path + [v,], end_vertex)
        return None

    def breadth_first_search(self, start_vertex:str, end_vertex:str)->list:
        '''
        return all possible paths
        '''
        pool, paths = [[start_vertex],], []
        while pool:
            path = pool.pop(0)
            # print(path)
            last_vertex = path[-1]
            if last_vertex == end_vertex:
                if path not in paths:
                    paths.append(path)
            else:
                for v in self.data.get(last_vertex, []):
                    if v not in path:
                        pool.append(path + [v,])
        return paths

    def get_nodes(self)->list:
        return list(self.data)
    
    def add_vertext(self,vertex:str)->bool:
        if not vertex or vertex in self.data:
            return False
        self.data[vertex] = []
        return True
    
    def add_adjacent(self, vertex1:str, vertex2:str)->bool:
        '''
        add connection given two vertices
        both of vertices could be new
        '''
        if vertex1 in self.data:
            if vertex2 not in self.data:
                self.data[vertex1].append(vertex2)
                self.data[vertex2] = [vertex1,]
            else:
                return False
        else:
            self.data[vertex1] = [vertex2,]
            if vertex2 in self.data:
                self.data[vertex2].append(vertex1)
            else:
                self.data[vertex2] = [vertex1,]
        return True
        

    
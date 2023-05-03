
from typing import Iterable

class City:
    def __init__(self, city:str):
        self.city = city
        self.routes = {}

    def add_route(self, adjacent_city, price:int):
        self.routes[adjacent_city] = price
    
    def get_price(self, adjacent_city)->int:
        return self.routes[adjacent_city]

    def get_adjacents(self)->Iterable:
        '''
        iterator of adjacent cities and route prices
        '''
        for adjacent_city, price in self.routes.items():
            yield (adjacent_city, price)



class DijkstraSearch:
    def __init__(self):
        self.data = {}

    def feed(self, data:Iterable):
        '''
        feed data into self.data
        key: city name in string
        value: instance of City
        '''
        # Names of depareture and arrival city
        for departure, arrival, price in data:
            if departure not in self.data:
                self.data[departure] = City(departure) 
            if arrival not in self.data:
                self.data[arrival] = City(arrival)
            self.data[departure].add_route(
                self.data[arrival], price)
        return self.data
    
    def search_cheapest(self, departure_name:str, arrival_name:str):
        # get instances of departure and arrival
        departure = self.data.get(departure_name)
        if not departure:
            return None
        arrival = self.data.get(arrival_name)
        if not arrival:
            return None

        # all cheapest prices to get to each city from the starting city
        # key is instance of City, value is price
        self.cheapest = {}
        # key is instance of adjacent city, 
        # value is previous stopover city.
        self.cheapest_previous = {}

        self.visited, self.unvisited = [], [departure, ]
        while self.unvisited:
            curr_city = self.unvisited.pop(0)
            # print(curr_city.city)
            self.visited.append(curr_city)
            self.update_cheapest(curr_city)
        
        cheapest_path = self.cheapest_path(departure, arrival)
        cheapest_price = self.cheapest[arrival]
        return cheapest_path, cheapest_price
        

    def update_cheapest(self, curr_city:City):
        '''
        given a city, detect cheaptest around
        adjacent cities starting from departure
        update self.cheapest
        update self.cheapest_previous
        '''
        curr_price = self.trace_cheapest_price(curr_city)
        for adj_city, price in curr_city.get_adjacents():
            new_price = curr_price + price
            if adj_city not in self.cheapest or \
                    new_price < self.cheapest[adj_city]:
                self.cheapest[adj_city] = new_price
                self.cheapest_previous[adj_city] = curr_city
            if adj_city not in self.visited:
                self.unvisited.append(adj_city) 
        # print('\n', curr_city.city)
        # for a, b in self.cheapest.items():
        #     print(a.city, b)
        

    def trace_cheapest_price(self, curr_city:City):
        '''
        there is departure. given a city,
        calculate the cheapest price
        between the city and departure
        suppose self.cheapest_previous is not None
        '''
        if curr_city in self.cheapest:
            return self.cheapest.get(curr_city)
        return 0
        

    def cheapest_path(self, departure:City, curr_city:City)->list:
        '''
        there is departure. given a city, get the 
        cheapest path between the city and departure
        suppose self.cheapest_previous is not None
        '''
        if departure == curr_city or curr_city \
                not in self.cheapest_previous:
            return [departure.city, ]
        previous_city = self.cheapest_previous[curr_city]
        # print(curr_city, previous_city)
        return self.cheapest_path(departure, previous_city) + \
                    [curr_city.city,]

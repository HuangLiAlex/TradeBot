import json
from BinanceAPI.util import container as ct

# read json file to a list (graph) of dictionary objects (stick)
class Json_Reader:
    
    def read(json_file):
        graph = []
        
        with open(json_file) as jf:
            json_data = json.load(jf)

        for cell in json_data:
            Time = cell[0]
            Open = cell[1]
            High = cell[2]
            Low  = cell[3]
            Close = cell[4]
            
            stick = ct.Stick.fromJson(Time, Open, High, Low, Close)
            graph.append(stick)
        return graph

    def read_stock(json_file):
        json_list = []
        graph = []

        for line in open(json_file, 'r'):
            json_list.append(json.loads(line))
        
        for json_data in json_list:
            Time = json_data["date"]
            Open = json_data["open"]
            Close = json_data["close"]
            High = json_data["high"]
            Low  = json_data["low"]
        
            stick = ct.Stick.fromJson(Time, Open, High, Low, Close)
            graph.append(stick)
        return graph
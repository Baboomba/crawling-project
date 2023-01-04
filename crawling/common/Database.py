import pandas as pd


class DataProcess:
    def __init__(self, kind:str):
        if kind == 'sales':
            self.columns = ['No.', 'store', 'sales', 'Qt.']
        elif kind == 'tips':
            self.columns = ['No.', 'store', 'tips', 'Pin']
        elif kind == 'review':
            self.columns = [
            'store', 'nick', 'rate', 'view', 'img url', 'img_no'
        ]


    def make_frame(self, kind):
        self.__init__(kind)
        df = pd.DataFrame(
            index = range(1),
            columns = self.columns)
        return df
        

    def raw_to_add(self, scraped:list):
        empty = []
        empty.append(scraped)
        raw = pd.DataFrame(empty, columns= self.columns)
        return raw


    def result_process(self, result, scraped:list):
        raw = self.raw_to_add(scraped)
        result = pd.concat([result, raw])
        return result
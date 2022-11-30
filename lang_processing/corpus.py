import pandas as pd

from . import line

class corpus:
    def __init__(self, meta_data_file_name, func_table_file_name):
        # Read in Function Table
        self.func_names = pd.read_csv(func_table_file_name)
        # Make Seperate C Lines
        self.ls = []
        df = pd.read_csv(meta_data_file_name)
        index = df.loc[df['at_beg_line'] == 'at_bol'].index
        # Separate C Lines
        for i in range(1, len(index)):
            self.add_line(line.lines(
                df.loc[(df.index < index[i]) & (df.index >= index[i - 1])],
                self.func_names))
        # self.ls[0].debug()
        # self.ls[1].debug()
        # self.ls[2].debug()
        # self.ls[3].debug()
        # self.ls[4].debug()
        # self.ls[5].debug()
        # self.ls[6].debug()
        # self.ls[0].classify_operator()
        # self.ls[0].match_type()

    def add_line(self, l):
        self.ls.append(l)

    def debug(self):
        for i in range(len(self.ls)):
            self.ls[i].debug()

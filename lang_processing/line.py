import pandas as pd
import numpy as np

from . import constants

class lines:
    def __init__(self, literal, func_table):
        self.literal = literal
        self.literal = self.literal.reset_index()
        self.classify_line(func_table)

    def classify_line(self, func_table):
        self.literal['id_tag'] = self.tag_data(func_table)
        print(self.literal)

    def tag_data(self, func_table):
        new_column = pd.Series(np.empty(len(self.literal.index)))
        new_column[:] = self.literal['id_literal'].values
        # Get function tag
        new_column = new_column.apply(lambda x: constants.get_function() if
                         x in func_table['Function Names'].values else x)
        # Get Control flow tag
        new_column = new_column.apply(lambda x: constants.get_control_flow() if
                         x in constants.get_control_flow_table() else x)
        # Get Type Flag
        new_column = new_column.apply(lambda x: constants.get_type_decl() if
                         x in constants.get_type_table() else x)
        # Get Bool Op Flag
        new_column = new_column.apply(lambda x: constants.get_bool_op() if
                         x in constants.get_bool_op_table() else x)
        # Get Int Op Flag
        new_column = new_column.apply(lambda x: constants.get_int_op() if
                         x in constants.get_int_op_table() else x)
        # Get State Transition Flag
        new_column = new_column.apply(lambda x:
                                      constants.get_state_transition() if
                                      x in constants.get_state_transition_op()
                                      else x)
        # Get Line End Flag
        new_column = new_column.apply(lambda x: constants.line_end() if
                                      x in constants.get_line_end_op() else x)
        # Get Following Arguement Flag
        new_column = new_column.apply(lambda x: constants.following_argument()
                                      if x in constants.get_following_argument()
                                      else x)
        # Get Member Of Flag
        new_column = new_column.apply(lambda x: constants.member_of() if
                                      x in constants.get_member_of() else x)
        # Get Member Of Flag
        new_column = new_column.apply(lambda x: constants.member_of() if
                                      x in constants.get_member_of() else x)
        # Get Open Parenthesis Of Flag
        new_column = new_column.apply(lambda x: constants.open_paren() if
                                      x in constants.get_open_paren() else x)
        # Get Close Parenthesis Of Flag
        new_column = new_column.apply(lambda x: constants.close_paren() if
                                      x in constants.get_close_paren() else x)
        # Get Close Parenthesis Of Flag
        new_column = new_column.apply(lambda x: constants.close_paren() if
                                      x in constants.get_close_paren() else x)
        # Get Integer Flag
        new_column = new_column.apply(lambda x: constants.integer_flag() if
                                      str.isdigit(x) else x)
        # Get Primary Data Strand Flag
        new_column = new_column.apply(lambda x: constants.primary_data_strand()
                                      if x in constants
                                      .get_primary_data_strand() else x)
        # Get Primary Data Strand Flag
        new_column = new_column.apply(lambda x: constants.variable()
                                      if not(x in constants
                                      .get_all_symbols()) else x)
        return new_column

    # def parse_function(self)
    # def parse_control_flow(self)
    # def parse_state_transition(self)
    #
    # def match_type(self):
    # def match_var(self)
    # def match_transition(self)
    # def match_params(self)

    def debug(self):
        print(self.literal)

# Operator Classifiers
def get_state_transition():
    return 'State Transitionon'
def get_control_flow():
    return 'Control Flow'
def get_function():
    return 'Function'
def get_type_decl():
    return 'Type Declaration'
def get_bool_op():
    return 'Boolean Operator'
def get_int_op():
    return 'Integer Operator'
def following_argument():
    return 'Following Argument'
def line_end():
    return 'Line End'
def member_of():
    return 'Member Of'
def open_paren():
    return 'Open Parenthesis'
def close_paren():
    return 'Close Parenthesis'
# Note no corresponding get bc built into python
def integer_flag():
    return 'Integer'
def primary_data_strand():
    return 'Primary Data Strand'
def variable():
    return 'Variable'

def get_primary_data_strand():
    return ('bt',
            'bt_left_child',
            'bt_right_child')

def get_all_symbols():
    return (get_state_transition(),
     get_control_flow(),
     get_function(),
     get_type_decl(),
     get_bool_op(),
     get_int_op(),
     following_argument(),
     line_end(),
     member_of(),
     open_paren(),
     close_paren(),
     integer_flag(),
     primary_data_strand(),
     variable())

def get_open_paren():
    return ('(')
def get_close_paren():
    return (')')

def get_member_of():
    return '->'
def ordinalize():
    return {(0, get_control_flow()),
            (1, get_type_decl()),
            (2, get_bool_op()),
            (3, get_function()),
            (4, get_state_transition())
            }
def get_bool_op_table():
    return ('!',
            '&&',
            '||',
            '>',
            '>=',
            '<=',
            '<'
            )
def get_line_end_op():
    return ('semicolon',
            '{')
def get_following_argument():
    return ('comma')
def get_int_op_table():
    return ('+')
def get_state_transition_op():
    return ('=')
def get_control_flow_table():
    return ('if',
            'else',
            'return')
def get_type_table():
    return ('int',
            'void',
            'bin_tree',
            'struct',
            'typedef',
            'BIN_TREE_T',
            '*')

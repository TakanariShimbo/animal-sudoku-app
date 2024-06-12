import random

import numpy as np

from optimization import Optimizer, Consts, Table


def check_table_can_solve(table: Table) -> bool:
    consts = Consts(fixed_table=table)
    optimizer = Optimizer(table=consts)
    result_table = optimizer.run()
    if result_table:
        return True
    else:
        return False


def solve_table(table: Table) -> Table:
    consts = Consts(fixed_table=table)
    optimizer = Optimizer(table=consts)
    result_table = optimizer.run()
    assert type(result_table) == Table
    return result_table


def prepare_init_table(n_empty_cells: int) -> Table:
    seed = random.randint(1, 10000)
    empty_number_array = np.zeros((9, 9), dtype=int)
    empty_table = Table(number_array=empty_number_array)
    consts = Consts(fixed_table=empty_table)
    optimizer = Optimizer(table=consts, seed=seed)
    result_table = optimizer.run()
    assert type(result_table) == Table
    result_table.convert_some_cells_to_zero(n_cells_to_zero=n_empty_cells, seed=seed)
    return result_table

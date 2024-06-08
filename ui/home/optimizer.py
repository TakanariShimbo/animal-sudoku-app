from optimization import Optimizer, Consts, Table


def check_table_can_solve(table: Table) -> bool:
    consts = Consts(fixed_table=table)
    optimizer = Optimizer(consts=consts)
    result_table = optimizer.run()
    if result_table:
        return True
    else:
        return False


def solve_table(table: Table) -> Table:
    consts = Consts(fixed_table=table)
    optimizer = Optimizer(consts=consts)
    result_table = optimizer.run()
    assert type(result_table) == Table
    return result_table

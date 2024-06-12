from ortools.sat.python import cp_model

from .table import Table
from .variables import Variables
from .constraints import add_constraints
from .solution_callback import SolutionCallback


class Optimizer:
    def __init__(self, table: Table, seed: int = 123) -> None:
        model = cp_model.CpModel()

        solver = cp_model.CpSolver()
        solver.parameters.random_seed = seed
        solver.parameters.enumerate_all_solutions = False
        solver.parameters.linearization_level = 0

        self._model = model
        self._solver = solver
        self._table = table

    def run(self) -> Table | None:
        variables = Variables(model=self._model)

        add_constraints(model=self._model, table=self._table, variables=variables)

        solution_callback = SolutionCallback(variables=variables)
        status = self._solver.solve(model=self._model, solution_callback=solution_callback)
        has_solution = status == cp_model.OPTIMAL or status == cp_model.FEASIBLE
        # self._print_statistics()

        if not has_solution:
            return None
        return solution_callback.result_table

    # def _print_statistics(self) -> None:
    #     print("\nStatistics")
    #     print(f"  - conflicts      : {self._solver.num_conflicts}")
    #     print(f"  - branches       : {self._solver.num_branches}")
    #     print(f"  - wall time      : {self._solver.wall_time} s")

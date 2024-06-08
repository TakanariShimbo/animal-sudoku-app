from ortools.sat.python import cp_model

from .table import Table
from .consts import Consts
from .variables import Variables
from .constraints import add_constraints
from .solution_callback import SolutionCallback


class Optimizer:
    def __init__(self, consts: Consts) -> None:
        # モデルの作成
        model = cp_model.CpModel()

        # ソルバーの作成
        solver = cp_model.CpSolver()
        solver.parameters.linearization_level = 0
        solver.parameters.enumerate_all_solutions = True

        self._model = model
        self._solver = solver
        self._consts = consts

    def run(self) -> Table | None:
        # モデルに変数を追加
        variables = Variables(model=self._model, consts=self._consts)

        # モデルに拘束を追加
        add_constraints(model=self._model, consts=self._consts, variables=variables)

        # モデルをソルバーで解く
        solution_limit = 1
        solution_callback = SolutionCallback(consts=self._consts, variables=variables, solution_limit=solution_limit)
        status = self._solver.solve(model=self._model, solution_callback=solution_callback)
        # self._print_statistics()

        if not (status == cp_model.OPTIMAL or status == cp_model.FEASIBLE):
            return None
        return solution_callback.result_table

    def _print_statistics(self) -> None:
        print("\nStatistics")
        print(f"  - conflicts      : {self._solver.num_conflicts}")
        print(f"  - branches       : {self._solver.num_branches}")
        print(f"  - wall time      : {self._solver.wall_time} s")

import numpy as np
from ortools.sat.python import cp_model

from .table import Table
from .consts import Consts
from .variables import Variables


class SolutionCallback(cp_model.CpSolverSolutionCallback):
    def __init__(self, consts: Consts, variables: Variables, solution_limit: int):
        super().__init__()

        self._consts = consts
        self._variables = variables
        self._solution_count = 0
        self._solution_limit = solution_limit
        self._result_table: Table | None = None

    def get_assigned_number(self, h_position: int, v_position: int) -> int:
        for number in self._consts.numbers:
            is_assigned_var = self._variables.get_is_assigned_var(h_position=h_position, v_position=v_position, number=number)
            is_assigned = self.value(is_assigned_var)
            if is_assigned:
                return number
        raise Exception(f"Zero Assigned Number at {h_position} {v_position}")

    def save_result(self) -> None:
        result_number_array = np.zeros([9, 9], dtype=int)
        for h_idx, h_position in enumerate(self._consts.h_positions):
            for v_idx, v_position in enumerate(self._consts.v_positions):
                number = self.get_assigned_number(h_position=h_position, v_position=v_position)
                result_number_array[v_idx, h_idx] = number

        self._result_table = Table(number_array=result_number_array)

    def on_solution_callback(self) -> None:
        self._solution_count += 1
        self.save_result()

        if self._solution_count >= self._solution_limit:
            print(f"Stop search after {self._solution_limit} solutions")
            self.stop_search()

    def solution_count(self) -> int:
        return self._solution_count

    @property
    def result_table(self) -> Table | None:
        return self._result_table

import pandas as pd
from ortools.sat.python import cp_model

from .consts import Consts
from .variables import Variables


pd.set_option("display.width", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.unicode.east_asian_width", True)


class SolutionCallback(cp_model.CpSolverSolutionCallback):
    def __init__(self, consts: Consts, variables: Variables, solution_limit: int):
        super().__init__()

        self._consts = consts
        self._variables = variables
        self._solution_count = 0
        self._solution_limit = solution_limit
        self._result_numbers_df: pd.DataFrame | None = None

    def get_assigned_number(self, h_position: int, v_position: int) -> int:
        for number in self._consts.numbers:
            is_assigned_var = self._variables.get_is_assigned_var(h_position=h_position, v_position=v_position, number=number)
            is_assigned = self.value(is_assigned_var)
            if is_assigned:
                return number
        raise Exception(f"Zero Assigned Number at {h_position} {v_position}")

    def save_result(self) -> None:
        result_numbers_df = pd.DataFrame(None, index=self._consts.v_positions, columns=self._consts.h_positions)
        for h_position in self._consts.h_positions:
            for v_position in self._consts.v_positions:
                number = self.get_assigned_number(h_position=h_position, v_position=v_position)
                result_numbers_df.loc[v_position, h_position] = number

        self._result_numbers_df = result_numbers_df

    def on_solution_callback(self) -> None:
        self._solution_count += 1
        self.save_result()

        if self._solution_count >= self._solution_limit:
            print(f"Stop search after {self._solution_limit} solutions")
            self.stop_search()

    def solution_count(self) -> int:
        return self._solution_count

    @property
    def result_numbers_df(self) -> pd.DataFrame | None:
        return self._result_numbers_df

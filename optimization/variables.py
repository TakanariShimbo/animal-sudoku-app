from ortools.sat.python import cp_model

from .consts import Consts


class Variables:
    def __init__(self, model: cp_model.CpModel, consts: Consts):
        self._consts = consts
        self._is_assigned_var_dict = self.prepare_is_assigned_var(model=model)

    def prepare_is_assigned_var(self, model: cp_model.CpModel) -> dict[tuple[int, int, int], cp_model.BoolVarT]:
        is_assigned_var_dict: dict[tuple[int, int, int], cp_model.BoolVarT] = {}

        for h_position in self._consts.h_positions:
            for v_position in self._consts.v_positions:
                for number in self._consts.numbers:
                    key = (h_position, v_position, number)
                    val = model.new_bool_var("IsAssignedVar_Hpos%i_Vpos%i_Num%i" % (h_position, v_position, number))
                    is_assigned_var_dict[key] = val

        return is_assigned_var_dict

    def get_is_assigned_var(self, h_position: int, v_position: int, number: int) -> cp_model.BoolVarT:
        return self._is_assigned_var_dict[(h_position, v_position, number)]

    def get_is_assigned_var_(self, h_grid_position: int, v_grid_position: int, h_position_in_grid: int, v_position_in_grid: int, number: int) -> cp_model.BoolVarT:
        h_position = (h_grid_position - 1) * 3 + h_position_in_grid
        v_position = (v_grid_position - 1) * 3 + v_position_in_grid
        return self.get_is_assigned_var(h_position=h_position, v_position=v_position, number=number)

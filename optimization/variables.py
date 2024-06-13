from ortools.sat.python import cp_model

from .table import TABLE_CONFIG


class Variables:
    def __init__(self, model: cp_model.CpModel):
        self._is_assigned_var_dict = self.prepare_is_assigned_var(model=model)

    def prepare_is_assigned_var(self, model: cp_model.CpModel) -> dict[tuple[int, int, int], cp_model.BoolVarT]:
        is_assigned_var_dict: dict[tuple[int, int, int], cp_model.BoolVarT] = {}

        for h_position in TABLE_CONFIG.h_positions:
            for v_position in TABLE_CONFIG.v_positions:
                for number in TABLE_CONFIG.numbers:
                    key = (h_position, v_position, number)
                    val = model.new_bool_var(f"IsAssignedVar_Hpos{h_position}_Vpos{v_position}_Num{number}")
                    is_assigned_var_dict[key] = val

        return is_assigned_var_dict

    def get_is_assigned_var(self, h_position: int, v_position: int, number: int) -> cp_model.BoolVarT:
        return self._is_assigned_var_dict[(h_position, v_position, number)]

    def get_is_assigned_var_(self, h_grid_position: int, v_grid_position: int, h_position_in_grid: int, v_position_in_grid: int, number: int) -> cp_model.BoolVarT:
        v_grid_size, h_grid_size = TABLE_CONFIG.grid_size
        h_position = (h_grid_position - 1) * h_grid_size + h_position_in_grid
        v_position = (v_grid_position - 1) * v_grid_size + v_position_in_grid
        return self.get_is_assigned_var(h_position=h_position, v_position=v_position, number=number)

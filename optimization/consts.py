from .table import Table


class Consts:
    def __init__(self, fixed_table: Table) -> None:
        self._fixed_table = fixed_table

    @property
    def h_positions(self) -> list[int]:
        return list(range(1, 10))

    @property
    def v_positions(self) -> list[int]:
        return list(range(1, 10))

    @property
    def numbers(self) -> list[int]:
        return list(range(1, 10))

    @property
    def h_grid_positions(self) -> list[int]:
        return list(range(1, 4))

    @property
    def v_grid_positions(self) -> list[int]:
        return list(range(1, 4))

    @property
    def h_positions_in_grid(self) -> list[int]:
        return list(range(1, 4))

    @property
    def v_positions_in_grid(self) -> list[int]:
        return list(range(1, 4))

    def get_fixed_number(self, h_position: int, v_position: int) -> int | None:
        val = self._fixed_table.get_number_df().loc[v_position, h_position]
        if val == 0:
            return None
        else:
            return int(val)

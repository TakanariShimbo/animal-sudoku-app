import pandas as pd


class Consts:
    def __init__(self, fixed_numbers_df: pd.DataFrame) -> None:
        assert fixed_numbers_df.shape == (9, 9)
        fixed_numbers_df = pd.DataFrame(data=fixed_numbers_df.values, index=self.v_positions, columns=self.h_positions, dtype=int)
        self._fixed_numbers_df = fixed_numbers_df

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

    @property
    def fixed_numbers_df(self) -> pd.DataFrame:
        return self._fixed_numbers_df

    def get_fixed_number(self, h_position: int, v_position: int) -> int | None:
        val = self._fixed_numbers_df.loc[v_position, h_position]
        if val == 0:
            return None
        else:
            return int(val)

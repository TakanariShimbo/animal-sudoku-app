import numpy as np
import pandas as pd


class TableConfig:
    # ----------------------------------------
    # number config
    # ----------------------------------------
    @property
    def numbers(self) -> list[int]:
        return list(range(1, 10))

    @property
    def strings(self) -> list[str]:
        return ["", "🐭1", "🐮2", "🐯3", "🐰4", "🐉5", "🐍6", "🐎7", "🐏8", "🐵9"]

    @property
    def number_to_string_dict(self) -> dict[int, str]:
        return {key: val for key, val in enumerate(self.strings)}

    @property
    def string_to_number_dict(self) -> dict[str, int]:
        return {val: key for key, val in enumerate(self.strings)} | {f"{key}": key for key, val in enumerate(self.strings)}

    def convert_array_to_string(self, number_array: np.ndarray) -> np.ndarray:
        to_sring_converter = np.vectorize(self.number_to_string_dict.get)
        return to_sring_converter(number_array)

    def convert_array_to_number(self, string_array: np.ndarray) -> np.ndarray:
        to_number_converter = np.vectorize(self.string_to_number_dict.get)
        return to_number_converter(string_array)

    # ----------------------------------------
    # index and column config
    # ----------------------------------------
    @property
    def v_positions(self) -> list[int]:
        return list(range(1, 10))

    @property
    def h_positions(self) -> list[int]:
        return list(range(1, 10))

    @property
    def table_size(self) -> tuple[int, int]:
        return len(self.v_positions), len(self.h_positions)

    @property
    def indexes_and_columns_for_number(self) -> tuple[list[int], list[int]]:
        return self.v_positions, self.h_positions

    def get_indexes_and_columns_for_string(self, column_header: str, index_header: str) -> tuple[list[str], list[str]]:
        number_indexes, number_columns = self.indexes_and_columns_for_number
        string_indexes = [f"{index_header}{n}" for n in number_indexes]
        string_columns = [f"{column_header}{n}" for n in number_columns]
        return string_indexes, string_columns

    # ----------------------------------------
    # grid config
    # ----------------------------------------
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
    def grid_size(self) -> tuple[int, int]:
        return len(self.v_positions_in_grid), len(self.h_positions_in_grid)


TABLE_CONFIG = TableConfig()


class Table:
    def __init__(self, number_array: np.ndarray) -> None:
        assert number_array.shape == TABLE_CONFIG.table_size
        assert np.issubdtype(number_array.dtype, np.integer)
        assert number_array.min() >= 0
        assert number_array.max() <= max(TABLE_CONFIG.numbers)

        self._number_array = number_array

    @classmethod
    def from_number_df(cls, number_df: pd.DataFrame) -> "Table":
        return cls(number_array=number_df.values)

    @classmethod
    def from_string_df(cls, string_df: pd.DataFrame) -> "Table":
        string_array = string_df.values
        number_array = TABLE_CONFIG.convert_array_to_number(string_array=string_array)
        return cls(number_array=number_array)

    def get_string_df(self, column_header: str, index_header: str) -> pd.DataFrame:
        indexes, columns = TABLE_CONFIG.get_indexes_and_columns_for_string(column_header=column_header, index_header=index_header)
        return pd.DataFrame(
            data=TABLE_CONFIG.convert_array_to_string(number_array=self._number_array),
            index=indexes,
            columns=columns,
            dtype=str,
        )

    def get_number_df(self) -> pd.DataFrame:
        indexes, columns = TABLE_CONFIG.indexes_and_columns_for_number
        return pd.DataFrame(
            data=self._number_array,
            index=indexes,
            columns=columns,
            dtype=int,
        )

    @property
    def is_filled(self) -> bool:
        return self._number_array.min() > 0

    def convert_some_cells_to_zero(self, n_cells_to_zero: int, seed: int) -> None:
        np.random.seed(seed)
        idxes = np.arange(self._number_array.size)
        np.random.shuffle(idxes)
        target_idxes = idxes[:n_cells_to_zero]
        np.put(self._number_array, target_idxes, 0)

    def get_fixed_number(self, h_position: int, v_position: int) -> int | None:
        val = self.get_number_df().loc[v_position, h_position]
        if val == 0:
            return None
        else:
            return int(val)

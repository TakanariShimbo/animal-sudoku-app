import numpy as np
import pandas as pd


class Table:
    DISPLAYED_STRING_LIST = ["", "🐭1", "🐮2", "🐯3", "🐰4", "🐉5", "🐍6", "🐎7", "🐏8", "🐵9"]

    def __init__(self, number_array: np.ndarray) -> None:
        assert number_array.shape == (9, 9)
        assert np.issubdtype(number_array.dtype, np.integer)
        assert number_array.min() >= 0
        assert number_array.max() <= 9

        self._number_array = number_array

    @classmethod
    def from_number_df(cls, number_df: pd.DataFrame) -> "Table":
        return cls(number_array=number_df.values)

    @classmethod
    def from_string_df(cls, string_df: pd.DataFrame) -> "Table":
        string_array = string_df.values
        number_array = cls._convert_array_to_number(string_array=string_array)
        return cls(number_array=number_array)

    @staticmethod
    def _get_indexes_and_columns_for_number() -> tuple[list[int], list[int]]:
        indexes = list(range(1, 10))
        columns = list(range(1, 10))
        return indexes, columns

    @classmethod
    def _get_indexes_and_columns_for_string(cls, column_header: str = "列", index_header: str = "行") -> tuple[list[str], list[str]]:
        number_indexes, number_columns = cls._get_indexes_and_columns_for_number()
        string_indexes = [f"{index_header}{n}" for n in number_indexes]
        string_columns = [f"{column_header}{n}" for n in number_columns]
        return string_indexes, string_columns

    @classmethod
    def _convert_array_to_string(cls, number_array: np.ndarray) -> np.ndarray:
        number_to_string_dict = {key: val for key, val in enumerate(cls.DISPLAYED_STRING_LIST)}
        to_sring_converter = np.vectorize(number_to_string_dict.get)
        return to_sring_converter(number_array)

    @classmethod
    def _convert_array_to_number(cls, string_array: np.ndarray) -> np.ndarray:
        string_to_number_dict = {val: key for key, val in enumerate(cls.DISPLAYED_STRING_LIST)} | {f"{key}": key for key, val in enumerate(cls.DISPLAYED_STRING_LIST)}
        to_number_converter = np.vectorize(string_to_number_dict.get)
        return to_number_converter(string_array)

    @property
    def string_df(self) -> pd.DataFrame:
        indexes, columns = self._get_indexes_and_columns_for_string()

        return pd.DataFrame(
            data=self._convert_array_to_string(number_array=self._number_array),
            index=indexes,
            columns=columns,
            dtype=str,
        )

    @property
    def number_df(self) -> pd.DataFrame:
        indexes, columns = self._get_indexes_and_columns_for_number()

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

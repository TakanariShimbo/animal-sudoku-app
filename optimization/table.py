import numpy as np
import pandas as pd


class Table:
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
    def _get_string_list() -> list[str]:
        return ["", "🐭1", "🐮2", "🐯3", "🐰4", "🐉5", "🐍6", "🐎7", "🐏8", "🐵9"]

    @classmethod
    def _get_number_to_string_dict(cls) -> dict[int, str]:
        return {key: val for key, val in enumerate(cls._get_string_list())}

    @classmethod
    def _get_string_to_number_dict(cls) -> dict[str, int]:
        return {val: key for key, val in enumerate(cls._get_string_list())} | {f"{key}": key for key, val in enumerate(cls._get_string_list())}

    @staticmethod
    def _get_indexes_and_columns_for_number() -> tuple[list[int], list[int]]:
        indexes = list(range(1, 10))
        columns = list(range(1, 10))
        return indexes, columns

    @classmethod
    def _get_indexes_and_columns_for_string(cls, column_header: str, index_header: str) -> tuple[list[str], list[str]]:
        number_indexes, number_columns = cls._get_indexes_and_columns_for_number()
        string_indexes = [f"{index_header}{n}" for n in number_indexes]
        string_columns = [f"{column_header}{n}" for n in number_columns]
        return string_indexes, string_columns

    @classmethod
    def _convert_array_to_string(cls, number_array: np.ndarray) -> np.ndarray:
        to_sring_converter = np.vectorize(cls._get_number_to_string_dict().get)
        return to_sring_converter(number_array)

    @classmethod
    def _convert_array_to_number(cls, string_array: np.ndarray) -> np.ndarray:
        to_number_converter = np.vectorize(cls._get_string_to_number_dict().get)
        return to_number_converter(string_array)

    def get_string_df(self, column_header: str, index_header: str) -> pd.DataFrame:
        indexes, columns = self._get_indexes_and_columns_for_string(column_header=column_header, index_header=index_header)

        return pd.DataFrame(
            data=self._convert_array_to_string(number_array=self._number_array),
            index=indexes,
            columns=columns,
            dtype=str,
        )

    def get_number_df(self) -> pd.DataFrame:
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

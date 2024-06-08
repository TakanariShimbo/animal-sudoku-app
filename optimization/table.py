import numpy as np
import pandas as pd


DISPLAYED_STRING_LIST = ["", "🐭1", "🐮2", "🐯3", "🐰4", "🐉5", "🐍6", "🐎7", "🐏8", "🐵9"]

NUMBER_TO_STRING_DICT = {key: val for key, val in enumerate(DISPLAYED_STRING_LIST)}
STRING_TO_NUMBER_DICT = {val: key for key, val in enumerate(DISPLAYED_STRING_LIST)} | {f"{key}": key for key, val in enumerate(DISPLAYED_STRING_LIST)}

CONVERT_NUMBER_TO_STRING = np.vectorize(NUMBER_TO_STRING_DICT.get)
CONVERT_STRING_TO_NUMBER = np.vectorize(STRING_TO_NUMBER_DICT.get)

NUMBER_INDEXES = list(range(1, 10))
NUMBER_COLUMNS = list(range(1, 10))
STRING_INDEXES = [f"行{n}" for n in NUMBER_INDEXES]
STRING_COLUMNS = [f"列{n}" for n in NUMBER_COLUMNS]


class Table:
    def __init__(self, number_array: np.ndarray) -> None:
        assert number_array.shape == (9, 9)
        assert np.issubdtype(number_array.dtype, np.integer)
        assert number_array.min() >= 0
        assert number_array.max() <= 9

        self._string_df = pd.DataFrame(
            data=CONVERT_NUMBER_TO_STRING(number_array),
            index=STRING_INDEXES,
            columns=STRING_COLUMNS,
            dtype=str,
        )
        self._number_df = pd.DataFrame(
            data=number_array,
            index=NUMBER_INDEXES,
            columns=NUMBER_COLUMNS,
            dtype=int,
        )
        self._is_filled = number_array.min() > 0

    @classmethod
    def from_number_df(cls, number_df: pd.DataFrame) -> "Table":
        return cls(number_array=number_df.values)

    @classmethod
    def from_string_df(cls, string_df: pd.DataFrame) -> "Table":
        string_array = string_df.values
        number_array = CONVERT_STRING_TO_NUMBER(string_array)
        return cls(number_array=number_array)

    @property
    def string_df(self) -> pd.DataFrame:
        return self._string_df

    @property
    def number_df(self) -> pd.DataFrame:
        return self._number_df

    @property
    def is_filled(self) -> bool:
        return self._is_filled

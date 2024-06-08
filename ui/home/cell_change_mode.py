from enum import Enum, auto
import pandas as pd


class CellChangedMode(Enum):
    COLLECTLY = auto()
    NOT_NUMBER = auto()
    NOT_EMPTY = auto()
    NOT_CHANGED = auto()


def check_cell_changed_mode(from_string_df: pd.DataFrame, to_string_df: pd.DataFrame) -> CellChangedMode:
    is_cell_changed = check_is_cell_changed(from_string_df=from_string_df, to_string_df=to_string_df)
    if not is_cell_changed:
        return CellChangedMode.NOT_CHANGED

    is_empty_cell_changed = check_is_empty_cell_changed(from_string_df=from_string_df, to_string_df=to_string_df)
    if not is_empty_cell_changed:
        return CellChangedMode.NOT_EMPTY

    is_empty_cell_changed_correctly = check_is_empty_cell_changed_correctly(from_string_df=from_string_df, to_string_df=to_string_df)
    if not is_empty_cell_changed_correctly:
        return CellChangedMode.NOT_NUMBER

    return CellChangedMode.COLLECTLY


def check_is_cell_changed(from_string_df: pd.DataFrame, to_string_df: pd.DataFrame) -> bool:
    comparison = from_string_df != to_string_df
    return comparison.any().any()


def check_is_empty_cell_changed(from_string_df: pd.DataFrame, to_string_df: pd.DataFrame) -> bool:
    comparison = (from_string_df == "") & (to_string_df != "")
    return comparison.any().any()


def check_is_empty_cell_changed_correctly(from_string_df: pd.DataFrame, to_string_df: pd.DataFrame) -> bool:
    for number in list(range(1, 10)):
        comparison = (from_string_df == "") & (to_string_df == f"{number}")
        if comparison.any().any():
            return True
    return False

import numpy as np
import pandas as pd
import streamlit as st

from optimization import Optimizer, Consts, Table
from ui import RerenderSState, TableSState


def check_is_changed_correctly(from_string_df: pd.DataFrame, to_string_df: pd.DataFrame) -> bool:
    for number in list(range(1, 10)):
        comparison = (from_string_df == "") & (to_string_df == f"{number}")
        if comparison.any().any():
            return True
    return False


def check_is_changed_incorrectly(from_string_df: pd.DataFrame, to_string_df: pd.DataFrame) -> bool:
    comparison = from_string_df != to_string_df
    return comparison.any().any()


def check_is_filled_all(displayed_numbers_df: pd.DataFrame) -> bool:
    return not displayed_numbers_df.isin([""]).any().any()


st.set_page_config(
    page_title="アニマル数独アプリ",
    page_icon="🐧",
)

st.write("### 🐧アニマル数独アプリ")

init_number_array = np.array(
    [
        [0, 8, 0, 4, 0, 0, 0, 9, 0],
        [0, 6, 0, 0, 0, 0, 1, 3, 0],
        [0, 0, 1, 7, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 5, 0, 0],
        [7, 0, 5, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 3],
        [5, 2, 0, 3, 0, 0, 0, 7, 6],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
    ],
    dtype=int,
)
init_table = Table(number_array=init_number_array)
TableSState.init(table=init_table)

edited_string_df = st.data_editor(
    key=RerenderSState.get(),
    data=TableSState.get().string_df,
)


if check_is_changed_correctly(
    from_string_df=TableSState.get().string_df,
    to_string_df=edited_string_df,
):
    edited_table = Table.from_string_df(string_df=edited_string_df)
    TableSState.set(table=edited_table)
    RerenderSState.call()
    st.rerun()


if check_is_changed_incorrectly(
    from_string_df=TableSState.get().string_df,
    to_string_df=edited_string_df,
):
    RerenderSState.call()
    st.rerun()


is_filled = TableSState.get().is_filled


left, cencter, right = st.columns([1, 1, 1])
with left:
    is_restart_pushed = st.button(label="最初から🐔")
with cencter:
    is_solve_pushed = st.button(label="回答を見る🐶")
with right:
    is_check_pushed = st.button(label="順調か確認🐗")


if is_restart_pushed:
    TableSState.set(table=init_table)
    RerenderSState.call()
    st.rerun()


if is_check_pushed and not is_filled:
    current_table = TableSState.get()
    consts = Consts(fixed_table=current_table)
    optimizer = Optimizer(consts=consts)
    result_table = optimizer.run()
    if result_table:
        st.info("順調だよ、その調子🐧")
    else:
        st.error("どこか間違ってるみたい🐧")


if is_solve_pushed:
    current_table = TableSState.get()
    consts = Consts(fixed_table=current_table)
    optimizer = Optimizer(consts=consts)
    result_table = optimizer.run()
    if result_table:
        TableSState.set(table=result_table)
        RerenderSState.call()
        st.rerun()

    consts = Consts(fixed_table=init_table)
    optimizer = Optimizer(consts=consts)
    result_table = optimizer.run()
    if result_table:
        TableSState.set(table=result_table)
        RerenderSState.call()
        st.rerun()

    st.warning("ごめんね、サーバーで問題が発生しているみたい🐧")


if is_filled:
    consts = Consts(fixed_table=TableSState.get())
    optimizer = Optimizer(consts=consts)
    result_table = optimizer.run()
    if result_table:
        st.info("遊んでくれてありがとう　またね🐧")
        st.balloons()
    else:
        st.error("どこか間違っているみたい🐧")

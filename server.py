import time

import numpy as np
import pandas as pd
import streamlit as st

from optimization import Optimizer, Consts, Table
from ui import RerenderSState, TableSState, check_cell_changed_mode, CellChangedMode


def check_is_filled_all(displayed_numbers_df: pd.DataFrame) -> bool:
    return not displayed_numbers_df.isin([""]).any().any()


st.set_page_config(
    page_title="アニマル数独アプリ",
    page_icon="🐧",
)

style = "<style>h3 {text-align: center;}</style>"
st.markdown(style, unsafe_allow_html=True)
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
    use_container_width=True,
)

_, left, _, right, _ = st.columns([1, 3, 1, 3, 1])
with left:
    is_restart_pushed = st.button(label="最初から🐔", use_container_width=True)
with right:
    is_solve_pushed = st.button(label="回答を見る🐶", use_container_width=True)


cell_changed_mode = check_cell_changed_mode(
    from_string_df=TableSState.get().string_df,
    to_string_df=edited_string_df,
)

is_filled = TableSState.get().is_filled


if cell_changed_mode == CellChangedMode.NOT_EMPTY:
    st.toast("すでに埋まっているマスは変えられないよ🐧")
    time.sleep(1.0)
    RerenderSState.call()
    st.rerun()


if cell_changed_mode == CellChangedMode.NOT_NUMBER:
    st.toast("1から9の数字を入力してね🐧")
    time.sleep(1.0)
    RerenderSState.call()
    st.rerun()


if cell_changed_mode == CellChangedMode.COLLECTLY:
    edited_table = Table.from_string_df(string_df=edited_string_df)
    consts = Consts(fixed_table=edited_table)
    optimizer = Optimizer(consts=consts)
    result_table = optimizer.run()
    if result_table == None:
        st.toast("その数字は入れられないよ🐧")
        time.sleep(1.0)
    else:
        TableSState.set(table=edited_table)
    RerenderSState.call()
    st.rerun()


if is_restart_pushed:
    TableSState.set(table=init_table)
    RerenderSState.call()
    st.rerun()


if is_solve_pushed:
    current_table = TableSState.get()
    consts = Consts(fixed_table=current_table)
    optimizer = Optimizer(consts=consts)
    result_table = optimizer.run()
    assert type(result_table) == Table
    TableSState.set(table=result_table)
    RerenderSState.call()
    st.rerun()


if is_filled:
    st.info("遊んでくれてありがとう　またね🐧")
    st.balloons()

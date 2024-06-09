import time

import streamlit as st

from optimization import Table
from .sstates import RerenderSState, TableSState, InitTableSState, NEmptySState
from .cell_change_mode import CellChangedMode, check_cell_changed_mode
from .optimizer import check_table_can_solve, solve_table, prepare_init_table
from .images import RuleImages


def show_home() -> bool:
    #######################################################
    #                       INIT                          #
    #######################################################
    if not NEmptySState.is_initialized_already():
        NEmptySState.set(n_empty_cells=40)

    if not InitTableSState.is_initialized_already():
        init_table = prepare_init_table(n_empty_cells=NEmptySState.get())
        InitTableSState.set(table=init_table)
        TableSState.set(table=init_table)

    #######################################################
    #                       SHOW                          #
    #######################################################

    style = "<style>h3 {text-align: center;}</style>"
    st.markdown(style, unsafe_allow_html=True)
    st.write("### 🐧アニマル数独アプリ")

    left, _ = st.columns([5, 12])
    with left:
        chagne_table_popver = st.popover(label="🐸問題を変える", use_container_width=True)

    with chagne_table_popver:
        with st.form(key="chagne_table_form", border=False):
            n_empty_cells = st.number_input(label="空白なマスの数", min_value=1, value=40, max_value=81, step=1)
            is_change_table_pushed = st.form_submit_button(label="変更", type="primary")

    edited_string_df = st.data_editor(
        key=RerenderSState.get(),
        data=TableSState.get().string_df,
        use_container_width=True,
    )

    left, _, center, _, right = st.columns([5, 1, 5, 1, 5])
    with left:
        explain_popver = st.popover(label="🐔説明を見る", use_container_width=True)
    with center:
        is_restart_pushed = st.button(label="🐶最初から", use_container_width=True)
    with right:
        is_solve_pushed = st.button(label="🐗回答を見る", use_container_width=True, type="primary")

    with explain_popver:
        st.write("🐔縦一列・横一列・3X3グリッド に同じ動物（数字）が入らないようにしてね")

        st.write("⚠️縦一列の例")
        st.image(image=RuleImages.vertical_constraint, use_column_width=True)

        st.write("⚠️横一列の例")
        st.image(image=RuleImages.horizontal_constraint, use_column_width=True)

        st.write("⚠️3X3グリッドの例")
        st.image(image=RuleImages.grid_constraint, use_column_width=True)

    cell_changed_mode = check_cell_changed_mode(
        from_string_df=TableSState.get().string_df,
        to_string_df=edited_string_df,
    )

    is_all_cells_filled = TableSState.get().is_filled

    #######################################################
    #                      ACTION                         #
    #######################################################
    if cell_changed_mode == CellChangedMode.NOT_EMPTY:
        st.toast("🐧埋まっているマスは変えられないよ")
        time.sleep(1.0)
        RerenderSState.call()
        return True

    if cell_changed_mode == CellChangedMode.NOT_NUMBER:
        st.toast("🐧1から9の数字を入力してね")
        time.sleep(1.0)
        RerenderSState.call()
        return True

    if cell_changed_mode == CellChangedMode.COLLECTLY:
        edited_table = Table.from_string_df(string_df=edited_string_df)
        can_solve = check_table_can_solve(table=edited_table)
        if not can_solve:
            st.toast("🐧その数字は入れられないよ")
            time.sleep(1.0)
        else:
            TableSState.set(table=edited_table)
        RerenderSState.call()
        return True

    if is_change_table_pushed:
        NEmptySState.set(n_empty_cells=int(n_empty_cells))
        InitTableSState.clear()
        RerenderSState.call()
        return True

    if is_restart_pushed:
        TableSState.set(table=InitTableSState.get())
        RerenderSState.call()
        return True

    if is_solve_pushed:
        current_table = TableSState.get()
        result_table = solve_table(table=current_table)
        TableSState.set(table=result_table)
        RerenderSState.call()
        return True

    if is_all_cells_filled:
        st.info("🐧遊んでくれてありがとう")
        st.balloons()

    return False

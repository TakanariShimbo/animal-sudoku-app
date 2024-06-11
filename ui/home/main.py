import time

import streamlit as st

from optimization import Table
from .sstates import RerenderSState, TableSState, InitTableSState, NEmptySState, TextsSState
from .cell_change_mode import CellChangedMode, check_cell_changed_mode
from .optimizer import check_table_can_solve, solve_table, prepare_init_table
from .images import RuleImages
from .texts import Texts


N_EMPTY_CELLS_DEFAULT = 20


def show_home() -> bool:
    #######################################################
    #                       INIT                          #
    #######################################################
    if not TextsSState.is_initialized_already():
        TextsSState.set(texts=Texts(lang="en"))

    if not NEmptySState.is_initialized_already():
        NEmptySState.set(n_empty_cells=N_EMPTY_CELLS_DEFAULT)

    if not InitTableSState.is_initialized_already():
        init_table = prepare_init_table(n_empty_cells=NEmptySState.get())
        InitTableSState.set(table=init_table)
        TableSState.set(table=init_table)

    #######################################################
    #                       SHOW                          #
    #######################################################
    texts = TextsSState.get()

    style = "<style>h3 {text-align: center;}</style>"
    st.markdown(style, unsafe_allow_html=True)
    st.write(f"### {texts.title}")

    left, _, right = st.columns([5, 7, 5])
    with left:
        change_problem_popver = st.popover(label=texts.change_problem, use_container_width=True)
    with right:
        is_change_language_pushed = st.button(label=texts.change_language, use_container_width=True)

    with change_problem_popver:
        with st.form(key="change_problem_form", border=False):
            n_empty_cells = st.number_input(label=texts.number_of_empty_cells, min_value=1, value=N_EMPTY_CELLS_DEFAULT, max_value=81, step=1)
            is_change_table_pushed = st.form_submit_button(label=texts.change, type="primary")

    edited_string_df = st.data_editor(
        key=RerenderSState.get(),
        data=TableSState.get().string_df,
        use_container_width=True,
    )

    left, _, center, _, right = st.columns([5, 1, 5, 1, 5])
    with left:
        explanation_popver = st.popover(label=texts.explanation, use_container_width=True)
    with center:
        is_restart_pushed = st.button(label=texts.restart, use_container_width=True)
    with right:
        is_solve_pushed = st.button(label=texts.answer, use_container_width=True, type="primary")

    with explanation_popver:
        st.write(texts.explanation_contents)

        st.write(texts.example_vertical)
        st.image(image=RuleImages.vertical_constraint, use_column_width=True)

        st.write(texts.example_horizontal)
        st.image(image=RuleImages.horizontal_constraint, use_column_width=True)

        st.write(texts.example_grid)
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
        st.toast(texts.not_empty_alert)
        time.sleep(1.0)
        RerenderSState.call()
        return True

    if cell_changed_mode == CellChangedMode.NOT_NUMBER:
        st.toast(texts.not_number_alert)
        time.sleep(1.0)
        RerenderSState.call()
        return True

    if cell_changed_mode == CellChangedMode.COLLECTLY:
        edited_table = Table.from_string_df(string_df=edited_string_df)
        can_solve = check_table_can_solve(table=edited_table)
        if not can_solve:
            st.toast(texts.can_not_solve_alert)
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

    if is_change_language_pushed:
        if texts.is_en:
            TextsSState.set(texts=Texts(lang="jp"))
        elif texts.is_jp:
            TextsSState.set(texts=Texts(lang="en"))
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
        st.success(texts.thanks)
        st.balloons()

    return False

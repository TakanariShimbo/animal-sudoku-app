import streamlit as st
import pandas as pd

from optimization import OrtoolOptimizer, Consts
from ui import RerenderSState, DisplayedNumbersDfSState


def convert_to_displayed_numbers_df(numbers_df: pd.DataFrame) -> pd.DataFrame:
    animal_dict = {
        0: "",
        1: "🐭1",
        2: "🐮2",
        3: "🐯3",
        4: "🐰4",
        5: "🐉5",
        6: "🐍6",
        7: "🐎7",
        8: "🐏8",
        9: "🐵9",
    }

    displayed_numbers_df = pd.DataFrame(
        data=numbers_df.replace(animal_dict).values,
        index=[f"行{i}" for i in numbers_df.index.values],
        columns=[f"列{c}" for c in numbers_df.columns.values],
        dtype=str,
    )
    return displayed_numbers_df


def convert_to_original_numbers_df(displayed_numbers_df: pd.DataFrame) -> pd.DataFrame:
    animal_dict = {
        0: "",
        1: "🐭1",
        2: "🐮2",
        3: "🐯3",
        4: "🐰4",
        5: "🐉5",
        6: "🐍6",
        7: "🐎7",
        8: "🐏8",
        9: "🐵9",
    }
    reverse_animal_dict = {v: k for k, v in animal_dict.items()}

    original_numbers_df = pd.DataFrame(
        data=displayed_numbers_df.replace(reverse_animal_dict).values,
        index=[int(i[1:]) for i in displayed_numbers_df.index.values],
        columns=[int(c[1:]) for c in displayed_numbers_df.columns.values],
        dtype=int,
    )
    return original_numbers_df


def update_displayed_numbers_df(displayed_numbers_df: pd.DataFrame) -> pd.DataFrame:
    animal_dict = {
        "1": "🐭1",
        "2": "🐮2",
        "3": "🐯3",
        "4": "🐰4",
        "5": "🐉5",
        "6": "🐍6",
        "7": "🐎7",
        "8": "🐏8",
        "9": "🐵9",
    }

    return displayed_numbers_df.replace(animal_dict)


def check_is_changed_correctly(from_displayed_numbers_df: pd.DataFrame, to_displayed_numbers_df: pd.DataFrame) -> bool:
    for number in consts.numbers:
        comparison = (from_displayed_numbers_df == "") & (to_displayed_numbers_df == f"{number}")
        if comparison.any().any():
            return True
    return False


def check_is_changed_incorrectly(from_displayed_numbers_df: pd.DataFrame, to_displayed_numbers_df: pd.DataFrame) -> bool:
    comparison = from_displayed_numbers_df != to_displayed_numbers_df
    return comparison.any().any()


def check_is_filled_all(displayed_numbers_df: pd.DataFrame) -> bool:
    return not displayed_numbers_df.isin([""]).any().any()


st.set_page_config(
    page_title="アニマル数独パズル",
    page_icon="🐧",
)

st.write("### 🐧アニマル数独パズル🐧")

fixed_numbers_data = [
    [0, 8, 0, 4, 0, 0, 0, 9, 0],
    [0, 6, 0, 0, 0, 0, 1, 3, 0],
    [0, 0, 1, 7, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 0, 0, 5, 0, 0],
    [7, 0, 5, 0, 9, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 0, 3],
    [5, 2, 0, 3, 0, 0, 0, 7, 6],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
]
fixed_numbers_df = pd.DataFrame(data=fixed_numbers_data, dtype=int)
consts = Consts(fixed_numbers_df=fixed_numbers_df)
DisplayedNumbersDfSState.init(displayed_numbers_df=convert_to_displayed_numbers_df(consts.fixed_numbers_df))

edited_displayed_numbers_df = st.data_editor(
    key=RerenderSState.get(),
    data=DisplayedNumbersDfSState.get(),
)


if check_is_changed_correctly(
    from_displayed_numbers_df=DisplayedNumbersDfSState.get(),
    to_displayed_numbers_df=edited_displayed_numbers_df,
):
    DisplayedNumbersDfSState.set(displayed_numbers_df=update_displayed_numbers_df(displayed_numbers_df=edited_displayed_numbers_df))
    RerenderSState.call()
    st.rerun()


if check_is_changed_incorrectly(
    from_displayed_numbers_df=DisplayedNumbersDfSState.get(),
    to_displayed_numbers_df=edited_displayed_numbers_df,
):
    RerenderSState.call()
    st.rerun()


is_filled_all = check_is_filled_all(displayed_numbers_df=DisplayedNumbersDfSState.get())


left, cencter, right = st.columns([1, 1, 1])
with left:
    is_restart_pushed = st.button(label="最初から🐔")
with cencter:
    is_solve_pushed = st.button(label="回答を見る🐶")
with right:
    is_check_pushed = st.button(label="順調か確認🐗")


if is_restart_pushed:
    fixed_numbers_df = pd.DataFrame(data=fixed_numbers_data, dtype=int)
    consts = Consts(fixed_numbers_df=fixed_numbers_df)
    DisplayedNumbersDfSState.set(displayed_numbers_df=convert_to_displayed_numbers_df(numbers_df=consts.fixed_numbers_df))
    RerenderSState.call()
    st.rerun()


if is_check_pushed and not is_filled_all:
    displayed_numbers_df = DisplayedNumbersDfSState.get()
    consts = Consts(fixed_numbers_df=convert_to_original_numbers_df(displayed_numbers_df=displayed_numbers_df))
    optimizer = OrtoolOptimizer(consts=consts)
    result_numbers_df = optimizer.run()
    if type(result_numbers_df) == pd.DataFrame:
        st.info("順調だよ、その調子🐧")
    else:
        st.error("どこか間違ってるみたい🐧")


if is_solve_pushed:
    displayed_numbers_df = DisplayedNumbersDfSState.get()
    consts = Consts(fixed_numbers_df=convert_to_original_numbers_df(displayed_numbers_df=displayed_numbers_df))
    optimizer = OrtoolOptimizer(consts=consts)
    result_numbers_df = optimizer.run()
    if type(result_numbers_df) == pd.DataFrame:
        DisplayedNumbersDfSState.set(displayed_numbers_df=convert_to_displayed_numbers_df(numbers_df=result_numbers_df))
        RerenderSState.call()
        st.rerun()

    fixed_numbers_df = pd.DataFrame(data=fixed_numbers_data, dtype=int)
    consts = Consts(fixed_numbers_df=fixed_numbers_df)
    optimizer = OrtoolOptimizer(consts=consts)
    result_numbers_df = optimizer.run()
    if type(result_numbers_df) == pd.DataFrame:
        DisplayedNumbersDfSState.set(displayed_numbers_df=convert_to_displayed_numbers_df(numbers_df=result_numbers_df))
        RerenderSState.call()
        st.rerun()

    st.warning("ごめんね、サーバーで問題が発生しているみたい🐧")


if is_filled_all:
    displayed_numbers_df = DisplayedNumbersDfSState.get()
    consts = Consts(fixed_numbers_df=convert_to_original_numbers_df(displayed_numbers_df=displayed_numbers_df))
    optimizer = OrtoolOptimizer(consts=consts)
    result_numbers_df = optimizer.run()
    if type(result_numbers_df) == pd.DataFrame:
        st.info("遊んでくれてありがとう　またね🐧")
        st.balloons()
    else:
        st.error("どこか間違っているみたい🐧")

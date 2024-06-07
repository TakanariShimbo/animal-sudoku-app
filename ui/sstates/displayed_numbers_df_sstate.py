import pandas as pd
import streamlit as st


DISPLAYED_NUMBERS_DF_SSTATE = "DisplayedNumbersDf"


class DisplayedNumbersDfSState:
    @staticmethod
    def get() -> pd.DataFrame:
        return st.session_state[DISPLAYED_NUMBERS_DF_SSTATE]

    @staticmethod
    def set(displayed_numbers_df: pd.DataFrame) -> None:
        st.session_state[DISPLAYED_NUMBERS_DF_SSTATE] = displayed_numbers_df

    @staticmethod
    def init(displayed_numbers_df: pd.DataFrame) -> None:
        if not DISPLAYED_NUMBERS_DF_SSTATE in st.session_state:
            st.session_state[DISPLAYED_NUMBERS_DF_SSTATE] = displayed_numbers_df

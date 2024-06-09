import streamlit as st


N_EMPTY = "N_EMPTY"


class NEmptySState:
    @staticmethod
    def get() -> int:
        return st.session_state[N_EMPTY]

    @staticmethod
    def set(n_empty_cells: int) -> None:
        st.session_state[N_EMPTY] = n_empty_cells

    @staticmethod
    def is_initialized_already() -> bool:
        if N_EMPTY in st.session_state:
            return True
        else:
            return False

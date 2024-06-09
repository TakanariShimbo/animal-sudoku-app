import streamlit as st

from optimization import Table


INIT_TABLE_SSTATE = "INIT_TABLE"


class InitTableSState:
    @staticmethod
    def get() -> Table:
        return st.session_state[INIT_TABLE_SSTATE]

    @staticmethod
    def set(table: Table) -> None:
        st.session_state[INIT_TABLE_SSTATE] = table

    @staticmethod
    def is_initialized_already() -> bool:
        if INIT_TABLE_SSTATE in st.session_state:
            return True
        else:
            return False

    @staticmethod
    def clear() -> None:
        del st.session_state[INIT_TABLE_SSTATE]

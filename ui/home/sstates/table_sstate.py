import streamlit as st

from optimization import Table


TABLE_SSTATE = "TABLE"


class TableSState:
    @staticmethod
    def get() -> Table:
        return st.session_state[TABLE_SSTATE]

    @staticmethod
    def set(table: Table) -> None:
        st.session_state[TABLE_SSTATE] = table

    @classmethod
    def init(cls, table: Table) -> None:
        if not TABLE_SSTATE in st.session_state:
            cls.set(table=table)

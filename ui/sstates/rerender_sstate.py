import streamlit as st


RERENDER_SSTATE = "RERENDER"
INITIAL_VALUE = 0


class RerenderSState:
    @staticmethod
    def get() -> int:
        try:
            return st.session_state[RERENDER_SSTATE]
        except:
            st.session_state[RERENDER_SSTATE] = INITIAL_VALUE
            return st.session_state[RERENDER_SSTATE]

    @staticmethod
    def call() -> None:
        try:
            st.session_state[RERENDER_SSTATE]
        except:
            st.session_state[RERENDER_SSTATE] = INITIAL_VALUE

        st.session_state[RERENDER_SSTATE] += 1

import streamlit as st

from ui import set_app_config, show_home


set_app_config()


is_rerun_required = show_home()
if is_rerun_required:
    st.rerun()

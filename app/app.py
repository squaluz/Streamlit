import streamlit as st
import settings

# Initialize Session State variables used in the client app
# (Must come before imports below)
if 'message' not in st.session_state:
    st.session_state.message = 'None'
if 'token' not in st.session_state:
    st.session_state.token = False
if 'report' not in st.session_state:
    st.session_state.report = []

from common import messageboard, check_token
import app.dumb_app as dumb_app, dumber_app

# The first widget container in the main page is a 'messageboard'
messageboard = st.empty()

def main():
    with st.expander('Authenticate'):
        import component_runner
        from component_event_handler import handle_event
        component_runner.init(handle_event)
    pages = {
        'DuMMMy aPp 1': [dumb_app.main],      # DUMMY APP 1
        'DUmmmY ApP 2': [dumber_app.main],    # DUMMY APP 2
    }
    def _launch_apps():
        messageboard.empty()
        choice = st.sidebar.radio('What do you want to do?', tuple(pages.keys()))
        pages[choice][0](title=choice, *pages[choice][1:])
    if (check_token(st.session_state.token)):
        _launch_apps()
    else:
        messageboard.info('Please login below...')
    # ABOUT
    st.sidebar.title('Component Hero Demo')
    st.sidebar.markdown('---')
    st.sidebar.info('(c) 2022. CloudOpti Ltd. All rights reserved.')

if __name__ == '__main__':
    st.sidebar.image('./logo.png', output_format='png')
    main()
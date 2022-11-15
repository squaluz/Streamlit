EVENTS  = [ 'onStatusUpdate', 'onActionRequest', 'onError' ]
PROPS   = { 'hostname':'Hero Streamlit App',
            'initial_state': {
                'password': settings.ENCRYPT_PASSWORD,
                'message': 'Default Message',
                'action': 'Default Action'
            },
          }
def init(event_handler):
    run_component(declared_component, EVENTS, PROPS, event_handler)

component_runner.init(handle_event)
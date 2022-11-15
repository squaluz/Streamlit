DEFAULT_EVENTS = ['onStatusUpdate', 'onActionRequest', 'onError']
class ComponentHost():
    declared_component = None   # low level declared component host
    key = None
    events = []
    props = {}
 
    class ComponentEvent():
        '''
        Object holding an event name (obj.name), data (obj.data), event source (obj.source).
        name and data can be set to `None`.
        '''
        name = None
        data = None
        source = None
        def __init__(self, host, event):
            e = {}
            if isinstance(event, str):
                e = json.loads(event)
            elif isinstance(event, dict):
                e = event
            event_name = e.get('name', None)
            event_data = e.get('data', None)
            # All events are named
            # Filter by allowed events
            if event_name in host.events:
                self.name = event_name
                self.data = event_data
            else: # report error for unknown and null named events
                self.name = 'onError'
                self.data = {'message': f'Component event {event_name} is not allowed. (Data: {event_data})'}
            self.source = host

    def __init__(self, declared_component, key=None, events=DEFAULT_EVENTS, **props):

        self.declared_component = declared_component
        self.key = key
        self.events = events
        # Allowed props
        self.props = {prop: value for prop, value in props.items() if prop in [
            'hostname', 'initial_state'
        ]}
        # Default prop value
        self.props.setdefault('hostname', 'Default Host')
        self.props.setdefault('initial_state', {'message': 'Default Message', 'action': 'Default Action'})
        self.props.setdefault('events', DEFAULT_EVENTS)
        self.props.setdefault("width", "100%") # built-in prop, height is set in the component itself
        print('### Component Host Ready ###')
        print(f'Event queue: {settings.USE_COMPONENT_EVENT_QUEUE}')
        print(f'Props: {json.dumps(self.props)}')

    def next_event(self):
        # Run declared component
        event = self.declared_component(key=self.key, **(self.props))
        return self.ComponentEvent(host=self, event=event)

    def send_event(self, event):
        '''
        Functionality to send events/data to a component is not supported
        by Streamlit, except when the component is initially mounted :(

        On the other hand, the component can pass events to Streamlit as
        and when it needs to.
        '''
        pass

def run_component(declared_component, events, props, event_handler):
    try:
        run_component_sync(declared_component, events, props, event_handler)
    except Exception as ex:
        print('>> Exception running component <<')
        print(str(ex))

def run_component_sync(declared_component, events, props, event_handler):
    component_host = ComponentHost(declared_component, key='login', events=events, **props)
    event =  component_host.next_event()
    if event:
        try:
            report = event_handler(event)
        except Exception as ex:
            print('>> (run_component_sync) Exception in event handler <<', str(ex))
            report = ['>> (run_component_sync) Exception in event handler <<', str(ex)]
        print_report(report)

def print_report(report):
    print()
    print(f'### [{datetime.now()}] Component event handler report ####')
    print(report)

def handle_event(event):
    if not event:
        # return the preserved report
        return st.session_state.report   
    name = event.name
    data = event.data
    source = event.source
    report = []
    report.append(name)
    report.append(data)

    props = data.get('props', None)
    action = data.get('action', None)

    if name == 'onStatusUpdate':
      pass # DO SOMETHING
    elif name == 'onActionRequest':
      pass # DO SOMETHING
    elif name == 'onError':
      pass # DO SOMETHING
    st.session_state.report = report
    return report
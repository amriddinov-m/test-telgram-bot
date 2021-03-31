from transitions import Machine


class BotStatus(object):
    states = ['created', 'get_order', 'get_payment', 'order_create']

    def __init__(self, name):
        self.name = name

        self.machine = Machine(model=self, states=BotStatus.states, initial='created')
        self.machine.add_transition(trigger='start_order', source='created', dest='get_order')
        self.machine.add_transition(trigger='start_payment', source='get_order', dest='get_payment')
        self.machine.add_transition(trigger='end_order', source='get_payment', dest='order_create')
        self.machine.add_transition(trigger='start', source='created', dest='created')
        self.machine.add_transition(trigger='start_end_order', source='order_create', dest='created')
        self.machine.add_transition(trigger='no_start', source='get_payment', dest='created')

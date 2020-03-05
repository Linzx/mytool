"""
    # The activity's onCreate has been called.
    am_on_create_called(User | 1 | 5), (Component Name | 3), (Reason | 3)
    # The activity's onRestart has been called.
    am_on_restart_called(User | 1 | 5), (Component Name | 3), (Reason | 3)
    # The activity's onStart has been called.
    am_on_start_called(User | 1 | 5), (Component Name | 3), (Reason | 3)
    # The activity's onDestroy has been called.
    am_on_destroy_called(User | 1 | 5), (Component Name | 3), (Reason | 3)
    # The activity's onActivityResult has been called.
    am_on_activity_result_called(User | 1 | 5), (Component Name | 3), (Reason | 3)
"""
class event_am_on_life:
    def __init__(self, name, user, component, reason):
        self.name = name
        self.user = user
        self.component = component
        self.reason = reason


    def to_string(self):
        print('name['+self.user + ', ' + self.component + ', ' + self.reason + ']')



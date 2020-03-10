"""
am_on_stop_called
am_on_create_called
am_on_restart_called
am_on_start_called
am_on_destroy_called
am_on_activity_result_called
am_on_paused_called
am_on_resume_called
am_on_top_resumed_gained_called
am_on_top_resumed_lost_called
am_set_resumed_activity
log format: (User | 1 | 5), (Component Name | 3), (Reason | 3)
"""
class event_am_on:
    name=''
    user=0
    component=''
    reason=''


    def __init__(self, name, user, component, reason):
        self.name = name
        self.user = user
        self.component = component
        self.reason = reason


    def to_string(self):
        print(self.name+' ['+self.user + ', ' + self.component + ', ' + self.reason + ']')



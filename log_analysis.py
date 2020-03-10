import sys
import os


# log format: (User | 1 | 5), (Component Name | 3), (Reason | 3)
am_on_life_events = ['am_on_stop_called',
                     'am_on_create_called',
                     'am_on_restart_called',
                     'am_on_start_called',
                     'am_on_destroy_called',
                     'am_on_activity_result_called',
                     'am_on_paused_called',
                     'am_on_resume_called',
                     'am_on_top_resumed_gained_called',
                     'am_on_top_resumed_lost_called',
                     'am_set_resumed_activity',
                    ]
log_path='readme'


def get_log_path():
    global log_path
    log_path = input('Please attach the log file here, press enter...\n').strip()
    print('log file:%s' % log_path)


def parse_log():
    """
    parse events log
    """
    with open(log_path,'r') as f:
        for line in f:
            for event in am_on_life_events:
                if event in line:
                    print('find event %s in %s' %(event,line))
                else:
                    continue


if __name__=="__main__":
    # get_log_path()
    parse_log()
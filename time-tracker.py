""" This is a program that can keep track your own work and rest time. Created by Crazy-Jack. """
""" Features:
    0) Task setting: You can set your own set in advance for routine work, for example, each day should finish 3 hour GRE working and 3 hour machine learning and 8 hour course work. These setting cannot be canceled once it's set up and you can view your process report to determine how did you do for the specific task each day in a weekly report generated at every Saturday.
    1) When you want to start some task, you call a function called START that can start track your progress name and start time. New progress can be made when you are in other process. However, you can only do one thing each time. When other process is started, the other work should be stopped automaticall. Besides, when the latest process is finished, you can choose to resume the earily process that is not finished yet.
    2) When you are in process:
        2.1) Display: what you will display is a bar that count for your process in this process, 25 mins stragetic, you can see where you are in the 25 mins bar.
        2.2) Change your mind and refresh. After each 25 mins, you should get an alter and change your schedule into the next important course of study. You can choose what to study and you can also let the computer to do the choose for you.
        2.3) In process Operation: If you hit a button, let's say 'p' on the computer, the program will pause counting time and give you a input instruction which wait you to input next instruction, whether to 'resume' for resume, 'end' for end the process, or 'restart' for restart counting.
    3) Daily track: At the end of each day, your program will automatically save your progress and your work after 00:00 will not count. You will recieve an email of the report of what progress you have made yesterday and what's you plan today at 06:00 each day. At 12:00, you will receive an email for your summary for your morning work and adjust your afternoon plan according to what you did or didn't in the morning. The same process happens when 18:00 at evening.
    4) Reporting: you can report your progress using chart that can be put into email. Or for now you can just generated a chart in your local computer. [4.1 00:39, Berkeley]"""


""" Engineer Log:
    1) Build a class called Process for initate setting,  start parameters: project name, distrubuted hours each day....
    2) How to make sure that only one process is running? solution: Write a global variable and update this varible to the latest value.
    3) HOw to stop other counting when global variable changes? Build in __init__ function, if the tracker(Class attribute) is not the same, call stop function
    4) method: STOP(self); Resume(self); START(process_name, start_time=system_time)
    5) How to resume: Have a process list, update when you START and STOP.
"""
import operator as op
import time, datetime

def second_to_hours(second_time):
    if second_time < 60:
        return secondObject(second_time)
    elif second_time < 3600:
        return minsObject(second_time/60)
    else:
        return hoursObject(second_time/3600)

class Time(object):
    time_scale = 60
    def __init__(self, time_span):
        self.span = time_span
    def operation(self, another_input, fn):
        return fn(self.span, another_input.span)

class Seconds(Time):
    def operation(self, another_time, fn):
        if another_time not isinstance(another_time, Second):
            another_time = another_time.convert_to_seconds()
        Time.operation(self, another_time, fn)
    def convert_to_mins(self):
        return Minites(self.span / Time.time_scale)
    def convert_to_hours(self):
        return self.convert_to_mins().convert_to_hours()
class Minites(Time):
    def operation(self, another_time, fn):
        if another_time not isinstance(another_time, Minites):
            another_time = another_time.convert_to_mins()
        Time.operation(self, another_time, fn)
    def convert_to_seconds(self):
        return Seconds(self.span * Time.time_scale)
    def convert_to_hours(self):
        return Hours(self.span / Time.time_scale)
class Hours(Time):
    def operation(self, another_time, fn):
        if another_time not isinstance(another_time, Hours):
            another_time = another_time.convert_to_hours()
        Time.operation(self, another_time, fn)
    def convert_to_mins(self):
        return Minites(self.span * Time.time_scale)
    def convert_to_seconds(self):
        return self.convert_to_mins().convert_to_seconds()







class Process(object):
    def __init__(self, name, distrubuted_hours):
        self.name = name
        self.distrubuted_hours = distrubuted_hours
        self.record = open('record'+'_'+str(datetime.datetime.now()), 'w')
        self.count = 1
    def start(self, now_time = time.time()):
        self.start_time = now_time
        self.count += 1
        self.record.write('NAME: '+str(self.name)+' '+'start at '+str(self.start_time))
        self.record.close()
    def end(self, now_time = time.time()):
        self.end_time = now_time
        self.duration = operation(self.end_time, self.start_time, op.)



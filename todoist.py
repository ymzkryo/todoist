#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from pytodoist import todoist
from lib.date import Date

date = Date()
class Todoist():
    def login(self,API_TOKEN):
        user = todoist.login_with_api_token(API_TOKEN)
        return user

    def get_projects(self, user):
        return  user.get_projects()

    def get_tasks(self, user):
        tasks =  user.get_tasks()
        now = date.get_now()
        for task in tasks:
            target_date = task.due_date_utc
            if not target_date is None:
                fuga = date.str_to_date(target_date)
                print(date.date_to_str(date.utc_to_jst(fuga)) + ' ' + task.content)
            #print(str(task.id) + ' ' + task.project.name + ' ' + task.content + ' ' + date.date_to_str(task.due_date_utc, '%Y-%m-%D %H:%M:%S'))
    def add_task(self, content, projects, project=None, due=None):
        print(content)
        return

    def complete_task(self, content, projects, project=None):
        print(content)
        return

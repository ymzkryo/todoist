#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from pytodoist import todoist
import sys
import argparse


def main():
    user = todoist.login_with_api_token(API_TOKEN)
    today_tasks = user.search_tasks(todoist.Query.PRIORITY_1, todoist.Query.PRIORITY_2)
    for task in today_tasks:
        print(task.content + ' ' + str(task.id) + ' ' + str(task.due_date_utc) + ' ' + task.date_string)

if __name__ == '__main__':
    main()

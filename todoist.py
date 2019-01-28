#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from pytodoist import todoist
import sys
import argparse
import json

def load_json():
    f = open('config.json', 'r')
    json_data = json.load(f)
    f.close()
    return json_data['api_token']

def main():                                    
    API_TOKEN = load_json()
    print(API_TOKEN)
    user = todoist.login_with_api_token(API_TOKEN)
    today_tasks = user.search_tasks(todoist.Query.PRIORITY_1, todoist.Query.PRIORITY_2)
    for task in today_tasks:
        print(task.content + ' ' + str(task.id) + ' ' + str(task.due_date_utc) + ' ' + task.date_string)

if __name__ == '__main__':
    main()

#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from pytodoist import todoist

# main class
class Main():
    # login
    # @param self
    # @return user
    def login(self):                                    
        API_TOKEN = lib.load_json()
        user = todoist.login_with_api_token(API_TOKEN)
        return user

    # list all task
    # @param self
    # @param user
    # @param args_list
    def get_tasks(self, user, args_list):
        if (len(args_list) != 0):
            start_date = args_list[0]
            end_date = args_list[1]
        else:
            start_date = 'today'
            end_date = 'tomorrow'
        tasks = user.search_tasks(start_date, end_date)
        for task in tasks:
            print(task.content + ' ' + str(task.id) + ' ' + str(task.due_date_utc) + ' ' + task.date_string)
    
    # add new task
    # @param self
    # @param user
    # @param args_list
    def add_task(self, user, args_list):
        task_name = args_list[0]
        inbox = user.get_project('Inbox')
        install_task = inbox.add_task(task_name)
        if install_task:
            print('add Task success!')
            print('add Task detail:')
            print('task name:' + task_name + ' project:Inbox')

    # complete task
    def complete_task(self):
        return

# library class
class Library():
    # load_json
    # @return api_token
    def load_json(self):
        import json
        f = open('config.json', 'r')
        json_data = json.load(f)
        f.close()
        return json_data['api_token']

    # get_args
    # @return args
    def get_args(self):
        import argparse
        import sys
        usage = 'Usage: python FILE [--add] [--list <start_date> <end_date>] [--complete] [--help]'.format(__file__)
        parser = argparse.ArgumentParser(usage = usage)
        parser.add_argument('-l', '--list', nargs=2, action='append', help='--list start_date end_date')
        parser.add_argument('-a', '--add', nargs='*', action='append', help='show add message')
        #parser.add_argument('-c', '--complete', nargs='*', action='append', help='show complete message')
        args = parser.parse_args()
        return args

    # parse_argment_list
    # @param arg_list
    # @result_list
    def parse_argment_list(self, arg_list):
        result_list = arg_list[0]
        return result_list

if __name__ == '__main__':
    lib = Library()
    main = Main()
    args = lib.get_args()
    user = main.login()
    if (args.add):
        args_list = lib.parse_argment_list(args.add)
        if (len(args_list) != 0):
            main.add_task(user, args_list)
    if (args.list):
        args_list = lib.parse_argment_list(args.list)
        if (len(args_list) != 0):
            print('hoge')
        #main.get_todays_tasks(user)
        main.get_tasks(user, args_list)
    if (args.complete):
        args_list = lib.parse_argment_list(args.complete)
        #if (len(args_list) != 0):
            #main.complete_task(user, args_list)

#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from dog import dog
from lib.certification import Certification
from todoist import Todoist
from lib.argument import Argument

class Main():

    
    def main(self):
        """
        main function
        app start

        """
        dog = Dog()
        dog.show_name()
        API_TOKEN = certification.load_json()
        if not API_TOKEN:
            print('[WARN]:Please set the API token in config.json')
        user = todoist.login(API_TOKEN)
        user.sync()
        projects = todoist.get_projects(user)
        args = argument.get_argument()
        if args.function.lower() == 'add':
            todoist.add_task(user, args.content, projects, 
                    project=args.project, due=args.due, priority=args.priority)
            user.update()
        elif args.function.lower() == 'list':
            todoist.get_tasks(user, args.query)
        elif args.function.lower() == 'complete':
            todoist.complete_task(user, args.content)
            user.update()


if __name__ == '__main__':
    certification = Certification()
    todoist = Todoist()
    argument = Argument()
    main = Main()
    main.main()

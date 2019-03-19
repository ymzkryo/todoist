# todoist

This will do the task list of todoist.  
It works in the CLI.  

# Dependency

- python3+
- certifi
- chardet
- idna
- pytodoist
- pytz
- requests
- urllib3


## Install Dependency library

```
pip instasll -r requirements.txt
```

# Setup

```
git clone https://github.com/yamachaaan/py-todoist-cli.git  
cd py-todoist-cli  
python ./main.py
```

# Usage

## settings

### step1
you get todoist API TOKEN  
[here](https://todoist.com/prefs/integrations)  

### step2
you create `./config.json`  


```
{
    "api_token":"YOUR TODOIST API TOKEN"
}

```

## list your tasks

There are tow patterns.  

### LIST ALL TASKS

```
$ .main.py list
```

### LIST OVERDUE and TODAY's TASKS

```
$ .main.py list -q today
```

# Licence
This software is released under the MIT License, see LICENSE.  

# Authors

yamachaaan  
[@ymzkryo](https://twitter.com/ymzkryo)  

# References

- [Todoist API Documents](https://developer.todoist.com/sync/v8/)
- [Doist/todoist-python](https://github.com/Doist/todoist-python)
- [Garee/pytodoist](https://github.com/Garee/pytodoist)
- [sachaos/todoist](https://github.com/sachaos/todoist)

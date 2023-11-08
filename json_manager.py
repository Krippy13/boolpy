#!/bin/python3

from boolpy.logger import get_logger
print("biscotto") 
logger = get_logger('JsonManager')

# $ # $ # $ # $ # $ # $ # $ # $ # $

import os
import re
import json
import asyncio
from typing import Any, Union, Optional, List

def prepare_for_json(
    iterable: Union[
        object, 
        list,
        dict,
        tuple
    ]
) -> Union[list, dict]:

    if hasattr(iterable, '__dict__'):
        iterable = iterable.__dict__

    if not isinstance(iterable, (list, dict, tuple)):
        raise TypeError("'iterable' must be dict, list, tuple"
                        + " or the instance of a class, got "
                        + iterable.__class__.__name__)

    if isinstance(iterable, (list, tuple)):
        result = []
        for item in iterable:
            if hasattr(item, '__dict__'):
                result.append(prepare_for_json(item))
            else:
                if isinstance(item, (list, tuple)):
                    inner_list = []
                    for ele in item:
                        if hasattr(ele, '__dict__'):
                            ele = prepare_for_json(ele)
                        inner_list.append(ele)
                    result.append(inner_list)
                else:
                    result.append(item)

    elif isinstance(iterable, dict):
        result = {}
        for key, value in iterable.items():
            if (
                hasattr(value, '__dict__')
                or isinstance(value, (list, tuple))
            ):
                result[key] = prepare_for_json(value)
            else:
                result[key] = value

    return result

# $ # $ # $ # $ #

def check_dict(iterable: Union[str, dict]) -> dict:
    if isinstance(iterable, str):
        return json.loads(iterable)

    elif isinstance(iterable, dict):
        return iterable.copy()
    else:
        raise TypeError('iterable must be dict or str, got '
                        + iterable.__class__.__name__)

# $ # $ # $ # $ # $ # $ # $ # $ # $ # $ #

class JsonManager:
    def __init__(self, path: Optional[str]) -> None:

        if not isinstance(path, (str, type(None))):
            raise TypeError("path parameter must be of type str, pass"
                            + " None to use the current directory")

        if path is not None and not os.path.isdir(path):
            raise ValueError("path parameter must be a directory,"
                             + " pass None to use the current one.")

        if path is None: path = './'
        if not path.endswith('/'): path += '/'

        self.path = path
        self.tasks = []
        self.updates = {}

    def json_format(self, file_name) -> str:
        if not str(file_name).endswith('.json'):
            file_name = '%s.json' % file_name
        return file_name

    def __updating(func: Any):
        def inner(self, *args, **kwargs):
            self.tasks.append(func)
            result = func(self, *args, **kwargs)
            self.tasks.remove(func)
            return result
        return inner

# $ # $ # $ # $ # $ #

    @__updating
    def push(self, key, data: dict, ensure_int:bool = True) -> dict:

        if (ensure_int is True
            and re.match(r'^(\-|\d){0,1}\d+$', str(key))):

            key = int(key)

        self.updates[key] = data
        return self.updates[key]



    @__updating
    def get(self, key, ensure_int:bool = True) -> dict:

        if (ensure_int is True
            and re.match(r'^(\-|\d){0,1}\d+$', str(key))):
 
            key = int(key)

        if key not in self.updates:
            file_name = self.json_format(key)

            with open(self.path + file_name) as read_json:
                self.updates[key] = json.loads(read_json.read())

            logger.debug(f'Got {key} from file')
        else:
            logger.debug(f'Got {key} from updates')

        return self.updates[key]



    @__updating
    def merge(self, _lambda = lambda s: re.match(r'^(\-|\d){0,1}\d+\.json$', s)) -> dict:

        for file_name in os.listdir(self.path):

            if _lambda(file_name):

                key = re.sub('.json', '', file_name)
                value = self.get(key)
            else:
                logger.info(f"Unexpected file {self.path}{file_name}")

        return self.updates

# $ # $ # $ # $ # $ # $ # $ #

    @__updating
    def check(self, key, check_dict: dict) -> dict:

        file_name = self.json_format(key)

        if not (key in self.updates
                or os.path.isfile(self.path + file_name)):

            result = check_dict
        else:
            result = {}
            actual_dict = self.get(key)
            for x, val in check_dict.items():

                if x in actual_dict:
                    val = actual_dict[x]

                result.update({x: val})

        self.updates[key] = result

        return self.updates[key]

# $ # $ # $ # $ # $ # $ # $ # $ #

    def push_updates(self) -> None:

        updates = self.updates
        self.updates = {}

        for key in updates:
            value = updates[key]
            file_name = self.json_format(key)
            logger.debug(f'Pushing {key} {value}')

            with open(self.path + file_name, 'w') as push_json:
                push_json.write(json.dumps(value, indent = 2))



    async def process_updates(self, timeout: int = 30) -> None:
        try:
            while True:
                if self.updates and not self.tasks:
                    self.push_updates()
                await asyncio.sleep(timeout)
        except:
            self.push_updates()
            raise


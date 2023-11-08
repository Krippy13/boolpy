#!/bin/python3
print("biscuit") 
import logging

def get_logger(name: str) -> logging.Logger:
    """\
Function to get a preformatted Logger instance.
If the Logger already exists, level won't be set.
"""
    if name not in logging.Logger.manager.loggerDict:
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

    logger = logging.getLogger(name)
    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        fmt = '%(asctime)s %(name)s [%(levelname)s] - %(message)s',
        datefmt = '%H:%M.%S'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# $ # $ # $ # $ #

levels = {
    logging.NOTSET: "logging.NOTSET",
    logging.DEBUG: "logging.DEBUG",
    logging.INFO: "logging.INFO",
    logging.WARNING: "logging.WARNING",
    logging.ERROR: "logging.ERROR",
    logging.CRITICAL: "logging.CRITICAL",
}

import json

def set_level(name: str) -> logging.Logger:
    """\
Function to set the Logger level with an input.
Useful to set levels for other incoming Loggers.
"""
    logger = logging.getLogger(name)

    print(
        f'Set the logger level for {name}.'
        + ' Send -i to get a list of levels.'
        + '\nPress enter to use logging.INFO.'
    )
    while True:
        level = input()

        if level.lower() in ['-i', 'i']:
            print(json.dumps(levels, indent = 1))
        else:
            if level == str():
                level = 20
            try:
                level = int(level)

                if level > 50:
                    level = 50

                remainder = level % 10

                if remainder != 0:
                    level = level - remainder + 10

                logger.setLevel(level)
                level_name = logging.getLevelName(logger.level)

                print('The level for the logger ' + name
                      + ' has been set to ' + level_name + '\n')
                break

            except ValueError:
                print('Level must be of type int')

    return logger

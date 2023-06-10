"""
Package reqto ... A wrapper around requests enabling to cut timeout directly after specified time
"""

import eventlet
eventlet.monkey_patch()
from requests import *
import requests


def get(url, timeout=None, timeout_function=None, timeout_args=None, **kwargs):
    try:
        if type(timeout)==list or type(timeout)==tuple:
            timeout=timeout[0]
        with eventlet.Timeout(timeout):
            arguments={**{"url":url},**kwargs}
            response = requests.get(**arguments)
        return(response)
    except eventlet.timeout.Timeout as exc:
        if timeout_function is not None:
            if timeout_args is not None:
                timeout_function(timeout_args)
            else:
                timeout_function()
        else:
            raise requests.exceptions.Timeout from exc

def post(url, data=None, json=None, timeout=None, timeout_function=None, timeout_args=None, **kwargs):
    try:
        if type(timeout)==list or type(timeout)==tuple:
            timeout=timeout[0]
        with eventlet.Timeout(timeout):
            arguments={**{"url":url, "data":data, "json":json},**kwargs}
            response = requests.post(**arguments)
        return(response)
    except eventlet.timeout.Timeout as exc:
        if timeout_function is not None:
            if timeout_args is not None:
                timeout_function(timeout_args)
            else:
                timeout_function()
        else:
            raise requests.exceptions.Timeout from exc

def put(url, data=None, timeout=None, timeout_function=None, timeout_args=None, **kwargs):
    try:
        if type(timeout)==list or type(timeout)==tuple:
            timeout=timeout[0]
        with eventlet.Timeout(timeout):
            arguments={**{"url":url, "data":data},**kwargs}
            response = requests.put(**arguments)
        return(response)
    except eventlet.timeout.Timeout as exc:
        if timeout_function is not None:
            if timeout_args is not None:
                timeout_function(timeout_args)
            else:
                timeout_function()
        else:
            raise requests.exceptions.Timeout from exc

def patch(url, data=None, timeout=None, timeout_function=None, timeout_args=None, **kwargs):
    try:
        if type(timeout)==list or type(timeout)==tuple:
            timeout=timeout[0]
        with eventlet.Timeout(timeout):
            arguments={**{"url":url, "data":data},**kwargs}
            response = requests.patch(**arguments)
        return(response)
    except eventlet.timeout.Timeout as exc:
        if timeout_function is not None:
            if timeout_args is not None:
                timeout_function(timeout_args)
            else:
                timeout_function()
        else:
            raise requests.exceptions.Timeout from exc

def delete(url, timeout=None, timeout_function=None, timeout_args=None, **kwargs):
    try:
        if type(timeout)==list or type(timeout)==tuple:
            timeout=timeout[0]
        with eventlet.Timeout(timeout):
            arguments={**{"url":url},**kwargs}
            response = requests.delete(**arguments)
        return(response)
    except eventlet.timeout.Timeout as exc:
        if timeout_function is not None:
            if timeout_args is not None:
                timeout_function(timeout_args)
            else:
                timeout_function()
        else:
            raise requests.exceptions.Timeout from exc

def head(url, timeout=None, timeout_function=None, timeout_args=None, **kwargs):
    try:
        if type(timeout)==list or type(timeout)==tuple:
            timeout=timeout[0]
        with eventlet.Timeout(timeout):
            arguments={**{"url":url},**kwargs}
            response = requests.head(**arguments)
        return(response)
    except eventlet.timeout.Timeout as exc:
        if timeout_function is not None:
            if timeout_args is not None:
                timeout_function(timeout_args)
            else:
                timeout_function()
        else:
            raise requests.exceptions.Timeout from exc

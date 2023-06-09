#!/bin/env python3

import unidecode
import importlib
import os
import sys
import threading
import json
import hashlib
import inspect
import time
from fastapi import FastAPI,APIRouter


app = FastAPI()
router = APIRouter()

plugins = {}


def _help():
	print("help is missing")


def hash_file(filename=""):
	BUF_SIZE = 65536
	md5 = hashlib.md5()
	with open(filename, 'rb') as f:
		while True:
			data = f.read(BUF_SIZE)
			if not data:
				break
			md5.update(data)
	return md5.hexdigest()


def reload_plugins():
	folder = "plugins"
	for name in os.listdir(folder):
		if (name[-3:] == ".py") and (name[0] != '_'):
			module_name = name[:-3]

			if module_name in globals().keys():
				if plugins[module_name] != hash_file(os.path.join(folder, name)):
					globals()[module_name] = importlib.reload(globals()[module_name])
					plugins[module_name] = hash_file(os.path.join(folder, name))
					# print(module_name + " reloaded")
			else:
				globals()[module_name] = importlib.import_module(folder + "." + module_name)
				plugins[module_name] = hash_file(os.path.join(folder, name))
				# print(module_name + " imported")


def update():
	reload_plugins()
	for module in plugins.keys():
		for func in dir(globals()[module]):
			if func[0] != '_':
				dynamic_function = dict(inspect.getmembers(globals()[module]))[func]
				if callable(dynamic_function):
					router.add_api_route(str("/" + module + "/" + func), dynamic_function)


@app.get("/help")
def list_functions():
	update()
	ret = {}
	for module in plugins.keys():
		for func in dir(globals()[module]):
			if func[0] != '_':
				dynamic_function = dict(inspect.getmembers(globals()[module]))[func]
				if callable(dynamic_function):
					ret["/" + module + "/" + func] = "/" + module + "/" + func
					if ((inspect.signature(dynamic_function)) is not None):
						ret["/" + module + "/" + func] += str(inspect.signature(dynamic_function))
					if ((dynamic_function.__doc__) is not None):
						ret["/" + module + "/" + func] += '\n' + dynamic_function.__doc__
	return ret


update()
app.include_router(router)

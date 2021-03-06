import sys
sys.dont_write_bytecode=True
from jinja2 import Template
import os

from duck import datadir
from duck.launcher import Plugins
#Search event
def Search(query, color=None,font=None):
	static="{}plugins/plugins/".format(datadir.getDir())
	s = str(open("{}plugins.html".format(static),"r").read())
	rep=Plugins.Repo()
	plugins=rep.getAllApps()
	t=Template(s)
	return t.render(font=font,static="file://{}".format(static),plugins=plugins)

#JS function events
def onFormSubmit(elements):
	for e in elements:
		if e.has_key("name") and e["name"]=="who":
			print e["value"]
def onDataSent(object, value):
	if object=="openFile":
		import webbrowser
		webbrowser.open(value)

from pybuilder.core import use_plugin, init

use_plugin("python.core")

description = "Demo Project for Blitz17"
name = "flask-peewee-example"
version = '0.0.1'
default_task = ['clean', 'publish']

@init
def set_properties(project):
    project.set_property("dir_source_main_python", "example")
    

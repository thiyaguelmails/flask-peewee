from pybuilder.core import use_plugin, init

use_plugin("python.core")

name = "flask-peewee-example"
default_task = "publish"

@init
def set_properties(project):
    project.set_property("dir_source_main_python", "/var/lib/jenkins/workspace/flask-peewee")

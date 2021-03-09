# submodule package install
import cool_lib
import somepackage

from clearml import Task
task = Task.init(project_name='elinep', task_name='submodule_task')
print("done")

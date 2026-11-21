# Task Tracker CLI

#### Task management application that uses python, works directly within your terminal. Allows the user to create, update, delete, and track tasks

#### All tasks that are inputted are stored locally in JSON, so they exist outside the session

### Features
* **Add tasks using a description**
* **List tasks in terminal with a formatted table**
* **Track progress of tasks using status keywords : todo, in-progress, and done**
* **Filter tasks by current status**
* **Delete tasks automatically if done, confirmation required if status is NOT done**
* **Cross-platform data storage using platformdirs module**

### Requirements/Installation
* **Python3 and pip/pipx**
* **Clone repository https://github.com/GafiTC/TaskTrackerCLI.git and type cd TaskTracker --> pipx install . OR use pipx install in a Python virtual environment**

### Usage
#### Add/Delete a task
*task-cli delete "ID# of specific task"*  
*task-clid add "Name of task"*

#### List tasks       
*task-cli list {todo, in-progress, done}*

#### Mark tasks
*task-cli  mark (done, in progress) + ID# of task*


 



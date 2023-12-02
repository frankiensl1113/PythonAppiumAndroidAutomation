from todoist_api_python.api import TodoistAPI

api = TodoistAPI("ecd3cd96e3697bb7f9df27b4275475f38d695023")


class TodoistAction:
    @staticmethod
    def add_project(projectname):
        try:
            project = api.add_project(projectname)
            print("Created Project through API and the response is: "+str(project))
            return project
        except Exception as error:
            print(error)

    @staticmethod
    def delete_project(projectid):
        try:
            is_success = api.delete_project(project_id=projectid)
            print(is_success)
            return is_success
        except Exception as error:
            print(error)

    @staticmethod
    def get_project():
        try:
            projects = api.get_projects()
            print(projects)
            return projects
        except Exception as error:
            print(error)

    @staticmethod
    def add_task(tasktname, pid):
        try:
            task = api.add_task(content=tasktname, project_id=pid)
            print(task)
            return task
        except Exception as error:
            print(error)

    @staticmethod
    def get_active_task():
        try:
            tasks = api.get_tasks()
            print("GET active task belong to the current user through todoist API, response " + str(tasks))
            return tasks
        except Exception as error:
            print(error)

    @staticmethod
    def reopen_task(id):
        try:
            is_success = api.reopen_task(task_id=id)
            print("Reopen task API is called: and return response " + str(is_success))
        except Exception as error:
            print(error)

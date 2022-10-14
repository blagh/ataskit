class Task:

    def __init__(self):
        self.name = ""
        self.description = "" # rich text someday
        self.parent = None # multi?
        self.children = [] # careful about loops
        self.created_by = None
        self.assigned_to = []

        self.audit_log = []


    def add_child(self, task):
        parent = self.parent
        while (parent):
            if task == parent:
                raise "Can't set child to ancestor"

            parent = parent.parent

        self.children.append(task)

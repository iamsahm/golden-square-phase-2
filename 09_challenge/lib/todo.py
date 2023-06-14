class Todo:
    
    def __init__(self, task) -> None:
        self.task = task
        self.complete = False
        pass

    def mark_complete(self):
        self.complete = True
        pass

class TodoList:

    def __init__(self): 
        self.entries = []
        pass

    def add(self, todo):
        self.entries.append(todo)

    def complete(self):
        return list(filter(lambda e: e.complete == True, self.entries))

    def incomplete(self):
        return list(filter(lambda e: e.complete == False, self.entries))

    def give_up(self):
        for i in self.entries:
            i.complete = True
        pass
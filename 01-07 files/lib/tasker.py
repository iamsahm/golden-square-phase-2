# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.


class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        self.name = name
        self.tasklist = []
        # Side effects:
        #   Sets the username property of the self object
        pass # No code here yet

    def remind_me_to(self, task):
        # Parameters:
        #   task: string representing a single task
        if type(task)!=str:
            raise Exception('Only strings in the task list pls')
        self.tasklist.append(task)
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def remind(self):
        # Returns:
        #   A string reminding the user to do the task
        if len(self.tasklist) != 0:
            list_to_string = ', '.join(self.tasklist)
            return f'Here is your tasklist: {list_to_string}'
        else:
                raise Exception('You are all caught up! Well done!')
    
        # Side-effects:
        #   Throws an exception if no task is set
     # No code here yet

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.
    def complete_task(self, task):
        # returns:
        # nothing
        if task in self.tasklist:
             self.tasklist.pop(self.tasklist.index(task))
        else:
             raise Exception('That task is not on the task list!')

        # side-effects:
        # Throws an exception if no user exists

        # Throws an exception if no task exists
        # removes task from the list


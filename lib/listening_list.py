# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.

# add strings to a list and return them when called
class ListeningList():

    def __init__(self):
        self.listened_list = []
        pass
    # init function
    # no parameters, no returns
    # adds empty listening list

    def add_track(self, track):
        if type(track) != str:
            raise Exception('dont put a number in me!')
        self.listened_list.append(track)
    # function: add track
    # parameters: string
    # returns nothing

    def view_list(self):
        if self.listened_list == []:
            raise Exception('You have not listened to anything!')

        return f'Here is a list of tracks you have heard: {", ".join(self.listened_list)}'
    # function: view listening list
    # parameters: none
    # returns: listening list
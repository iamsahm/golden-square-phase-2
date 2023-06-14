As a user
So that I can record my experiences
I want to keep a regular diary

Diary class
    read
    read diary entry based on wpm
    takes DiaryEntry class
        add
        return contents
    takes todolist class
        add todo
        incomplete
        complete
        give_up
    mobile_numbers method
        searches contents
        returns mobile phone numbers in contents


       ┌────────────────────────────────────────┐
       │                                        │
       │-Diary                                  │
       │ -add(DiaryEntry)                       │
       │ -read contents                         │
       │  >returns all contents as list         │
       │ -read contents per wpm + mins          │
       │  >returns contents that match wpm/mins │
    ┌──┤                                        │
    │  └───────────────────┬────────────────────┘
    │                      │
    │                      ▼    owns a list of
    │  ┌────────────────────────────────────────┐
    │  │-DiaryEntry(title, contents)            │
    │  │ -count_words                           │
    │  │  >returns len(contents)                │
    │  │ -list_mobiles                          │
    │  │  >list of all mobile formatted numbers │
owns│a │                                        │
    │  │                                        │
    │  └────────────────────────────────────────┘
    │
    │
    │  ┌───────────────────────────────────────┐
    │  │todolist                               │
    │  │-add(ToDo)                             │
    │  │-complete                              │
    │  │ >list of completed tasks              │
    └─►│-incomplete                            │
       │ >list of uncompleted tasks            │
       │-give up                               │
       │ >sets all tasks to complete           │
       └───────────────────────────────────────┘
                          ▼     owns a list of
       ┌───────────────────────────────────────┐
       │ToDo(task)                             │
       │-add                                   │
       │ -adds task to tasklist                │
       │-mark_complete                         │
       │ -sets task to complete                │
       └───────────────────────────────────────┘






As a user
So that I can reflect on my experiences
I want to read my past diary entries


As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed


As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries



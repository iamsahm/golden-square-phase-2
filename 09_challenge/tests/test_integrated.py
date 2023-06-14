from lib import *

DIARY_ENTRY_1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean scelerisque, ligula at suscipit hendrerit, mauris arcu venenatis magna, ut ullamcorper ex sapien sit amet sem. Nulla congue ipsum ut dui lacinia fermentum. Sed a ligula a arcu vulputate scelerisque sit amet eget erat. In lacus elit, posuere ac risus sed, accumsan dignissim odio. Sed malesuada magna suscipit porttitor ultrices. Vestibulum tempus tempor erat, sed varius enim ornare in. Phasellus nec libero in arcu pretium pellentesque sed a elit. Vivamus velit purus, malesuada vitae consectetur a, aliquet vel odio."

DIARY_ENTRY_2 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean scelerisque, ligula at suscipit hendrerit, mauris arcu venenatis magna, ut ullamcorper ex sapien sit amet sem. Nulla congue ipsum ut dui lacinia fermentum. Sed a ligula a arcu vulputate scelerisque sit amet eget erat. In lacus elit, posuere ac risus sed, accumsan dignissim odio. Sed malesuada magna suscipit porttitor ultrices. Vestibulum tempus tempor erat, sed varius enim ornare in. Phasellus nec libero in arcu pretium pellentesque sed a elit. Vivamus velit purus, malesuada vitae consectetur a, aliquet vel odio.
Suspendisse ultricies odio id risus maximus dictum. Suspendisse potenti. Aenean vestibulum ut leo a porta. Nunc in lectus urna. Quisque vel cursus elit. Quisque tellus lacus, bibendum eget commodo rutrum, varius ac lorem. Praesent gravida molestie gravida. Praesent posuere arcu nec sapien bibendum, eget bibendum magna iaculis. Phasellus a malesuada ipsum. Nunc semper vitae quam nec mattis. Nulla facilisi. Sed ultrices lectus turpis, non rutrum lectus pretium ut. Suspendisse tincidunt rhoncus libero in tempor. Aenean consectetur, justo at sollicitudin consectetur, justo nisl imperdiet orci, ac lobortis ante ligula et libero. Maecenas posuere quam sit amet pellentesque gravida.
In tincidunt tellus ligula, quis aliquam tortor blandit ac. Pellentesque lectus purus, commodo non leo eu, pellentesque aliquet ex. Curabitur suscipit ullamcorper lorem, et tempor leo venenatis sagittis. In nec nibh lacus. Mauris vitae molestie justo. Proin vehicula neque ut sagittis accumsan. Vivamus eu vulputate magna. Suspendisse dapibus dictum blandit. Cras feugiat placerat elit, ut feugiat ipsum efficitur sed. Aenean finibus erat elit, ut placerat ex condimentum vitae. Phasellus rhoncus augue vitae nibh consequat venenatis. Phasellus efficitur sodales dui, in euismod nisi sagittis in. Donec accumsan in ipsum ac semper. Suspendisse vestibulum leo at suscipit pharetra. """

DIARY_ENTRY_3 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean scelerisque, ligula at suscipit hendrerit, mauris arcu venenatis magna, ut ullamcorper ex sapien sit amet sem. Nulla congue ipsum ut dui lacinia fermentum. Sed a ligula a arcu vulputate scelerisque sit amet eget erat. In lacus elit, posuere ac risus sed, accumsan dignissim odio. Sed malesuada magna suscipit porttitor ultrices. Vestibulum tempus tempor erat, sed varius enim ornare in. Phasellus nec libero in arcu pretium pellentesque sed a elit. Vivamus velit purus, malesuada vitae consectetur a, aliquet vel odio.
Suspendisse ultricies odio id risus maximus dictum. Suspendisse potenti. Aenean vestibulum ut leo a porta. Nunc in lectus urna. Quisque vel cursus elit. Quisque tellus lacus, bibendum eget commodo rutrum, varius ac lorem. Praesent gravida molestie gravida. Praesent posuere arcu nec sapien bibendum, eget bibendum magna iaculis. Phasellus a malesuada ipsum. Nunc semper vitae quam nec mattis. Nulla facilisi. Sed ultrices lectus turpis, non rutrum lectus pretium ut. Suspendisse tincidunt rhoncus libero in tempor. Aenean consectetur, justo at sollicitudin consectetur, justo nisl imperdiet orci, ac lobortis ante ligula et libero. Maecenas posuere quam sit amet pellentesque gravida.
In tincidunt tellus ligula, quis aliquam tortor blandit ac. Pellentesque lectus purus, commodo non leo eu, pellentesque aliquet ex. Curabitur suscipit ullamcorper lorem, et tempor leo venenatis sagittis. In nec nibh lacus. Mauris vitae molestie justo. Proin vehicula neque ut sagittis accumsan. Vivamus eu vulputate magna. Suspendisse dapibus dictum blandit. Cras feugiat placerat elit, ut feugiat ipsum efficitur sed. Aenean finibus erat elit, ut placerat ex condimentum vitae. Phasellus rhoncus augue vitae nibh consequat venenatis. Phasellus efficitur sodales dui, in euismod nisi sagittis in. Donec accumsan in ipsum ac semper. Suspendisse vestibulum leo at suscipit pharetra.
Vivamus at nisl id felis rhoncus ullamcorper eget et quam. Nam vulputate ante sit amet enim congue, id vehicula felis dapibus. Aliquam erat volutpat. Quisque eu interdum ligula. Quisque molestie nulla a nisl scelerisque, ac sagittis tellus vestibulum. Morbi sit amet aliquet libero. Aliquam vitae mauris id felis pretium varius et eu risus. Donec sed lorem nec ipsum consequat tempus mattis et libero. Pellentesque iaculis porttitor dui eu congue. Suspendisse potenti. Donec et posuere elit. Donec vestibulum rhoncus urna in elementum. Duis non ante ultricies, efficitur est varius, aliquam enim.
Maecenas mattis purus eget nunc sollicitudin, at mollis lorem facilisis. Duis felis eros, luctus vitae accumsan eget, scelerisque quis velit. Nulla tincidunt lobortis ante sit amet tempor. In vel nunc non orci posuere laoreet. Donec imperdiet varius auctor. Vivamus venenatis lorem at tortor laoreet egestas. Ut maximus, eros ut luctus congue, eros dui molestie mauris, id aliquet urna elit at sem."""

def test_diary_add():
    diary = Diary()
    diary_entry = DiaryEntry("My Diary", "My first entry!")

    diary.add(diary_entry)

    assert diary_entry in diary.read_all()

def test_diary_init():
    diary = Diary()
    assert diary.read_all() == []

def test_diary_read():
    diary = Diary()
    diary.add(DiaryEntry("My Diary", "My 1"))
    diary.add(DiaryEntry("My 2", "my 2"))
    diary.add(DiaryEntry("My 3", "My 3"))

    assert len(diary.read_all()) == 3

def test_find_best_diary_for_time():
    diary = Diary()
    entry_1 = diary.add(DiaryEntry("My 1", DIARY_ENTRY_1))
    entry_2 = diary.add(DiaryEntry("My 2", DIARY_ENTRY_2))
    entry_3 = diary.add(DiaryEntry("My 3", DIARY_ENTRY_3))

    best_entry = diary.find_best_diary_for_time(100, 3)

    assert best_entry == entry_2

def test_todo_init():
    todo_list = TodoList()
    assert len(todo_list.incomplete()) == 0
    assert len(todo_list.complete()) == 0

def test_todo_add():
    todo_list = TodoList()

    task_1 = Todo("Write the code for this function!")
    task_2 = Todo("Write the code for all the tests!")

    todo_list.add(task_1)
    todo_list.add(task_2)

    assert todo_list.incomplete() == [task_1, task_2]

def test_todo_complete():
    todo_list = TodoList()

    task = Todo("Todo!")
    todo_list.add(task)

    task.mark_complete()

    assert task in todo_list.completed()

def test_todo_giveup():
    todo_list = TodoList()
    
    task_1 = Todo("Write the code for this function!")
    task_2 = Todo("Write the code for all the tests!")

    todo_list.add(task_1)
    todo_list.add(task_2)

    todo_list.give_up()

    assert len(todo_list.complete()) == 2
    assert len(todo_list.incomplete()) == 0

def test_user_integration():
    diary = Diary()
    todo_list = TodoList()
    user = User(diary, todo_list)

    assert user.diary == diary
    assert user.todo_list == todo_list

    

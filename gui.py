# First GUI version of the todo app.
#
# THIRD-PARTY MODULE: FreeSimpleGUI.
# Unlike `time` or `csv`, this isn't built into Python — you have to
# install it. In PyCharm:
#   Settings/Preferences -> Project -> Python Interpreter -> "+" ->
#   search "FreeSimpleGUI" -> Install Package.
# Or from the terminal:   pip install FreeSimpleGUI
#
# The lecture also covers RENAMING:
#   - Rename the previous `todos.txt` (the CLI version) to `cli.py`.
#     Convention: when a project has multiple frontends, use named
#     files (`cli.py`, `gui.py`) instead of `todos.txt`.
#   - Import `FreeSimpleGUI as sg` so we can use the short prefix.
#
# Widgets ("elements") used here:
#   sg.Text(text)              - a label
#   sg.InputText(tooltip=...)  - a single-line text input
#   sg.Button(text)            - a clickable button
#   sg.Window(title, layout)   - the container; layout is a list of rows
#
# LAYOUT IS A LIST OF LISTS. Each INNER list is one ROW. The widgets
# inside that inner list sit next to each other left-to-right.

import FreeSimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label, input_box, add_button]],
                   font=("Helvetica", 20))

window.read()
window.close()

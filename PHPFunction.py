'''
This script aims to work out the current PHP function that you're in.
'''

# import sublime
import sublime_plugin
import os


class PhpFunctionEventListener(sublime_plugin.EventListener):
    """Event listener for the plugin"""
    def on_selection_modified(self, view):
        if not self.should_execute(view):
            return

        function = self.get_function(view)
        if function:
            ffile = open('/Users/mgadd/Sites/dev/drarok/docs/web/function.txt', 'w')
            ffile.write(function)
            ffile.close()
            del ffile

    def should_execute(self, view):
        if view.file_name() != None:
            ext = os.path.splitext(view.file_name())[1]
            return ext[1:] == 'php'

        return False

    def get_function(self, view):
        """Get the current function, based on cursor position in the current line."""
        sel = view.sel()[0]
        line = view.line(sel)
        offset = sel.begin() - line.begin()

        # Get the text up to the cursor position.
        text = view.substr(line)[0:offset]

        level = 1
        for x in range(len(text) - 1, 0, -1):
            char = text[x]

            if char == ')':
                level += 1
                continue

            if char == '(':
                level -= 1

            if level == 0:
                chunk = text[0:x]

                start = 0
                for search in ['(', ' ']:
                    pos = chunk.rfind(search)
                    if pos > -1 and pos >= start:
                        start = pos + 1

                # TODO: Strip '!', etc, using a regex.
                return chunk[start:].strip(' !')

        return False

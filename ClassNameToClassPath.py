import sublime
import sublime_plugin


class ClassNameToClassPathCommand(sublime_plugin.TextCommand):
    """
    Convert a class name (Company_Model_Product_Type_Item) into a path (Company/Model/Product/Type/Item).

    Put this in your sublime-keymap file:
    // Map ctrl + shift + c to replace underscores with slashes.
    {"keys": ["ctrl+shift+c"], "command": "class_name_to_class_path"},
    """

    def run(self, edit):
        # Loop over each selection.
        for sel in self.view.sel():
            # Grab the existing text.
            text = self.view.substr(sel)

            # Process the text here.
            text = text.replace('_', '/')

            # Now replace the selection with our processed text.
            self.view.replace(edit, sel, text)

import sublime
import sublime_plugin


class SingleQuotesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Loop over each selection.
        for sel in self.view.sel():
            # Grab the existing text.
            text = self.view.substr(sel)

            # Process the text here.
            text = text.replace('"', '\'')

            # Now replace the selection with our processed text.
            self.view.replace(edit, sel, text)

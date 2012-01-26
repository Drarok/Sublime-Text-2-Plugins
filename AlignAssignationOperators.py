import sublime
import sublime_plugin


class AlignAssignationOperatorsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Loop over each selection.
        for sel in self.view.sel():
            # Grab the text from the current selection.
            text = self.view.substr(self.view.line(sel))
            replacementText = ''

            # First loop detects the spacing required.
            operatorPositions = {}
            maxOperatorPosition = 0

            for idx, line in enumerate(text.splitlines(True)):
                # Find the operator.
                currentOperatorPos = line.find('=')

                # Store its location for later.
                operatorPositions[idx] = currentOperatorPos

                # Have we found a new max?
                if currentOperatorPos > 0 and currentOperatorPos > maxOperatorPosition:
                    maxOperatorPosition = currentOperatorPos

                    # If there's no space before the operator, increase the max pos.
                    if line[currentOperatorPos - 1] != ' ':
                        maxOperatorPosition += 1

            # Loop over each line, inserting spaces as required.
            for idx, line in enumerate(text.splitlines(True)):
                currentOperatorPos = operatorPositions[idx]

                if currentOperatorPos == -1:
                    # No operator? Just leave the text as-is.
                    replacementText += line
                else:
                    # Process the text and insert the required number of spaces.
                    prefix = line[0:currentOperatorPos - 1].rstrip()
                    suffix = line[currentOperatorPos:].lstrip()
                    spaces = ' ' * (maxOperatorPosition - len(prefix))

                    # Make sure there's a space after the operator.
                    if suffix[0:2] == '=>':
                        if suffix[0:3] != '=> ':
                            suffix = '=> ' + suffix[2:]
                    elif suffix[0:2] != '= ':
                        suffix = '= ' + suffix[1:]

                    replacementText += prefix + spaces + suffix

            self.view.replace(edit, sel, replacementText)

"""
Test Data:
$var1 = 'proper';
$var2= 'missing pre-space';
$another ='missing post-space';
$thelongestone='no spaces';

$arr = array(
    'key1' =>'missing post-space',
    'key1'=> 'missing pre-space',
    'key2'=>'no spaces',
    'longerkey' => 'proper spaces',
);
"""
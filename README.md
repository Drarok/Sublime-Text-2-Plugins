# What's this?

This is simply a repository where I'm keeping my personal Sublime Text 2 plugins.

If you find any of them useful, feel free to copy, distribute, and improve on them. I only ask that you send me a pull request for anything useful you may add, or fix.

## Align Assignation Operators

This plugin adds an 'align\_assignation\_operators' command, which attempts to add spaces where required in order to make multi-line assignation blocks line up at the '=' sign.

Given this:
<pre>
	$var = array(
		'key1' => 'value',
		'anotherKey' => 'another value',
		'aVeryLongKey'=>'without spaces',
	);
</pre>

Running the plugin with the three lines inside the array selected will result in this:
<pre>
	$var = array(
		'key1'         => 'value',
		'anotherKey'   => 'another value',
		'aVeryLongKey  => 'without spaces',
	);
</pre>

## (Convert to) Single Quotes

Adds a 'single\_quotes' command which simply replaces occurrences of double-quotes with single quotes.

Before:
<pre>
	$var1 = $_POST["someVar"];
	$var2 = $_POST["anotherVar"];

	echo "This is a fixed string", PHP_EOL;
</pre>

After:
<pre>
	$var1 = $_POST['someVar'];
	$var2 = $_POST['anotherVar'];

	echo 'This is a fixed string', PHP_EOL;
</pre>

## Class Name to Class Path

This plugin adds a 'class_name_to_class_path' command, which replaces underscores and backslashes in the selected text with slashes, allowing you to paste a class name into the fuzzy file search, select the text, and turn it into a class path.

You'll need to assign it to a keyboard shortcut for it to be useful. I use Ctrl+Shift+C.
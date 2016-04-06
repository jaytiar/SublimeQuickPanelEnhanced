# Quick Panel Enhanced
This is a Sublime Text 3 plugin that provides improvements to the operation of the Quick (Overlay) Panel.

The Quick Panel is the pop-up that appears for things like Find Anything (Ctrl+P) and the Command Palette (Ctrl+Shift+P).

It provides fuzzy-match searching of the items in the list (be they files or symbols).

However, if the list is long (for example, if you have a very large codebase), there are couple of limitations:
  * Deleting text from the fuzzy-search input string can be slow as the list is regnerated after every key press.
  * Page Up and Page Down do not work, so you have to scroll one line at a time if using the keyboard.

This plugin addresses both of these limitations:
  * Deletion in the panel entry box is buffered, so characters are not removed until the user stops pressing backspace, meaning the list is only regenerated once.
  * Page Up/Down work as expected, scrolling several lines at once.

## Configuration
There are no separate settings - the function becomes automatically available once the plugin is installed.

The number of lines scrolled by page up/down and the delay before deletion takes effect can be controlled by adding paramaters to the key bindings.
See the Default key bindings for details.

## Installation
Search for QuickPanelEnhanced via Package Control in the usual way.

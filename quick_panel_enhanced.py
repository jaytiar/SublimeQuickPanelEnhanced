import sublime
import sublime_plugin
import functools

overlay_index = -1


class QuickPanelDeleteCommand(sublime_plugin.WindowCommand):
    """Buffer up leftwards deletions and apply after a timeout"""
    count = 0

    def run(self, delay=200):
        global overlay_index
        if overlay_index != -1:
            # Active view is the overlay panel - apply hysteresis.
            self.window.run_command("move",
                                    {"by": "characters",
                                     "forward": False,
                                     "extend": True})
            self.count += 1

            # Use synchronous timeout to avoid any window conditions.
            sublime.set_timeout(functools.partial(self.do_delete, self.count),
                                delay)
        else:
            # Active view is not the overlay panel - do the normal delete.
            self.window.run_command("left_delete")

    def do_delete(self, old_count):
        if self.count == old_count:
            # Count hasn't changed, so user has stopped typing - delete
            self.window.run_command("right_delete")
            self.count = 0


class QuickPanelPageUpCommand(sublime_plugin.WindowCommand):
    """Simulate page-up by repeating up command multiple times"""
    def run(self, count=8):
        # Only do something special if overlay has focus.
        global overlay_index
        if overlay_index == -1:
            self.window.run_command("move", {"by": "pages", "forward": False})
        else:
            for i in range(count):
                self.window.run_command("move",
                                        {"by": "lines", "forward": False})


class QuickPanelPageDownCommand(sublime_plugin.WindowCommand):
    """Simulate page-down by repeating down command multiple times"""
    def run(self, count=8):
        # Only do something special if overlay has focus.
        global overlay_index
        if overlay_index == -1:
            self.window.run_command("move", {"by": "pages", "forward": True})
        else:
            for i in range(count):
                self.window.run_command("move",
                                        {"by": "lines", "forward": True})


class QuickPanelEvents(sublime_plugin.EventListener):
    """Detect whether the overlay (quick panel) is visible"""
    def on_activated(self, view):
        if view.window():
            # The overlay has a view ID, but doesn't appear in a group.
            # The test below allows us to determine the overlay has focus.
            (grp, idx) = view.window().get_view_index(view)
            global overlay_index
            if grp == -1 and idx == -1:
                overlay_index = view.id()
            else:
                overlay_index = -1

    def on_deactivated(self, view):
        global overlay_index
        overlay_index = -1

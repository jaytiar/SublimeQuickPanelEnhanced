import sublime
import sublime_plugin
import functools


class QuickPanelDeleteCommand(sublime_plugin.WindowCommand):
    """Buffer up leftwards deletions and apply after a timeout"""
    count = 0

    def run(self, delay=200):
        # Active view is the overlay panel - apply hysteresis.
        self.window.run_command("move",
                                {"by": "characters",
                                 "forward": False,
                                 "extend": True})
        self.count += 1

        # Use synchronous timeout to avoid any window conditions.
        sublime.set_timeout(functools.partial(self.do_delete, self.count),
                            delay)

    def do_delete(self, old_count):
        if self.count == old_count:
            # Count hasn't changed, so user has stopped typing - delete
            self.window.run_command("right_delete")
            self.count = 0


class QuickPanelPageUpCommand(sublime_plugin.WindowCommand):
    """Simulate page-up by repeating up command multiple times"""
    def run(self, count=8):
        for i in range(count):
            self.window.run_command("move", {"by": "lines", "forward": False})


class QuickPanelPageDownCommand(sublime_plugin.WindowCommand):
    """Simulate page-down by repeating down command multiple times"""
    def run(self, count=8):
        for i in range(count):
            self.window.run_command("move", {"by": "lines", "forward": True})

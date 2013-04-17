import sublime_plugin


class RenameCurrentFileCommand(sublime_plugin.TextCommand):

    def run(self, edit, *args):
        self.view.window().run_command("rename_path",
            {"paths": [self.view.file_name()]})


class DeleteCurrentFileCommand(sublime_plugin.TextCommand):

    def run(self, edit, *args):
        self.view.window().run_command("delete_file",
            {"files": [self.view.file_name()]})
        # now we need to do something to mark the view as dirty
        self.view.run_command('mark_view_dirty')


class MarkViewDirtyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.insert(edit, self.view.size(), ' ')
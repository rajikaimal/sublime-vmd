import sublime_plugin
import subprocess
import sublime

# vmd settings file
VMD_SETTINGS = 'vmd.sublime-settings'
# get platform
platform = sublime.platform()


class VmdCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        settings = sublime.load_settings(VMD_SETTINGS)
        file_extension = str(settings.get('extensions')[0])
        file_name = view.file_name()
        if platform == 'linux':
        	executable_path = str(settings.get('bin')['linux'])
        	if not executable_path:
        		self.run_vmd(file_name, 'vmd', file_extension)
        	else:
	        	self.run_vmd(file_name, executable_path, file_extension)
        if platform == 'osx':
        	executable_path = str(settings.get('bin')['osx'])
        	if not executable_path:
        		self.run_vmd(file_name, 'vmd', file_extension)
        	else:
	        	self.run_vmd(file_name, executable_path, file_extension)
        if platform == 'windows':
        	executable_path = str(settings.get('bin')['windows'])
        	if not executable_path:
        		self.run_vmd(file_name, 'vmd', file_extension)
        	else:
	        	self.run_vmd(file_name, executable_path, file_extension)
	        	
    # run vmd shell command
    def run_vmd(self, file_name, executable_path, extension):
        if file_name is None:
            self.show_error('Error opening vmd !!!')
        if file_name.endswith('.' + extension):
        	process = subprocess.Popen(executable_path + ' ' + file_name, shell=True)
	        out, error = process.communicate()
	        if error:
	            self.show_error(error)
        else:
            self.show_error('Please open a markdown file (.md)')

    # show error message
    def show_error(self, error):
        sublime.error_message(error)

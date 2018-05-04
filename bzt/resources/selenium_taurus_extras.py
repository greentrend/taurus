from string import Template
from selenium.common.exceptions import NoSuchWindowException

class Apply(Template):
    
    def __init__(self, template):
        super(Apply, self).__init__(template)
        self.variables = {}
    
    def __repr__(self):
        return repr(self.safe_substitute(self.variables))

    def __str__(self):
        return self.safe_substitute(self.variables)
    
class Template():

    def __init__(self, variables=None):
        if dict:
            self.variables = variables
        else:
            self.variables = {}
        self.tmpl = Apply("")
    
    def apply(self, template):
        self.tmpl.template = template
        self.tmpl.variables = self.variables
        return str(self.tmpl)
        
class WindowManager():

    def __init__(self, driver):
        self.driver = driver
        self.windows = {}
        
    def switch(self, window_name):
        if window_name.isdigit():
            wnd_handlers = self.driver.window_handles
            if len(wnd_handlers) <= int(window_name) and int(window_name) >=0:
                self.driver.switch_to.window(wnd_handlers[int(window_name)])
            else:
                raise NoSuchWindowException("Invalid Window ID: %s" % window_name)
        else:
            if window_name.startswith("win_ser_"):
                if window_name == "win_ser_local":
                    wnd_handlers = self.driver.window_handles
                    if len(wnd_handlers) > 0:
                        self.driver.switch_to.window(wnd_handlers[0])
                    else:
                        raise NoSuchWindowException("Invalid Window ID: %s" % window_name)
                else:
                    if window_name not in self.windows:
                        self.windows[window_name] = self.driver.window_handles[-1]
                        self.driver.switch_to.window(self.windows[window_name])
                    else:
                        self.driver.switch_to.window(self.windows[window_name])
            else:
                self.driver.switch_to.window(window_name)
            
    def close(self, window_name):
        self.switch(window_name)
        self.driver.close()

    
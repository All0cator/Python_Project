
from ui.window import Window
from ui.console import Console

class Renderer:
    
    RENDERER_INSTANCES = 0
    MODE_CONSOLE = 0
    MODE_WINDOW = 1
        
    RENDER_MODES = {MODE_CONSOLE, MODE_WINDOW}
    
    def __init__(self, renderMode=MODE_CONSOLE):
        
        if(Renderer.RENDERER_INSTANCES == 1):
            assert(False and "Error: Already have a Renderer cannot create second")
        
        if(not renderMode in Renderer.RENDER_MODES):
            assert(False and "Error: Wrong renderMode given to Renderer object")
        
        self.renderMode = renderMode
        RENDERER_INSTANCES += 1
        
        if(renderMode == Renderer.MODE_CONSOLE):
            # Create a console
            self.surface = Console()
        else:
            # Create a window
            self.surface = Window()
    
    def __del__(self):
        Renderer.RENDERER_INSTANCES -= 1        
    
    def PrintMenu(self, descriptionText, menuOptions, startSeparator=False, endSeparator=False, isNumbered=False):
        """
        descriptionText (str)
        menuOptions (list)
        isNumbered (bool) 
        """
        
        self.surface.
        
        return
    
    def PrintCalendar(self):
        return
    
    def PrintEvent(self):
        return
    
    def Input(self):
        return
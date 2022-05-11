init -1500 python:

    class MouseTooltip(Tooltip, renpy.Displayable):
        """
        A Tooltip whose x/y position follows the mouse's.
        """
        action = Action
        
        def __init__(self, default, padding=None, *args, **kwargs):
            super(renpy.Displayable, self).__init__(*args, **kwargs)
            
            self.default = default
            self.value = default
            
            self.padding = padding or {}
            self.pad_x = padding.get('x', 0)
            self.pad_y = padding.get('y', 0)
            
            self.x = 0
            self.y = 0
        
        def render(self, width, height, st, at):
            
            try:
                w, h = self.value.size()
            
            except AttributeError:
                child_render = renpy.render(self.value, width, height, st, at)
                w, h = child_render.get_size()
            
            render = renpy.Render(w, h)
            render.place(self.value, x=self.x + self.pad_x, y=self.y + self.pad_y)
            return render
        
        def event(self, ev, x, y, st):
            self.x = x
            self.y = y
            renpy.redraw(self, 0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

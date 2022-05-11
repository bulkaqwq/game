
init 1 python:

    class Item:
        hover_image = None
        selected = False
        def __init__(self, name,image_name):
            self.name = name
            self.image_name = image_name
            self.hover_image = im.Composite((105, 105),
                                        (0, 0), "yellow.png",
                                        (0, 0), image_name)
            self.selected_image = im.Composite((105, 105),
                                        (0, 0), "red.png",
                                        (0, 0), image_name)
        def __eq__(self, other):
            return self.name == other.name

    class addItem(Action):
        
        def __init__(self, item):
            self.item = item
        
        def __call__(self):
            store.inventory.append(self.item)
            renpy.restart_interaction()

    class selectItem(Action):
        
        def __init__(self, object):
            self.object = object
        
        def __call__(self):
            new_value = not self.object.selected
            for item in store.inventory:
                setattr(item, "selected", False)
            store.active_item = None
            setattr(self.object, "selected", new_value)
            if (new_value):
                renpy.play("music/Click To Start.ogg", channel="investigation_SE")
                store.active_item = self.object
            else:
                renpy.play("music/ExitClickSound.ogg", channel="investigation_SE")
            renpy.restart_interaction()
        
        def get_selected(self):
            return self.object.selected

init python:
    def inventory_dragged(drags, drop):
        
        if not drop:
            return
        
        return True

    class checkInteractionValid(Action):
        
        def __init__(self, screenName, normalInteraction):
            self.screenName = screenName
            self.normalInteraction = normalInteraction
        
        def __call__(self):
            if store.active_item != None:
                renpy.call("investigation_object_not_working", self.screenName)
            else:
                renpy.jump(self.normalInteraction)

    class checkInteractionValid0(Action):
        
        def __init__(self, screenName, normalInteraction):
            self.screenName = screenName
            self.normalInteraction = normalInteraction
        
        def __call__(self):
            if store.active_item != None:
                renpy.call("investigation_object_not_working0", self.screenName)
            else:
                renpy.jump(self.normalInteraction)

    class testItem_General(Action):
        
        def __init__(self, item, switch, value, screenName, labelWork, labelNoItem, remove = True):
            self.item = item
            self.switch = switch
            self.value = value
            self.remove = remove
            self.screenName = screenName
            self.labelWork = labelWork
            self.labelNoItem = labelNoItem
        
        def __call__(self):
            if store.active_item != None:
                if store.active_item == self.item:
                    setattr(store, self.switch, self.value)
                    if self.remove:
                        store.inventory.remove(self.item)
                        store.active_item = None
                    renpy.jump(self.labelWork)
                else:
                    
                    renpy.call("investigation_object_not_working", self.screenName)
            else:
                renpy.jump(self.labelNoItem)
            renpy.restart_interaction()

    class testItem_General0(Action):
        
        def __init__(self, item, switch, value, screenName, labelWork, labelNoItem, remove = True):
            self.item = item
            self.switch = switch
            self.value = value
            self.remove = remove
            self.screenName = screenName
            self.labelWork = labelWork
            self.labelNoItem = labelNoItem
        
        def __call__(self):
            if store.active_item != None:
                if store.active_item == self.item:
                    setattr(store, self.switch, self.value)
                    if self.remove:
                        store.inventory.remove(self.item)
                        store.active_item = None
                    renpy.jump(self.labelWork)
                else:
                    renpy.call("investigation_object_not_working0", self.screenName)
            else:
                renpy.jump(self.labelNoItem)
            renpy.restart_interaction()

screen inventory_screen:
    zorder 100
    frame:
        has grid 1 4:

            spacing 5
            xpos 0
            ypos 0

        for index, item in enumerate(inventory):
            imagebutton:
                idle item.image_name
                hover item.hover_image
                selected_idle item.selected_image

                action selectItem(item)

        for i in range(4 - len(inventory)):
            add "images/myers-click/empty.png"

screen displayTextScreenGeneral:
    tag bedroom_choice_1_tag
    default displayText = ""
    default xalign_value = 0.5
    default yalign_value = 0.5
    vbox:
        xalign xalign_value
        yalign yalign_value
        frame:
            text displayText

label investigation_object_not_working(screenName):


    $ investigation_object_not_working_screen_name = screenName
    $ renpy.pop_call()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    van "I can't use the item here."


    $ renpy.call_screen(investigation_object_not_working_screen_name)

label investigation_object_not_working0(screenName):


    $ investigation_object_not_working_screen_name = screenName
    $ renpy.pop_call()

    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    play sound "music/selectsounds.ogg"

    v "I can't use the item here."

    $ renpy.call_screen(investigation_object_not_working_screen_name)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

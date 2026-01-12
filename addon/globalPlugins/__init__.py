# -*- coding: UTF-8 -*-
# Window State Announcer Global Plugin

import globalPluginHandler
import api
import ui
import ctypes
import logHandler
from scriptHandler import script
from ctypes import wintypes

# Windows API Constants
GA_ROOT = 2

# Setup User32
user32 = ctypes.windll.user32
user32.GetAncestor.argtypes = [wintypes.HWND, wintypes.UINT]
user32.GetAncestor.restype = wintypes.HWND
user32.IsZoomed.argtypes = [wintypes.HWND]
user32.IsZoomed.restype = wintypes.BOOL
user32.IsIconic.argtypes = [wintypes.HWND]
user32.IsIconic.restype = wintypes.BOOL

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    # Translators: The category name in Input Gestures dialog.
    scriptCategory = _("Window State Announcer")

    def __init__(self):
        super().__init__()
        # LOGGING: Confirm the plugin has loaded
        logHandler.log.info("WindowStateAnnouncer: Plugin Loaded Successfully")

    @script(
        # Translators: Description of the command.
        description=_("Announces whether the active window is minimized, maximized, or normal."),
        gesture="kb:NVDA+control+shift+s",
        speakOnDemand=True
    )
    def script_announceWindowState(self, gesture):
        # LOGGING: Confirm the gesture was received
        logHandler.log.debug("WindowStateAnnouncer: Script triggered by gesture")

        obj = api.getForegroundObject()
        
        if not obj or not getattr(obj, "windowHandle", None):
            ui.message(_("No window detected"))
            logHandler.log.debug("WindowStateAnnouncer: No foreground object or handle found.")
            return

        hwnd = obj.windowHandle
        root_hwnd = user32.GetAncestor(hwnd, GA_ROOT)
        target_hwnd = root_hwnd if root_hwnd else hwnd

        if user32.IsZoomed(target_hwnd):
            ui.message(_("Window is maximized"))
        elif user32.IsIconic(target_hwnd):
            ui.message(_("Window is minimized"))
        else:
            ui.message(_("Window is normal"))

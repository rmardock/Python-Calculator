## reconnect function from https://stackoverflow.com/questions/21586643/pyqt-widget-connect-and-disconnect

# Class for interface connection functions
class ConnectionTools(object):
    # Function to swap connections from UI elements and event-driven functions
    def reconnect(signal, new_handler=None, old_handler=None):
        try: 
            if old_handler is not None:
                while True:
                    signal.disconnect(old_handler)
            else:
                signal.disconnect()
        except TypeError:
            pass
        
        if new_handler is not None:
            signal.connect(new_handler)

class SignalUtility():
    # Function to enable buttons
    def enable_button(button):
        button.setEnabled(True)
    
    # Function to disable buttons
    def disable_button(button):
        button.setEnabled(False)
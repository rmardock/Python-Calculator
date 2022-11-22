## https://stackoverflow.com/questions/21586643/pyqt-widget-connect-and-disconnect

# Class for interface connection functions
class connection_tools(object):
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

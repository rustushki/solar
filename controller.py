import gtk
import math

from canvas import Canvas

class Controller(object):

    def __init__(self):
        """ Entry point to a simple Solar System simulator. 
        
        Build the Gtk Window--making it closeable--and populate it with a
        Canvas.  Hook the Canvas up to the function drawSolarSystem which does
        as it is named.
        """

        # Build a Gtk Window, center it, and add a Canvas to it.
        window = gtk.Window()
        window.set_position(gtk.WIN_POS_CENTER)
        canvas = Canvas(drawSolarSystem)
        window.add(canvas)

        # Hook "Window Close" to close() method
        window.connect("delete-event", gtk.main_quit)

        # Display the Window
        window.show_all()

        gtk.main()


def drawSolarSystem(context):
    """ Draw the Solar System Model
    
    Args:
        context - Cairo context
    """

    context.translate (0.1, 0.1) # Changing the current transformation matrix

    context.arc (0.1, 0.1, 0.1, 0, 2 * math.pi)
    context.close_path ()

    context.set_source_rgb (0.3, 0.2, 0.5) # Solid color
    context.set_line_width (0.01)
    context.stroke_preserve()

    context.set_source_rgb(1.0, 1.0, 0.0)
    context.fill()

Controller()

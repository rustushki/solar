import cairo
import gtk

class Canvas(gtk.DrawingArea):
    def __init__(self, drawingInstructions):
        """ Build a Canvas, stretching it to 800x600 and connecting the expose
        event to the provided drawingInstructions method. 

        Args:
            drawingInstructions - drawing instructions for the Canvas
        """
        
        super(Canvas, self).__init__()

        # Hook expose_event to the onExposure() method
        self.connect("expose_event", self.onExposure)

        # Size the Window to 800 x 600
        self.set_size_request(800, 600)

        self.drawingInstructions = drawingInstructions

    def onExposure(self, widget, event):
        """ React to screen exposure. """

        # Get the Rectangle of this DrawingArea.
        rect = self.get_allocation()

        # Build and Normalize a Cairo Context.
        context = widget.window.cairo_create()
        context.scale (rect.width, rect.width)

        # Delegate drawing to the provided drawingInstructions.
        self.drawingInstructions(context)

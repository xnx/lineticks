# lineticks

`LineTicks` is a simple class to add ticks to a Matplotlib line. The tick marks stick out perpendicular to the plotted line and move around when the plot is dragged, resized or its limits are changed.

It's a bit simple and requires the indexes of the data points on which to add tick marks. Labels should be given as a sequence of strings of the same length as the index list.

To use it, create a `LineTicks` instance, passing the Matplotlib `Line2D` object to be ticked, a sequence of indexes, `idx`, into the underlying data array for the points to add tick marks to, and a length (in display units), `tick_length`, for the tick marks themselves. The argument `direction` may be 1 or -1 for ticks oriented +90° or -90° from the line. To add tick labels, pass a sequence of strings, the same length as `idx` to `label`.

Some example applications are given in this repository.



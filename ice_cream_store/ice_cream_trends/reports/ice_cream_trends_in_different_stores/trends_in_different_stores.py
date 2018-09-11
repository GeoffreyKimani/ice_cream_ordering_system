from flask import Blueprint, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from io import BytesIO
import numpy as np

trends_in_different_stores_bp = Blueprint('trends_in_different_stores_bp', __name__,
                                          static_folder='static', template_folder='templates')


@trends_in_different_stores_bp.route('/ice_cream_trends_in_different_stores')
def trends_in_different_stores():
    # the data used here is generated from the store sales generator,
    # it may vary with every run of the script generating this data

    store_number = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE']
    store_sales = [11523, 10729, 10791, 10248, 11453]

    fig = Figure()
    ax = fig.add_subplot(111)

    ax.set_title('ICE CREAM TRENDS IN FIVE STORES IN YEAR 2010')
    ax.set_xlabel('STORE NUMBER')
    ax.set_ylabel('NUMBER OF ICE CREAMS SOLD')

    x_pos = np.arange(len(store_number))
    ax.set_xticks(x_pos)
    ax.set_xticklabels(store_number)

    # function to put labels on each of the graphs
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.0 * height,
                    '%d' % int(height), ha='center', va='bottom')

    autolabel(ax.bar(x_pos, store_sales))
    ax.legend()

    # render image to web page
    canvas = FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

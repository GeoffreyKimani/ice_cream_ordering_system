from flask import Blueprint, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from io import BytesIO
import numpy as np

trends_in_regions_bp = Blueprint('trends_in_regions_bp', __name__,
                                 static_folder='static', template_folder='templates')


@trends_in_regions_bp.route('/ice_cream_trends_in_regions')
def trends_in_regions():
    # the data used here is generated from the region sales generator,
    # it may vary with every run of the script generating this data

    region_number = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE']
    region_sales = [47673, 56560, 56503, 51680, 52543]

    fig = Figure()
    ax = fig.add_subplot(111)

    ax.set_title('ICE CREAM TRENDS IN FIVE REGIONS IN YEAR 2010')
    ax.set_xlabel('REGION NUMBER')
    ax.set_ylabel('NUMBER OF ICE CREAMS SOLD')

    x_pos = np.arange(len(region_number))
    ax.set_xticks(x_pos)
    ax.set_xticklabels(region_number)

    # function to put labels on each of the graphs
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.0 * height,
                    '%d' % int(height), ha='center', va='bottom')

    autolabel(ax.bar(x_pos, region_sales))
    ax.legend()

    # render image to web page
    canvas = FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response




from flask import Blueprint, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from io import BytesIO
import numpy as np

ice_cream_sales_bp = Blueprint('ice_cream_sales_bp', __name__,
                               static_folder='static', template_folder='templates')


@ice_cream_sales_bp.route('/ice-cream-sales-2010-2012')
def ice_cream_sales():
    # the data used here is generated from the weekly sales generator,
    # it may vary with every run of the script generating this data

    years = ['2010', '2011', '2012']
    year_sales = [10981, 10533, 12031]

    fig = Figure()
    ax = fig.add_subplot(111)

    ax.set_title('ICE CREAM SALES FOR YEAR 2010 - 2012')
    ax.set_xlabel('YEAR')
    ax.set_ylabel('NUMBER OF ICE CREAMS SOLD')

    x_pos = np.arange(len(years))
    ax.set_xticks(x_pos)
    ax.set_xticklabels(years)

    # function to put labels on each of the graphs
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.0 * height,
                    '%d' % int(height), ha='center', va='bottom')

    autolabel(ax.bar(x_pos, year_sales, label='ICE CREAM SALES FOR ONE STORE'))
    ax.legend()

    # render image to web page
    canvas = FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

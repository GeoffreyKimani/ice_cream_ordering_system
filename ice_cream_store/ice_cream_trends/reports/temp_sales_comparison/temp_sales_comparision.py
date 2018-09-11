"""here we will compare how temperature affects the sale of ice cream in a store.
    i have divided the temperature into 4 bands;
        0 - 15, 16 -23, 24 - 29, 30 - 35.
    In each band we will sample 2 sales data

    the data used here is from temperature sales generator file.
"""

from flask import Blueprint, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from io import BytesIO
import numpy as np


temp_sales_comparision_bp = Blueprint('temp_sales_comparision_bp', __name__,
                                      static_folder='static', template_folder='templates')


@temp_sales_comparision_bp.route('/temp_sales_comparision')
def temp_sales_comparision():
    temp_range = ['0-7', '8-15', '16-19', '20-23', '24-27', '28-30', '31-33', '34-35']
    temp_sales = [2, 10, 17, 20, 34, 40, 63, 68]

    fig = Figure()
    ax = fig.add_subplot(111)

    ax.set_title('ICE CREAM SALES AGAINST TEMPERATURE IN A STORE')
    ax.set_xlabel('TEMP RANGE')
    ax.set_ylabel('NUMBER OF ICE CREAMS SOLD')

    x_pos = np.arange(len(temp_range))
    ax.set_xticks(x_pos)
    ax.set_xticklabels(temp_range)

    # function to put labels on each of the graphs
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.0 * height,
                    '%d' % int(height), ha='center', va='bottom')

    autolabel(ax.bar(x_pos, temp_sales))
    ax.legend()

    # render image to web page
    canvas = FigureCanvas(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

import datetime
import os


class TexFig:

    '''
    Keeping the TexFig as a seperate class to allow for easier updating in the future
    figure: matplotlib figure
    title: figure title
    caption: figure caption
    figure_filename: name of figure can be generated automatically
    '''


    def __init__(self, figure, title, caption, figure_filename=None, output_type = '.pdf'):

        self.figure = figure
        self.title = title
        self.caption = caption
        self.figure_path = None
        if figure_filename is None:
            self.figure_filename = title.lower().replace(' ','_')

        date_now = datetime.datetime.now()
        date_id = date_now.strftime("%Y%m%d") 
        figure_filename = '_'.join([date_id,self.figure_filename]) + output_type
        self.figure_filename = figure_filename

    def add_plot_path(self, plot_path):
        self.figure_path = os.path.join(plot_path,self.figure_filename)

    def figtotex(self):

        if self.figure_path == None:
            raise Exception('Must run add_plot_path method first!')


        figpath = '/'.join(self.figure_path.split('/')[-2:])
        print(figpath)

        tex_out = f'\\afterpage{{\\clearpage\n\\begin{{figure}}[H]\n\t\\centering\n\t\\includegraphics{{{figpath}}}\n\t\\caption[{self.title}]{{\\textbf{{{self.title}}} {self.caption}}}\n\\end{{figure}}}}'
        return tex_out
import os
import shutil
import importlib
import matplotlib.pyplot as plt

class FigToTex:

    '''
    Class to dump figures to latex file. We will make a simple .tex file which can be loaded into a larger document. This prevents issues with such as tags and specialized preambles.
    
    For now all figures will be saved as an svg.

    folder structure
    main.tex
    plots/plot_type/fig.svg
    inputs/plot_type/fig.tex
    '''

    def __init__(self, plot_type:str, figures:list, outpath:str):

        self.figures = figures
        self.outpath = outpath
        self.plot_type = plot_type

        self.setup_dir()
        self.plot_to_tex()
        self.update_maintex()
        
    def setup_dir(self):

        self.plot_path = os.path.join(self.outpath,'plots')
        self.input_path = os.path.join(self.outpath,'inputs')
        self.tex_path = os.path.join(self.input_path, f'{self.plot_type}.tex')
        self.main_tex_path = os.path.join(self.outpath,'main.tex')

        os.makedirs(self.plot_path, exist_ok = True)
        os.makedirs(self.input_path, exist_ok = True)

        if not os.path.exists(self.main_tex_path):
            template_path = os.path.join(importlib.resources.files(__name__).parent.parent,'doc/template.tex')
            shutil.copy(template_path, self.main_tex_path)
        
        for f in self.figures:
            f.add_plot_path(self.plot_path)

    def plot_to_tex(self):

        with open(self.tex_path, 'w+') as f:
            for fig in self.figures:
                f.write(fig.figtotex())
        
                if os.path.exists(fig.figure_path):
                    raise Exception(f'{fig.figure_path} already exists! Please rename')
                else:
                    fig.figure.savefig(fig.figure_path)

    def update_maintex(self):
        
        tmp_tex = self.main_tex_path.replace('.tex','tmp.tex')
        input_path = '/'.join(self.tex_path.split('/')[-2:])

        with open(tmp_tex, 'w') as tmptex:
            with open(self.main_tex_path, 'r') as maintex:
                for l in maintex:
                    if not '\\end{document}' in l:
                        tmptex.write(l)
                    else:
                        tmptex.write(f'\\input{{{input_path}}}\n\n\\end{{document}}')
            
        os.remove(self.main_tex_path)
        os.rename(tmp_tex, self.main_tex_path)
            
        

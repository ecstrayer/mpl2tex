# mpl2tex
## Description 

This repository converts matplotlib plots to a latex document. Enabling the annotation of figures in an organized manner. It is not meant to generate beautiful figures, but rather keep one's plots a bit more organized.

## Install

`pip install mpl2tex`

## Components 

Currently the package is composed of three different classes. 

1. TextoFig - Helper classe the manages latex files as well as directory organization.
2. TexFig - A class which handles generating latex syntax and saving matplotlib figures in the right directory.
3. MPTexFig - A class which creates a multiple panel figure from a list of TexFig. 

### mpl2tex.TexFig() ###

Class to generate a single panel figure.

- `figure:` Takes an `mpl.Figure`
- `caption:` Longer description of data presented in figure.
- `title:` Short title used for table of contents.
- `figure_filename` Default file name is lower case title.
- `subfigure:` Boolean - default is False. 
- `output_type:` File suffix - defual is `.pdf`
- `figure_size:` Float relative to `\textwidth`

```
mpl2tex.TexFig(figure, caption, title, subfigure)
```

### mpl2tex.MPTexFig() ###

Class to generate a multipanel figure.

- `figures:` List of `mpl2tex.TexFig`
- `title:` Short title used for table of contents.
- `caption:` Longer description of data presented in figure.

```
mpl2tex.MPTexFig(Figures = figures, caption, title)
```

### mpl2tex.figtotex() ### 

Function that generates and runs the methods of MPTexFig. To add figure to LaTex document.

`plot_type:` Name for type of plots (e.g. experimentA_replicate_correlations)
`figures:` List of `TexFig` or `MPTexFig`
`outpath:` Path to output directory

```
mpl2tex.figtotex(plot_type, figures, outpath)
```

## Organization of output directory 

```
output\
    inputs\plot_type.tex
    plots\plot_type\plot.pdf
    main.tex 
```
- Plots are labeled with the date. The package will not overwrite existing plots.

## Log

This package uses git to keep track of changes to the document. `mpl2tex.MPTexFig()` class contains several methods related to git.

- `MPTexFig.log():` Runs `git add .` and `git commit -m message` on output directory. Message default is `Added {number_of_newfigures} figures of plot type {plot_type}.`
- `MPTexFig.show_git_log():` Runs `git log` on output directory.
- `MPTexFig.undo:` Runs `git reset --hard HEAD~1` on output directory.



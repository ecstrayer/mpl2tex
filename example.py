import matplotlib.pyplot as plt
import pytotex.texfig
import pytotex.figtotex



###########################
#starting a new tex file


fig1,ax1 = plt.subplots(1, figsize=(4,4))
ax1.plot([0,1],[0,1])

fig2,ax2 = plt.subplots(1, figsize=(4,4))
ax2.plot([20,0],[0,20])

outpath = 'output/'

figure_title1 = 'Really cool figure'
figure_caption1 = 'This is an important figure showing a line'

figure_title2 = 'Another really cool figure'
figure_caption2 = 'This is another important figure showing a line'
plot_type = 'cool_analysis'


tfig = [pytotex.texfig.TexFig(figure=fig1,caption = figure_caption1, title = figure_title1),
        pytotex.texfig.TexFig(figure=fig2,caption = figure_caption2, title = figure_title2)]
totex = pytotex.figtotex.FigToTex(plot_type=plot_type,figures = tfig, outpath='output/')

#updating an existing doc with same analysis

fig3,ax3 = plt.subplots(1, figsize=(4,4))
ax3.plot([12,0],[0,200])

figure_title3 = 'A third cool figure'
figure_caption3 = 'This is a third important figure showing a line'
plot_type = 'cool_analysis'


tfig = [pytotex.texfig.TexFig(figure=fig3,caption = figure_caption3, title = figure_title3)]
totex = pytotex.figtotex.FigToTex(plot_type=plot_type,figures = tfig, outpath='output/')


#updating an existing doc with new analysis

fig4,ax4 = plt.subplots(1, figsize=(4,4))
ax4.plot([12,0],[12,12])

figure_title4 = 'Really boring figure'
figure_caption4 = 'This is a boring figure'
plot_type = 'boring_analysis'


tfig = [pytotex.texfig.TexFig(figure=fig4,caption = figure_caption4, title = figure_title4)]
totex = pytotex.figtotex.FigToTex(plot_type=plot_type,figures = tfig, outpath='output/')
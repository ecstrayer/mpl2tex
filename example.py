import matplotlib.pyplot as plt
import pytotex.texfig
import pytotex.figtotex



###########################
fig1,ax1 = plt.subplots(1, figsize=(4,4))
ax1.plot([0,1],[0,1])

fig2,ax2 = plt.subplots(1, figsize=(4,4))
ax2.plot([20,0],[0,20])

outpath = 'output/'

figure_title1 = 'Really cool figure'
figure_caption1 = 'This is an important figure showing a line'

figure_title2 = 'Really cool figure 2'
figure_caption2 = 'This is an important figure showing a line 2'
plot_type = 'cool_analysis'




tfig = [pytotex.texfig.TexFig(figure=fig1,caption = figure_caption1, title = figure_title1),
        pytotex.texfig.TexFig(figure=fig2,caption = figure_caption2, title = figure_title2)]
totex = pytotex.figtotex.FigToTex(plot_type=plot_type,figures = tfig, outpath='output/')
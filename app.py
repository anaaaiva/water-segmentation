import gradio as gr
from functions import *

title = "Water Body Segmentation from satellite (aerial) images - PyTorch"
examples = ['examples/example1.png',
            'examples/example2.png',
            'examples/example3.png',
            'examples/example4.png',
            'examples/example5.png']

interface = gr.Interface(fn=predict, inputs=gr.Image(type="numpy").style(height= 256),
            outputs=gr.Image(type="numpy").style(height=256),
            examples=examples, title=title)

interface.launch()
import gradio as gr
from functions import *

title = "Water Body Segmentation from satellite (aerial) images - PyTorch"
examples = ['examples/example1.jpg',
            'examples/example2.jpg',
            'examples/example3.jpg',
            'examples/example4.jpg',
            'examples/example5.jpg']

interface = gr.Interface(fn=predict, inputs=gr.Image(type="numpy").style(height= 256),
            outputs=gr.Image(type="numpy").style(height=256),
            examples=examples, title=title)

interface.launch(share=True)

import gradio as gr
from gradio_simpletext import SimpleText

with gr.Blocks() as demo:
    gr.Markdown(
        "# Gradio 6.9 Custom Components with dynamic children rendering")
    with SimpleText():
        gr.Button()

if __name__ == "__main__":
    demo.launch()

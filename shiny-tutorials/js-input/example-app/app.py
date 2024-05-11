# pyright: basic

from my_component_name import my_component_name

from shiny import App, render, ui

app_ui = ui.page_fluid(
    my_component_name("myComponent"),
    ui.output_text("valueOut"),
)


def server(input, output, session):
    @render.text
    def valueOut():
        return f"Value from input is {input.myComponent()}"


app = App(app_ui, server)

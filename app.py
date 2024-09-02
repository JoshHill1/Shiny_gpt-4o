import shiny
from shiny import App, ui, render

app_ui = ui.page_fluid(
  ui.h2("Hello, World!")
)

def server(input, output, session):
  pass

app = App(app_ui, server)

if __name__ == "__main__":
  app.run()
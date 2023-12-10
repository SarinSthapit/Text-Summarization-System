from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    output_text = anvil.server.call('predict_output', self.input_article.text)
    if output_text:
      self.output.visible = True
      self.output.text = "Abstractive Summary: " + output_text.capitalize()

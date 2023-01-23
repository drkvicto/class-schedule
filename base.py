from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def login_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user()
    
    
    if user:
      self.sign_in.text = user['email']

    else:
      anvil.users.login_with_form()
    Notification('Conectou-se com sucesso!').show()
    self.login.visible = False
    self.cadastro.visible = False

    

  def sign_up_click(self, **event_args):
    """This method is called when the button is clicked"""
    signup = anvil.users.signup_with_form()
    Notification('Cadastro concluído com sucesso!').show()
    self.cadastro.visible = False
    self.login.visible = False

  def primeiro_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def segundo_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def terceiro_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.materias3.client_readable()
  
    
    pass

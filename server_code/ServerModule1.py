import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.email

@anvil.server.callable
def submit(email,password):
  app_tables.data.add_row(email=email, password=password)

@anvil.server.callable
def get_e(x):
      usr = app_tables.data.search(email= x)
      emails = [user['email'] for user in usr]
      return emails

def get_p(x):
      usr = app_tables.data.search(password= x)
      emails = [user['password'] for user in usr]
      return emails


@anvil.server.callable
def action(mail, pwd):
  if mail == get_e(mail) and pwd == get_p(pwd):
      anvil.email.send(to=mail , subject = "Login alert", text = "Your accound has been successfuly logged in. If not done by you please take nessary actions and change your password.")
    
  else:
      anvil.email.send(to=mail , subject = "Login alert", text ="Some one is trying to log into your accound. Please secure your account. If intended by you trying entering correct password.")
    
  
  
  
  
   
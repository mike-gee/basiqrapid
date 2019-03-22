Sessions
=================

Creating a session
#####################

Creating a basiq.io Session::

   import basiqrapid as bq

   API_KEY = "YOUR_API_KEY"

   session = bq.Session(API_KEY)

Capabilities
######################

Detailed object methods and subroutines available `here <https://basiq-rapid.readthedocs.io/en/latest/objects.html#main.Session>`_.

Create a User
**********************
Example Usage::

   usr = session.createUser(email="gavinBelson",mobile="")

Get a User by ID
*********************
Example Usage::

   user_id = "88888888"
   usr = session.getUser(user_id)

Get dict of institutions
***************************
Example Usage::

   inst_dict = session.getInstitutions()
   wbc_ID = inst_dict["Westpac Banking Corporation"]

Get institutions JSON
*************************
Example Usage::

   inst_json = session.getInstitutionsJSON()

Search for an institution code
*********************************
Example Usage::

   results = session.searchInstitutions("Westpac")
   for result in results:
      print(result)

Delete User
***************
Example Usage::

   user_id = "88888888"
   session.deleteUser(user_id)





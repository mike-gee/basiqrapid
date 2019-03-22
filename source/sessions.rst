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

Create a User
**********************
::
   usr = session.createUser(email="gavinBelson",mobile="")

Get a User by ID
*********************
::
   user_id = "88888888"
   usr = session.getUser(user_id)

Get dict of institutions
***************************
::
   inst_dict = session.getInstitutions()
   wbc_ID = inst_dict["Westpac Banking Corporation"]

Get institutions JSON
*************************
::
   inst_json = session.getInstitutionsJSON()

Search for an institution code
*********************************
::
   results = session.searchInstitutions("Westpac")
   for result in results:
      print(result)

Delete User
***************
::
   user_id = "88888888"
   session.deleteUser(user_id)





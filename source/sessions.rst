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
.. code-block:: python
   usr = session.createUser(email="gavinBelson",mobile="")

Get a User by ID
*********************
.. code-block:: python
   user_id = "88888888"
   usr = session.getUser(user_id)

Get dict of institutions
***************************
.. code-block:: python
   inst_dict = session.getInstitutions()
   wbc_ID = inst_dict["Westpac Banking Corporation"]

Get institutions JSON
*************************
.. code-block:: python
   inst_json = session.getInstitutionsJSON()

Search for an institution code
*********************************
.. code-block:: python
   results = session.searchInstitutions("Westpac")
   for result in results:
      print(result)

Delete User
***************
.. code-block:: python
   user_id = "88888888"
   session.deleteUser(user_id)





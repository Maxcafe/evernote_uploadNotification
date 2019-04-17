#coding : utf-8

import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
import os

from evernote.api.client import EvernoteClient

authToken = "S=s1:U=94e42:E=16d361ce84b:C=165de6bbb98:P=1cd:A=en-devtoken:V=2:H=a974d528bac6368c84c5b084ca1588e3"

# Initial development is performed on our sandbox server. To use the production
# service, change sandbox=False and replace your
# developer token above with a token from
# https://www.evernote.com/api/DeveloperToken.action
# To access Sandbox service, set sandbox to True
# To access production (International) service, set both sandbox and china to False
# To access production (China) service, set sandbox to False and china to True

sandbox=True
china=False

client = EvernoteClient(token=auth_token, sandbox=sandbox,china=china)

user_store = client.get_user_store()

version_ok = user_store.checkVersion(
    "Evernote EDAMTest (Python)",
    UserStoreConstants.EDAM_VERSION_MAJOR,
    UserStoreConstants.EDAM_VERSION_MINOR
)
print("Is my Evernote API version up to date? ", str(version_ok))
print("")
if not version_ok:
    exit(1)

note_store = client.get_note_store()

# List all of the notebooks in the user's account
notebooks = note_store.listNotebooks()

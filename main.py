# importing os module
import os
import pprint

# Get the list of user's
env_var = os.environ


os.environ['own_token'] = 'aaa'

# Print the list of user's
print("User's Environment variable:")
pprint.pprint(dict(env_var), width=1)
from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
api = Linkedin('', '*******')

# GET a profile
profile = api.get_profile('billy-g')


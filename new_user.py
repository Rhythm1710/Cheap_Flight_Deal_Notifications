import requests
import re
import email.utils as e

endpoint = "https://api.sheety.co/0136853def3d16907ae330700c98e64e/flightDeals/users"
api_key = "Bearer safdksajkfsadkfsalfklsafkldsaf214332424355252525"


class NewUser:
    def is_valid_email(self,email):
        try:
            parsed_email = e.parseaddr(email)
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', parsed_email[1]):
                return True
            else:
                return False
        except Exception:
            return False

    def register_new_user(self,first_name,last_name,email):
        headers={
            'Authorization': api_key,
        }
        parametres = {
            "user":{
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(endpoint,json=parametres,headers=headers)
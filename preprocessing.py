#Login get token for further api requests
#Get list of all circles
from config import env
import string
import random
#Delete test account
#Delete Victory
#Delete update

#Create accounts admin prod/staging
#True flow : Login -> get token -> get all users -> get id -> delete if exists user_test_mail 
#Lazy solution : generate a random email with isn't contained in db
def get_user_list():
    import requests
    if env=="staging":
        url = "https://staging-api.herocircle.app/users/all"

    payload = {}
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0VG9WYXQiOnRydWUsIl9pZCI6IjY0MTU1NzcxOWE1NjQ0ZTVkMGMwYjk3ZSIsInJlZ2lzdGVyVHlwZSI6InN0YW5kYXJkIiwiZmlyc3RuYW1lIjoiTW9ldGF6IiwibGFzdG5hbWUiOiJCcmF5ZWsiLCJlbWFpbCI6Im1vZXRhekBhZG1pbi5jb20iLCJwcml2YXRlQWNjb3VudCI6dHJ1ZSwicm9sZSI6ImFkbWluIiwiaGFzUGFzc3dvcmQiOnRydWUsIl9za2lsbHMiOltdLCJfY2FyZXMiOltdLCJzdGF0dXMiOnRydWUsInJlZmVycmFsSWQiOm51bGwsImlzUGF5b3V0UmVhZHkiOmZhbHNlLCJwZW5kaW5nUGF5b3V0IjowLCJjcmVhdGVkQXQiOiIyMDIzLTAzLTE4VDA2OjE3OjIxLjc4OFoiLCJ1cGRhdGVkQXQiOiIyMDIzLTA1LTA5VDIyOjU4OjU4LjAwMloiLCJfX3YiOjAsInBhc3N3b3JkIjoiJDJhJDEyJEx4dWg4ZFplQm12OFIucXZick5Jek9ubDBSWTlJaEFUUGVqeTdFN2UxWWk5clRCWDYxcXlXIiwiY3VzdG9tZXJJZCI6ImN1c19OWlZYczN3YnNKVHROcSIsImFjY2VwdHNDb29raWVzIjp0cnVlLCJmdWxsbmFtZSI6Ik1vZXRheiBCcmF5ZWsiLCJyZWZlcnJhbExpbmsiOiJodHRwczovL2hlcm9jaXJjbGUuYXBwL3JlZ2lzdGVyP3JlZmVycmFsSWQ9NjQxNTU3NzE5YTU2NDRlNWQwYzBiOTdlIiwiaWF0IjoxNjg0NzQ3ODAyfQ.Z4CAzTA6DnYQAN7FnY8umBX_Q1NJp0KNOjty0z0I3mU'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

print(get_random_string(5))
#get_user_list()
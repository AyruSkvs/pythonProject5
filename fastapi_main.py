import requests

def get_email():
    urls = ['https://reqres.in/api/users/1',
            'https://reqres.in/api/users/3',
            'https://reqres.in/api/users/10']

    out_lst = []
    for each in urls:
        response = requests.get(each)
        out_lst.append(response.json()['data']['email'])


    return out_lst

print(get_email())
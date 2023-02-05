import requests

# Expects a string username
def get_user_languages(username):
    
    url = 'https://api.github.com/users/' + username + '/repos'
    payload = {'full_name': ''}
    
    # get the user's json data
    response = requests.get(url, data=payload)
    repos = response.json()
    
    # extract languages
    user_languages = set()
    
    for i in range(len(repos)):
        j = repos[i]['language']
        if j:
            user_languages.add(j)
    
    
    lang_str = ', '.join(user_languages)
    return lang_str

    
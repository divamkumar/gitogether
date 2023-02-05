import requests


# string get_user_languages(string username)
def get_user_languages(username):
    
    url = 'https://api.github.com/users/' + username + '/repos'
    payload = {'full_name': ''}
    
    # get the user's json data
    response = requests.get(url, data=payload)
    
    # make sure that the user exists, if not return error text
    if response.status_code != 200:
        return 'Unable to find user languages.'
    
    
    # Variable declarations
    repos = response.json() # user's repos
    user_langs = []         # user's languages
    occurrences = []         # occurrences of each language

    # for every repo fetched
    for i in range(len(repos)):
        lang = repos[i]['language']
       
        # if it doesn't exist in the list already, add it
        if lang not in user_langs and lang:
            user_langs.insert(i, lang)
            occurrences.insert(i, 1)
        # if it exists, increment the number of occurences    
        elif lang:
            ind = user_langs.index(lang)
            occurrences[ind] = occurrences[ind] + 1
    
    # sort them in order of occurences, descending.
    occurrences_sorted = sorted(range(len(occurrences)),key=lambda user_langs:occurrences[user_langs],reverse=True)
    langs_sorted = [user_langs[i] for i in occurrences_sorted ]

    return ', '.join(langs_sorted)

print(get_user_languages('hello'))
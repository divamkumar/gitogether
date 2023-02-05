# int compare_languages(string user1, string user2)
# returns either 0 or 1 depending on the number of programming languages
# two users share
def compare_languages(user1, user2):
    
    # split them into lists
    user1_languages = user1.split(', ')
    user2_languages = user2.split(', ')
    
    # check the items they have in common
    same = len(set(user1_languages) & set(user2_languages))
    
    # returns 1 if the users share at least 3 languages, or all of one user's languages
    # otherwise returns 0
    if same >= 3 or same == len(user1_languages) or same == len(user2_languages):
        return 1
    else:
        return 0
    

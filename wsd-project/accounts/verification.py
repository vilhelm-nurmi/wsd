def is_player(user):
    #Checks the type of the user, TODO change to groups
    if not user.is_authenticated :
        return False
    if user.type=='P':
        return True
    return False
def owns_game(game,user):
    try:
        if game in user.purchased_games.all():
            return True
    except:
        return False
    return False

def is_developer(user):
    #Checks the type of the user, TODO change to groups
    if not user.is_authenticated :
        return False
    if user.type=='D':
        return True
    return False

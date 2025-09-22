def extraction(user):
    username = user["profile"]["username"]
    email = user["profile"]["email"]
    theme = user["settings"]["theme"]
    print("Username: ", username)
    print("Email: ",email)
    print("Theme:", theme)

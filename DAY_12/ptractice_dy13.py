files=["sunset.png","waterfall.png","mountains.png","sunrize.mp4","sunset.mp4"]

photos=[]
videos=[]

for f in files:
    if f.endswith((".png",".jpg")):
        photos.append(f)
    elif f.endswith((".mp3",".mp4")):
        videos.append(f)

print("Photos:", photos)
print("Videos:", videos)

fav = input("Enter file names (comma separated): ").split(",")

# remove spaces
fav = [f.strip() for f in fav]

for name in fav:
    if name in photos:
        print(name, "is sent (photo)")
    elif name in videos:
        print(name, "is sent (video)")
    else:
        print(name, "not found")

    
"""
#email regestration
accounts = {}

for i in range(5):
    print(f"\nRegistration {i+1}")
    
    email = input("Enter email: ")
    password = input("Enter password: ")


    if email in accounts:
        print("Email already existed!")
    else:
        accounts[email] = password
        print("Account created successfully!")

print("\n---- Registered Accounts ----")
for email in accounts:
    print(email)
"""

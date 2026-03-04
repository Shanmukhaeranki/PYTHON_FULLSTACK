"""
class Flipkart:
    discount = 10

    @classmethod
    def updateddiscount(cls, newdiscount):
        cls.discount = newdiscount
        
    def userinfo(self, name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber
        print(f"username: {self.name}")
        print(f"phonenumber: {phonenumber}")
              
    @staticmethod
    def banner():
        print("welcom to Flipkart SHOP NOW")


shannu = Flipkart()
shannu.userinfo("shannu", "2345678912")
shannu.updateddiscount(30)
Flipkart.updateddiscount(40)
Flipkart.banner()

saaketh = Flipkart()
saaketh.userinfo("saaketh", "23456789098")

nikhil = Flipkart()
nikhil.userinfo("nikhil", "23465434543")

"""





#constructor(self call)
#INHERITANCE(#single,#multiple.#multi-level,)
class InstagramV1:
    def __init__(self, username):
        self.username = username
        print(f"Heyy {self.username} Welcome to insatgram!!")

    def reels(self):
        print("you can scroll reels")

    def posts(self):
        print("you can post here")


class InstagramV2(InstagramV1):
    def __init__(self, username):
        super().__init__(username)

    def story(self):
        print("You can uplod the story")


class InstagramV3(InstagramV2):
    def __init__(self, username):
        super().__init__(username)

    def note(self):
        print("you can upload note")


class live:
    def launchlive(self):
        print("you can go live now")


class verification:
    def verify(self):
        print("You can verify your account now!!")


class InstagramV4(InstagramV3, live, verification):
    def __init__(self, username):
        super().__init__(username)


class creator(InstagramV4):
    def __init__(self, username):
        super().__init__(username)

    def insight(self):
        print("you can check your post insight")


class Business(InstagramV4):
    def __init__(self, username):
        super().__init__(username)

    def button(self):
        print("you can contact them mail and number")


shannu = InstagramV1("shannu")
shannu.reels()
shannu.posts()

print("\n")

saaketh = InstagramV2("saaketh")
saaketh.reels()
saaketh.posts()
saaketh.story()

print("\n")

nikhil = InstagramV3("nikhil")
nikhil.reels()
nikhil.posts()
nikhil.story()
nikhil.note()

print("\n")

Tagore = InstagramV4("Tagore")
Tagore.reels()
Tagore.posts()
Tagore.story()
Tagore.note()
Tagore.launchlive()

print("\n")

nuthan = InstagramV4("nuthan")
nuthan.reels()
nuthan.posts()
nuthan.story()
nuthan.note()
nuthan.launchlive()
nuthan.verify()
nuthan.insight()
nuthan.button()


























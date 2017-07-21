class user:

    def __init__ (self, newusername, newuserid):
        self.username = newusername
        self.userid = newuserid
        self.friends = []


    def getusername(self):
        return self.username

    def getuserID(self):
        return self.userID

    def getfriends(self):
        return self.friends

    def addfriends(self, friendid):
        self.friends.append(friendid)



class network:
    def __init__(self):
        self.users=[]



    def numusers(self):
        return len(self.users)
        #uses length of list to find amount of users

    def adduser(self, username):
        user_id=len(self.users)
        self.users.append(user(username, user_id))
        #Would cause user to have to make a user name and password



    def getuserid(self, username):
        return user_id
        for user in self.users:
            if username== user.getusername():
                user_id=user.getuserid()
                #to get user id it has to to return back and if the username= user id then it is gotten
    def addconnection(self, user1,user2):
        user1_id=self.getuserid(user1)
        user2_id=self.getuserid(user2)

        user1=self.getusers[user1_id]
        user2=self.getusers[user2_id]

        self.users[user2_id].addfriends(user1_id)
        self.users[user1_id].addfriends(user2_id)





    def printusers(self):
        print("This is the Network")
        for users in self.users:
            print("\tuser {}: {}".format(user.getid, user.getusername))
            #goes to a new line because of t and stores these users in the orange brackets

    def printconnections(self, username):
        user=self.users[self.getuserid(username)]
        #goes in user list and uses user id to search within the list.
        connections==user.getfriends()
        print("\t{}'s connections".format(user.getusername()))
        #its saying user connections and then prints it out
        for friendid in connections:
            friend=self.users[friends]
            print("\t {}".format(friend.getusername()))
        #uses user id to find user name of each user and prints.



def main():
    mynetwork=network()
    done=False
    while not done:
        action=input("\nwhat would you like to do? add a user(u), add a connection(c), print friend list (p),print connections(pc) exit(e)")

        if action=="u":
            username=input("what username?") #adds username using user input
            mynetwork.adduser(username) #adds that username from user input into the network

        elif action=="c":
            if mynetwork.numusers()<2:
                print("Error. Don't have enough users.")
                continue #exits the loop and starts over but break just completely breaks it
            else:
                user1=input("first user?")
                user2=input("second user?")
                mynetwork.addconnection(user1,user2)#add input of both user 1 and 2 to mynetwork

        elif action=="p":
            mynetwork.printusers()

        elif action=="pc":
            user=input("what user?")
            mynetwork.printconnections(user)

        elif action=="e":
            print("sorry to see you go")
            done=True


        else:
            print("ERROR. STUPID DOG YOU MAKE ME GO MAD!!")



if __name__ == '__main__':
    main()

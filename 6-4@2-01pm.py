class Connect:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user not in self.users:
            self.users[user] = []

    def add_friend(self, user1, user2):
        if user1 in self.users and user2 in self.users:
            self.users[user1].append(user2)
            self.users[user2].append(user1)

    def delete_user(self, user):
        if user in self.users:
            del self.users[user]
            for friends in self.users.values():
                if user in friends:
                    friends.remove(user)

    def remove_friend(self, user1, user2):
        if user1 in self.users and user2 in self.users:
            if user2 in self.users[user1]:
                self.users[user1].remove(user2)
            if user1 in self.users[user2]:
                self.users[user2].remove(user1)

    def display_network(self):
        for user in self.users:
            print(user, "->", ', '.join(self.users[user]))

    def show_friends(self, user):
        if user in self.users:
            print("Friends of", user, ":", ', '.join(self.users[user]))

    def mutual_friends(self, user):
        if user in self.users:
            mutuals = []
            for friend in self.users[user]:
                for friend_of_friend in self.users[friend]:
                    if friend_of_friend not in self.users[user] and friend_of_friend != user:
                        mutuals.append(friend_of_friend)
            print("Mutual friends of", user, ":", ', '.join(set(mutuals)))


# Example usage
c = Connect()
c.add_user("Alice")
c.add_user("Bob")
c.add_user("Charlie")
c.add_user("David")
c.add_friend("Alice", "Bob")
c.add_friend("Bob", "Charlie")
c.add_friend("Charlie", "David")
c.display_network()
c.show_friends("Alice")
c.mutual_friends("Alice")
c.remove_friend("Alice", "Bob")
c.display_network()
c.delete_user("Charlie")
c.display_network()
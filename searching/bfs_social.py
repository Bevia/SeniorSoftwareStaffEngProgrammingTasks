from collections import deque

# Define the social network graph as an adjacency list
social_network = {
    "Alice": ["Bob", "Claire", "David"],
    "Bob": ["Alice", "Emma", "Fred"],
    "Claire": ["Alice", "George", "Hannah"],
    "David": ["Alice"],
    "Emma": ["Bob"],
    "Fred": ["Bob"],
    "George": ["Claire"],
    "Hannah": ["Claire"]
}


# BFS function to find friends-of-friends
def find_friends_of_friends(network, start_person):
    visited = set([start_person])  # Track visited nodes to avoid loops
    queue = deque([(start_person, 0)])  # Queue stores (person, depth level)
    friends_of_friends = []  # List to store friends-of-friends

    while queue:
        person, depth = queue.popleft()

        # Only consider friends-of-friends (depth == 2)
        if depth == 2:
            friends_of_friends.append(person)

        # Stop further search once we reach depth of 2
        elif depth < 2:
            for friend in network[person]:
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, depth + 1))

    return friends_of_friends


# Find friends-of-friends for Alice
result = find_friends_of_friends(social_network, "Alice")
print("Friends of friends of Alice:", result)
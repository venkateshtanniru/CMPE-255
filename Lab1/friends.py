
users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    # TODO
    count = 0
    for i in users:
        if i["name"]== user:
            user_id= i["id"]
            break
    for j in friendship:
        if user_id in j:
            count=count+1
    return count
sorted_friends={}
def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    # TOOD
    for i in users:
        sorted_friends.update({i["name"]:num_friends(i["name"])})
    #print(sorted_friends)
    import operator
    sorted_d = sorted(sorted_friends.items(), key=operator.itemgetter(1),reverse=True)
    print(sorted_d)
    
sort_by_num_friends()


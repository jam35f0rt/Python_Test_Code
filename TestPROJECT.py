example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

def create_data_structure(string_input):
    network={}
    if string_input == '':
        return network
    newlist = string_input[:-1].split('.')
    for i in  newlist:
        b, a = [], []
        if i.split()[0] not in network:
            network[i.split()[0]] = {}
        if 'connected' in i:
            i = i.replace('to','to,')
            for k in range(1,len(i.split(','))):
                b = b+[i.split(',')[k][1:]]
            network[i.split()[0]]['connection'] = b
        if 'likes to play' in i:
            i = i.replace('play','play,')
            for k in range(2,len(i.split(','))):
                a = a +[i.split(',')[k][1:]]
            network[i.split()[0]]['gamesliked'] = a
    return network

def get_connections(network, user):
    if user not in network:
        return None
    list_con = []
    if network[user]['connection'] != []:
        for i in network[user]['connection']:
            list_con = list_con + [i]#[user +' is connected to'+ i]
    return list_con

def get_games_liked(network,user):
    if user not in network:
        return None
    list_games = []
    if network[user]['gamesliked'] != []:
        for i in network[user]['gamesliked']:
            list_games = list_games + [i]#[user +' likes play to'+ i]
    return list_games

def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    if user_B in network[user_A]['connection']:
        return 'network unchanged'
    network[user_A]['connection']=network[user_A]['connection']+[user_B]
    return 'Network update with succes!'

def add_new_user(network, user, games):
    if user in network:
        return 'network *UNCHANGED*'
    network[user]={}
    network[user]['connection'] = []
    network[user]['gamesliked'] = games
    return 'User added with succes'

def get_secondary_connections(network, user):
    if user not in network:
        return None
    list_sec_con = []
    for each_user in get_connections(network,user):
        list_sec_con = list_sec_con + get_connections(network, each_user)
    return list_sec_con

def count_common_connections(network, user_A, user_B):
    if user_A not in network  or user_B not in network:
        return False
    common_conn = 0
    b = get_connections(network, user_B)
    for conn in get_connections(network, user_A):
        if conn in b :
            common_conn += 1
    return common_conn

'''def find_path_to_friend(network, user_A, user_B):
    if user_A not in network  or user_B not in network:
        return None
    if user_B == user_b :
        return path
    else:'''
        

net = create_data_structure(example_input)
print (net)
print ('--------------------Debra\'s connection------------------')
print (get_connections(net, "Debra"))
print (get_connections(net, "Mercedes"))
print (get_games_liked(net, "John"))
print (add_connection(net, "John", "Freda"))
print (get_connections(net, "John"))
print (add_new_user(net, "James", ['pes2017','FIFA17']) )
print (add_new_user(net, "Debra", []) )
print (get_games_liked(net, "John"))
print (add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"])) # True
print (get_secondary_connections(net, "Mercedes"))
print (get_connections(net, "James"))
print (get_secondary_connections(net, "James"))
print (count_common_connections(net, "James", "John"))
#print (find_path_to_friend(net, "John", "Ollie"))















'''def get_connections(network, user):
    res, a, in_it = [], '', 0
    for info in network:
        if user in info :
            if 'connected' in info:
                if user==info.split()[0]:
                    res = res + [info]
                else:
                    if a == '':
                        a = a + info[:info.find('to')+3] + user 
                    else:
                        a = info[:info.find(' ')] +', ' + a
            in_it = 1
    if a != '':
        res.append(a)
    return res if res != [] else [] if in_it == 1 else None
            
def get_games_liked(network,user):
    return []
    
net = create_data_structure(example_input)
print (net)
print ('--------------------Debra\'s connection------------------')
print (get_connections(net, "Debra"))
print ('--------------------Mercedes\'s connection------------------')
print (get_connections(net, "Mercedes"))'''

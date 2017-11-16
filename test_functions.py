import math
'''def get_dist_score(moves, centers):
    return [sum([c2-abs(c1-c2) for(c1,c2) in zip(move, centers)])+1 for move in moves]


def get_center(game_width, game_height):
    center = []
    for i in range((game_width%2+1)%2+1):
        for j in range((game_height%2+1)%2+1):
            center.append((math.ceil(game_width/2+i-1),math.ceil(game_height/2+j-1)))
    return center'''
    


def get_center(game_width, game_height):
    return (((game_width-1)/2, (game_height-1)/2))

def get_dist_score(moves, centers):
    return [sum([c2-(c1-c2)**2 for(c1,c2) in zip(move, centers)])+1 for move in moves]

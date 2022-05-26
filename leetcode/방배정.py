import sys
sys.setrecursionlimit(10000)
def solution(k, room_number):
    def find(x,rooms):
        if x not in rooms:
            rooms[x] = x+1
            return x
        empty = find(rooms[x],rooms)
        rooms[x] = empty+1
        return empty
        
    answer = []
    rooms = {}
    for room in room_number:
        r = find(room, rooms)
        answer.append(r)
    return answer
    
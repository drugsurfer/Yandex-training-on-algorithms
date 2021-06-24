t_room, t_cond = map(int, input().split())
mode = input()
if mode == 'freeze' and t_room >= t_cond:
    t_room = t_cond
    print(t_room)
elif mode == 'heat' and t_room <= t_cond:
    t_room = t_cond
    print(t_room)
elif mode == 'auto':
    t_room = t_cond
    print(t_room)
elif mode == 'fan':
    print(t_room)
else:
    print(t_room)
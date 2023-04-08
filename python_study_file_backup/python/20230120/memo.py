
import datetime

booked = [ ["09:55","hae"], ["10:05","jee"] ]
unbooked = [ ["10:04","hee"], ["14:07","eom"] ]

bi = 0
ubi = 0

print(int(booked[bi][0][:2]))
print(int(booked[bi][0][3:]))

b_t = datetime.datetime.strptime(booked[bi][0], "%H:%M")
ub_t = datetime.datetime.strptime(unbooked[ubi][0], "%H:%M")

print(b_t, ub_t)


b_t_h, b_t_m = int(booked[bi][0][:2]), int(booked[bi][0][3:])
ub_t_h, ub_u_m = int(unbooked[ubi][0][:2]), int(unbooked[ubi][0][3:])

print(b_t_h, b_t_m)
print(ub_t_h, ub_u_m)

t_h = 9
t_m = 55

b_t_h = 10
b_t_m = 0

if t_h*60+t_m <= b_t_h*60+b_t_m <= t_h*60+t_m+10:
    print('?? {} <= {} <= {}'.format(t_h*60+t_m, b_t_h*60+b_t_m, t_h*60+t_m+10))


l = []
l.append("%d:%d"%(10,3))
print(l)

l_h, l_m = int(l[0][:2]), int(l[0][3:])
print(l_h, l_m)


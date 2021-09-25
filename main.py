print('x','y','z','w','f')
for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                f= not (x and y) or (z and w) or (w and y)or (not x and w)
                if f==0:
                    print(x,y,z,w,f)
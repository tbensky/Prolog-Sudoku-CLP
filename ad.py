letters = ["A","B","C","D","E","F","G","H","I"]

def ad_cols(c):
    print("all_distinct([",end='')
    
    for i in range(1,10):
        if i < 9:
            print(f"{c}{i}",end=',')
        else:
            print(f"{c}{i}",end='')
    print("]).")
    

def ad_rows(i):
    print("all_distinct([",end='')
    
    for c in letters:
        if c < "I":
            print(f"{c}{i}",end=',')
        else:
            print(f"{c}{i}",end='')
    print("]).")
    
def ad_blocks(which,offset):
    print("all_distinct([",end='')
    
    for i in range(offset,offset+3):
        for c in which:
            if i != offset+2:
                print(f"{c}{i},",end='')
            else:
                if c != which[-1]:
                    print(f"{c}{i},",end='')
                else:
                    print(f"{c}{i}",end='')
    print("]).")              

print("% cols")
for c in letters:
    ad_cols(c)
    
print("\n% rows")

for i in range(1,10):
    ad_rows(i)
    
print("\n% blocks")
blocks = [["A","B","C"],["D","E","F"],["G","H","I"]]

for bl in blocks:
    ad_blocks(bl,1)
    ad_blocks(bl,4)
    ad_blocks(bl,7)
def shift():
     with open("one.txt", 'r') as a:
         data_a = a.read()
     with open ("two.txt", 'r')as b:
         data_b = b.read()
     with open ("one.txt" , 'w')as ab:
         ab.write(data_b)
     with open ("two.txt" , 'w')as ba:
         ba.write(data_a)
         
shift()
print("shiffted")
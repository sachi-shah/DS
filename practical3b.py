# Implement Tower of Hanoi


def TowerOfHanoi(n , from_, to, middle):
   if n == 1:
      print ("Move disk 1 from rod",from_,"to rod",to)
      return
   
   TowerOfHanoi(n-1, from_, middle, to)
   print("Move disk",n,"from rod",from_,"to rod",to)
   TowerOfHanoi(n-1, middle, to, from_)
    
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')





#Write a recursive function that prints numbers from n down to 1.
def show(n):
   if(n == 0):
      return
   print(n)
   show(n-1)

   show(5)
#Creating a function for the week day calculation.
def dayofweek(d,m,y):
    t=[0,3,2,5,0,3,5,1,6,2,4]
    y-=m<3
    #Here we use a formula for the Day number calculation.
    return((y+int(y/4)-int(y/100)+int(y/400)+t[m-1]+d)%7)
x=int(input("Enter the date (in DD Format)"))
y=int(input("Enter the Month(in MM Format)"))
z=int(input("Enter the Year(in YYYY Format)"))

day=dayofweek(x,y,z)
#Declaring an array for the calculated number to be display as Days.
Days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
print("The Day is "+Days[day])


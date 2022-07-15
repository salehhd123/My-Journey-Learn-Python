#this code Represents the phone book, receives the phone number, and returns to us the name of the owner of the number


users =[
    {'name':'Saleh','phoneNumber':1111111111},
    {'name':'Amal','phoneNumber':2222222222},
    {'name':'Khadijah','phoneNumber':3333333333},
    {'name':'Abdullah','phoneNumber':4444444444},
    {'name':'Rawan','phoneNumber':5555555555},
    {'name':'Faisal','phoneNumber':6666666666},
    {'name':'Layla','phoneNumber':7777777777},
]

def check(num):
        for x in users:
            if(type(num)== int):
                if  num == x.get('phoneNumber'):
                    print('the number is for :' + x.get('name'))
                else:
                    print('Sorry, the number is not found')
            else:
                print('This is invalid number')

#not found number
check(2)
#found number
check(1111111111)
#invalid number because the type is string
check('1')

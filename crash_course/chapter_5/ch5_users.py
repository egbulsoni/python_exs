usernames = ['anne', 'john', 'mary', 'luke', 'admin', 'peter']
if usernames:
    for username in usernames:
        if username == 'admin':
         print(f'Hello {username}, would you like to see the status report?')
        else:
            print(f'Hello {username}, thank you for logging in!')
else:
    print('there are no users in the userbase')

# ex 5.10

new_users = ['Loki', 'Peter', 'MARY', 'eric']
for user in new_users:
    if user.lower() in usernames:
        print(f'{user} already exists, you must choose another username!')
    else:
        print(f'The username {user} is available!')
        
# ex 5.11

nums = list(range(1,10))
for num in nums:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')


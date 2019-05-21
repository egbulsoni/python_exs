motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
popped = motorcycles.pop(2) #pop without arguments pops the last item
print(popped) #shows the popped item
del motorcycles[0] #delete the item (without returning it)
print(motorcycles)
#when you don't know what's the element:
motorcycles.remove('yamaha') #note: this method removes only 1st occurrence
print(motorcycles)

order = []
for i in range(1,6):
    ordr = input("Enter order: ")
    order.append(ordr)
print("Original Orders:")
print(order)
updt = input("Enter additional Order: ")
print("Updated Orders:")
order.insert(6,updt)
print(order)
udt = input("Enter Priority Order: ")
order.insert(0,udt)
print(order)

bt = input("Enter which order to search")
print(f"Number of occurances: {order.count(bt)}")
print(f"First occurance: {order.index(bt)}")
bl = input("Enter which order to cancel")
print(order.remove(bl))
print(order)
print(f'Last order removed: {order.pop(5)}')
print(sorted(order))
print(f"Total orders: {len(order)}")


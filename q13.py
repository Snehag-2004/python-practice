
def findCheapestPrice(n, flights, src, dst, k):

    price = [float('inf')] * n
    price[src] = 0

    for i in range(k + 1):

        temp = price.copy()

        for flight in flights:
            u, v, cost = flight

            if price[u] != float('inf'):
                temp[v] = min(temp[v], price[u] + cost)

        price = temp

    if price[dst] == float('inf'):
        return -1

    return price[dst]


# Example 1
n = 4
flights = [[0,1,100], [1,2,100], [2,0,100],
           [1,3,600], [2,3,200]]

src = 0
dst = 3
k = 1

print("Cheapest Price:", findCheapestPrice(n, flights, src, dst, k))


# Example 2
n = 3
flights = [[0,1,100], [1,2,100], [0,2,500]]

src = 0
dst = 2
k = 1

print("Cheapest Price:", findCheapestPrice(n, flights, src, dst, k))


# Example 3
n = 3
flights = [[0,1,100], [1,2,100], [0,2,500]]

src = 0
dst = 2
k = 0

print("Cheapest Price:", findCheapestPrice(n, flights, src, dst, k))

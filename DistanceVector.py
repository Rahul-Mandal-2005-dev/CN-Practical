
def distance_vector():
    n = int(input("Enter number of routers: "))
    print("Enter cost matrix (999 means infinity):")

    cost = []
    for i in range(n):
        cost.append(list(map(int, input().split())))

    dist = [row[:] for row in cost]
    next_hop = [[j if cost[i][j] != 999 and i != j else -1
                 for j in range(n)] for i in range(n)]

    for _ in range(n - 1):
        changed = False

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if cost[i][k] != 999 and dist[k][j] != 999:
                        new_cost = cost[i][k] + dist[k][j]

                        if new_cost < dist[i][j]:
                            dist[i][j] = new_cost
                            next_hop[i][j] = k
                            changed = True

        if not changed:
            break

    for i in range(n):
        print("\nRouting table for Router", i + 1)
        print("Destination\tCost\tNext Hop")

        for j in range(n):
            hop = "-" if i == j else (
                str(next_hop[i][j] + 1) if next_hop[i][j] != -1 else "None"
            )
            print(j + 1, "\t\t", dist[i][j], "\t", hop)

def main():
    distance_vector()

main()

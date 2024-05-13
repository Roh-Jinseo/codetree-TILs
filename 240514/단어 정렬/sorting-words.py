n = int(input())
wrds = [input() for _ in range(n)]
print(*sorted(wrds), sep='\n')
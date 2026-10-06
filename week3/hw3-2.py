N, Dsq = map(int, input().split())

sensors = set()

for i in range(N):
    x, y, z, power = map(int, input().split())
    sensors.add((x, y, z, power))

sensors = tuple(sensors)

interference = set()

for i in range(len(sensors)):
    for j in range(i + 1, len(sensors)):
        a = sensors[i]
        b = sensors[j]

        distance_sq = (
            (a[0] - b[0]) ** 2
            + (a[1] - b[1]) ** 2
            + (a[2] - b[2]) ** 2
        )

        if distance_sq <= Dsq and a[3] != b[3]:
            if a < b:
                pair = (a, b)
            else:
                pair = (b, a)

            interference.add(pair)

result = sorted(interference)

print(f"Interference Pairs: {len(result)}")

for a, b in result:
    print(f"{a} <-> {b}")

import sys

class SourceDestination:
    def __init__(self, source: int, destination: int, length: int) -> None:
        self.source = source
        self.destination = destination
        self.length = length
    

class Mapping:
    def __init__(self,  name: str) -> None:
        self.name = name
        self.maps: list[SourceDestination] = []

    def addMap(self, source: int, destination: int, length: int):
        self.maps.append(SourceDestination(source, destination, length))


def applyMap(value: int, maps: list[SourceDestination]) -> int:
    for m in maps:
        if m.source <= value < m.source + m.length:
            return value + m.destination - m.source
    return value


def day4(): 
    part1 = sys.maxsize
    part2 = sys.maxsize
    maps: list[Mapping] = []
    with open('2023/inputs/day5.txt') as f:
        for line in f:
            if 'seeds:' in line:
                data = line.split(': ')
                seeds = [int(x) for x in data[1].split(' ')]
                continue
            if 'map' in line:
                currentMap = Mapping(line.split(' ')[0])
                maps.append(currentMap)
            elif line != '\n':
                dest, source, length = line.strip().split(' ')
                currentMap.addMap(int(source), int(dest), int(length))

    for seed in seeds:
        currentValue = seed
        for currentMap in maps:
            currentValue = applyMap(currentValue, currentMap.maps)

        part1 = min(part1, currentValue)


    for i, seed in enumerate(seeds[::2]):
        locations = []

        for j in range(seed, seed + seeds[i*2+1], 1_000_000):
            currentValue = j
            for currentMap in maps:
                currentValue = applyMap(currentValue, currentMap.maps)

            locations.append((j, currentValue))

        newSeed, lowestLocation = min(locations, key=lambda x: x[1])
        

        for k in range(6, 0, -1):
            locations = []
            for j in range(newSeed - 10**k, newSeed + 10**k, 10**(k-1)):
                currentValue = j
                for currentMap in maps:
                    currentValue = applyMap(currentValue, currentMap.maps)

                locations.append((j, currentValue))

            newSeed, lowestLocation = min(locations, key=lambda x: x[1])

        part2 = min(part2, lowestLocation)

    return part1, part2

print(day4())

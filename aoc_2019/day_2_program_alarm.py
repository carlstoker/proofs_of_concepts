def process_opcodes(opcodes, noun, verb):
    li = opcodes[:]
    i = 0
    li[1], li[2] = noun, verb

    while (i + 3) < len(li):
        n1, n2, n3 = li[i + 1:i + 4]
        if li[i] == 1:
            li[n3] = li[n1] + li[n2]
        elif li[i] == 2:
            li[n3] = li[n1] * li[n2]
        else:
            return li[0]
        i += 4


def find_noun_verb(li, desired_num):
    for noun in range(100):
        for verb in range(100):
            if process_opcodes(li, noun, verb) == desired_num:
                return '{}'.format((100 * noun) + verb)


with open("aoc_day_2.txt", "r") as f:
    inp = [int(x) for x in f.read().split(',')]

print("Part one:", process_opcodes(inp, 12, 2))
print("Part two:", find_noun_verb(inp, 19690720))

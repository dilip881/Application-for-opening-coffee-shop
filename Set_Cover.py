def set_cover(universe, subsets):
    elements = set(e for s in subsets for e in s)
    if elements != universe:
        return None
    covered = set()
    cover = []
    while covered != elements:
        subset = max(subsets, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset

    return cover


def main():
    all_sets = []
    sub_set = set()
    print("ENTER THE LOWER RANGE OF ELEMENTS:")
    a = int(input())
    print("ENTER THE HIGHER RANGE OF ELEMENTS:")
    b = int(input())
    universe = set(range(a, b))
    print("ENTER THE NUMBER OF SUB-SETS:")
    size = int(input())
    for i in range(size):
        print("ENTER THE NUMBER OF SUB-SET ELEMENTS:")
        n = int(input())
        for j in range(n):
            print("ENTER THE ELEMENT INTO SUBSET:")
            element = int(input())
            sub_set.add(element)
            all_sets.append(sub_set)
            continue
    cover = set_cover(universe, all_sets)
    print(all_sets[1])

if __name__ == '__main__':
    main()

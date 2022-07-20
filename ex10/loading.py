from re import I


def ft_progress(lst):
    i = 1
    while i <= len(lst):
        yield i
        pourc = int(i * 100 / len (lst))
        nb = int(i * 20 / len(lst))
        arrow = ">".rjust(nb, "=")
        print(f"ETA: [{pourc:3}%] [{arrow:<20}] {i}/{len(lst)}")
        i += 1

if __name__ == "__main__":
    listy = range(33)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
    print()
    print(ret)
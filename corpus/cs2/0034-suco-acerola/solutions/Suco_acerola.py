amigos, frutas= input() .split()
amigos, frutas = float(amigos), float(frutas)

while (amigos!=0) and (frutas!=0):
    volume= frutas * 0.05/ amigos

    print(f"{volume: .2f}")
    amigos, frutas = input().split()
    amigos, frutas = float(amigos), float(frutas)
def right_angle_trinagle(n: int) -> None:
    for i in range(n):
        for j in range(i + 1):
            print('*', end=' ')
        print(' ')

right_angle_trinagle(25)


def hollow_spuare_pattern(n: int) -> None:
    
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print('*', end='')
            else:
                print(' ', end='')

        print()
        

hollow_spuare_pattern(10)


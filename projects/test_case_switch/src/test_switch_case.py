'''
Created on Dec 3, 2019

@author: snherbst
'''

def test_1():
    print(1)
    return 1
    
def test_2():
    print(2)
    return 2
2
def test_3():
    print(3)
    return 3

def test_4():
    print(4)
    return 4


if __name__ == '__main__':
    print ("indtast et tal mellem 1-4:", end="")
    input_val = int(input())
    test_val = {
        1:test_1,
        2:lambda : (
            print('et'),
            print('to')
            ),
        3:test_3,
        4:test_4
    }
    test_val[input_val]()
    #print( test_val[input_val]() )

'''
switch (d)
{
    case 1:
        do1();
        do2();
        break;
    case 3:
        do1();
        do3();
        break
    }'''
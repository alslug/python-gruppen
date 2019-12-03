'''
Created on Dec 3, 2019

@author: snherbst
'''

def test_ret(value):
    print(value)
    return value
    

if __name__ == '__main__':
    input_val = 2
    test_val = {
        1:lambda(test_ret(1)),
        2:lambda(test_ret(2)),
        3:lambda(test_ret(3)),
        4:lambda(test_ret(4))
    }
    print( test_val[input_val] )
    print( test_val[input_val]() )

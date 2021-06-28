from myhdl import *


@block
def JKFF(j, k, clk, q, d):

    @always(delay(10))
    def FF():
        if clk == 1:
            q.next = q
        elif j == 0 and k == 0:
            q.next = q
        elif j == 0 and k == 1:
            q.next = 0
        elif j == 1 and k == 0:
            q.next = 1
        elif j == 1 and k == 1:
            q.next = not q
        d.next = not q.next

    return FF

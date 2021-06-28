from myhdl import *
from JKFF import *


@block
def test_JKFF():
    j, k = [Signal(intbv(1)) for i in range(2)]
    q1 = Signal(intbv(0))
    q2 = Signal(intbv(1))
    clk = Signal(intbv(0))

    jkff_1 = JKFF(j, k, clk, q1, q2)

    def clkgen():
        clk.next = not clk

    def clkgen2():
        k.next = not k

    @instance
    def stimulus():
        print("J K Q1 Q2")

        yield delay(9)
        # print("%s %s %s %s" % (j, k, q1, q2))
        # clkgen()
        #
        # yield delay(10)
        # print("%s %s %s %s" % (j, k, q1, q2))
        # clkgen2()

        for i in range(20):
            print("%s %s %s %s" % (j, k, q1, q2))
            yield delay(10)

    return stimulus, jkff_1

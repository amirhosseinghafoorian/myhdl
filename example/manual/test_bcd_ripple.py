from myhdl import *
from JKFF import *


@block
def test_JKFF():
    logic_1 = Signal(intbv(1))
    logic_0 = Signal(intbv(0))

    q1 = Signal(intbv(0))
    q2 = Signal(intbv(0))
    q4 = Signal(intbv(0))
    q8 = Signal(intbv(0))

    d1 = Signal(intbv(0))
    d2 = Signal(intbv(0))
    d4 = Signal(intbv(0))
    d8 = Signal(intbv(0))

    jkff_1 = JKFF(j=logic_1, k=logic_1, clk=logic_0, q=q1, d=d1)
    jkff_2 = JKFF(j=d8, k=logic_1, clk=q1, q=q2, d=d2)
    jkff_4 = JKFF(j=logic_1, k=logic_1, clk=q2, q=q4, d=d4)
    jkff_8 = JKFF(j=(q4 and q2), k=logic_1, clk=q1, q=q8, d=d8)

    @instance
    def stimulus():
        print("Q8 Q4 Q2 Q1")

        yield delay(9)

        for i in range(10):
            print("%s  %s  %s  %s" % (q8, q4, q2, q1))
            yield delay(10)

    return stimulus, jkff_1, jkff_2, jkff_4, jkff_8

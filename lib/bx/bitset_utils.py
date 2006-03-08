from bx.bitset import *

"""
Some basic utils for lists
"""

def bitset_subtract( ex1, ex2 ):
    bits1 = BinnedBitSet(MAX)
    for start,end  in ex1:
        bits1.set_range( start, end - start )

    bits2 = BinnedBitSet(MAX)
    for start,end  in ex2:
        bits2.set_range( start, end - start )

    bits2.invert()
    bits1.iand( bits2 )
    return bits2list( bits1 )

def bits2list( bits ):
    ex = []
    end = 0
    while 1:
        start = bits.next_set( end )
        if start == bits.size: break
        end = bits.next_clear( start )
        ex.append( (start, end) )

    return ex

def bitset_complement( exons ):
    bits = BinnedBitSet(MAX)
    introns = []
    for start, end in exons:
        bits.set_range( start, end - start )
    bits.invert()

    # only complement within the range of the list
    ex_start = min( [a[0] for a in exons] )
    ex_end = max( [a[1] for a in exons] )
    end = ex_start
    len = ex_end
    while 1:
            start = bits.next_set( end )
            if start == bits.size: break
            end = bits.next_clear( start )
            if end > len: end = len
            if start != end:
                introns.append( (start,end ) )
            if end == len: break
    return introns 

def bitset_union( exons ):
    bits = BinnedBitSet(MAX)
    for start,end in exons:
        bits.set_range( start, end - start )
    end = 0
    return bits2list( bits )

import unittest

from schediazo.part import PartDict

class TestPartDict(unittest.TestSuite):
    def test_list_insert(self):
        # Should give: 3, 2, 1
        a = PartDict()
        a._list_insert_head(1)
        a._list_insert_head(2)
        a._list_insert_head(3)
        self.assertEqual([x for x in a], [3,2,1])

        # Should give: 1,2,3
        b = PartDict()
        b._list_insert_tail(1)
        b._list_insert_tail(2)
        b._list_insert_tail(3)
        self.assertEqual([x for x in b], [1,2,3])

        # Should give: 3,1,2
        c = PartDict()
        c._list_insert_tail(1)
        c._list_insert_tail(2)
        c._list_insert_head(3)
        self.assertEqual([x for x in c], [3,1,2])

        # Should give: 2,1,3
        d = PartDict()
        d._list_insert_head(1)
        d._list_insert_head(2)
        d._list_insert_tail(3)
        self.assertEqual([x for x in d], [2,1,3])

    def test_list_insert_remove(self):
        # remove from the middle, head, and tail, middle, to leave two items
        # 1,2,3,4,5,6
        e = PartDict()
        e._list_insert_tail(1)
        e._list_insert_tail(2)
        e._list_insert_tail(3)
        e._list_insert_tail(4)
        e._list_insert_tail(5)
        e._list_insert_tail(6)
        e._list_remove(4)
        e._list_remove(6)
        e._list_remove(1)
        e._list_remove(3)
        self.assertEqual([x for x in e], [2,5])

    def test_list_insert_after_before(self):
        e = PartDict()
        e._list_insert_tail(2)
        e._list_insert_tail(5)

        # try inserting after
        e._list_insert_after(6,2)     # should give 2,6,5
        e._list_insert_after(7,5)     # should give 2,6,5,7
        e._list_insert_after(8,6)     # should give 2,6,8,5,7
        self.assertEqual([x for x in e], [2,6,8,5,7])

        # try inserting before
        e._list_insert_before(9,2)    # should give 9,2,6,8,5,7
        e._list_insert_before(10,2)   # should give 9,10,2,6,8,5,7
        e._list_insert_before(11,7)   # should give 9,10,2,6,8,5,11,7
        self.assertEqual([x for x in e], [9,10,2,6,8,5,11,7])

    def test_list_move(self):
        e = PartDict()
        [e._list_insert_tail(x) for x in [9,10,2,6,8,5,11,7]]

        # try moving items to the head and tail
        e._list_movetohead(6)         # should give 6,9,10,2,8,5,11,7
        e._list_movetohead(9)         # should give 9,6,10,2,8,5,11,7
        e._list_movetotail(8)         # should give 9,6,10,2,5,11,7,8
        e._list_movetotail(7)         # should give 9,6,10,2,5,11,8,7
        self.assertEqual([x for x in e], [9,6,10,2,5,11,8,7])

        # try moving items up and down
        e._list_movetowardshead(2)
        e._list_movetowardshead(2)
        e._list_movetowardshead(2)        # should give 2,9,6,10,5,11,8,7
        e._list_movetowardshead(5)
        e._list_movetowardshead(5)
        e._list_movetowardshead(5)        # should give 2,5,9,6,10,11,8,7
        e._list_movetowardshead(6)        # should give 2,5,6,9,10,11,8,7
        e._list_movetohead(7)             # should give 7,2,5,6,9,10,11,8
        e._list_movetowardstail(7)        # should give 2,7,5,6,9,10,11,8
        e._list_movetowardstail(7)        # should give 2,5,7,6,9,10,11,8
        e._list_movetowardstail(7)        # should give 2,5,6,7,9,10,11,8
        e._list_movetowardshead(8)        # should give 2,5,6,7,9,10,8,11
        e._list_movetowardshead(8)        # should give 2,5,6,7,9,8,10,11
        e._list_movetowardshead(8)        # should give 2,5,6,7,8,9,10,11
        self.assertEqual([x for x in e], [2,5,6,7,8,9,10,11])

    def test_part(self):

        p1 = PartBase(id='1')
        p2 = PartBase(id='2')
        p3 = PartBase(id='3')
        p4 = PartBase(id='4')

        d = PartDict()
        d[p1.id] = p1
        d[p2.id] = p2
        d[p3.id] = p3
        d[p4.id] = p4
        self.assertEqual([x for x in d], ['1','2','3','4'])

        del d[p3.id]
        self.assertEqual([x for x in d], ['1','2','4'])

        p0 = PartBase(id='0')
        d[p0.id] = p0
        self.assertEqual([x for x in d], ['1','2','4','0'])
        d.movetoback('0')
        self.assertEqual([x for x in d], ['0','1','2','4'])
        d.moveforward('1')
        self.assertEqual([x for x in d], ['0','2','1','4'])
        d.movebackward('4')
        self.assertEqual([x for x in d], ['0','2','4','1'])
        d.movetofront('2')
        d.movetofront('1')
        d.movetofront('0')
        self.assertEqual([x for x in d], ['4','2','1','0'])
        self.assertEqual([x for x in reversed(d)], ['0','1','2','4'])

if __name__=='__main__':
    unittest.main()

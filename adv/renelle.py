import adv_test
from adv import *

def module():
    return Renelle

class Renelle(Adv):
    conf = {}
    conf['mod_a1'] = ('crit', 'passive', 0.08, 'hit15')

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0, mass=0)


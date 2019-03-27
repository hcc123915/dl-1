import adv_test
from adv import *

def module():
    return Francesca

class Francesca(Adv):
    conf = {
        "mod_a1"  : ('fs', 'passive', 0.30) ,
        } 



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        `fs, seq=5
        """

    #conf['acl'] = """
    #    `s1
    #    `s3
    #    `s2
    #    """
    adv_test.test(module(), conf, verbose=0, mass=0)


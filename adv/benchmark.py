import adv_test
from adv import *
import mikoto

def module():
    return Mikoto

class Mikoto(mikoto.Mikoto):
    conf = {
        "mod_a2"  : ('crit' , 'chance'  , 0.08) ,
        }
    def pre(this):
        if this.condition('hp70'):
            this.conf['mod_a'] = ('crit' , 'passive', 0.10)
        if this.condition('connect s1'):
            this.s1_proc = this.c_s1_proc

    def init(this):
        this.s1buff = Selfbuff("s1",0.0, 15)
        this.s2buff = Selfbuff("s2",0.2, 10, 'spd')

    def speed(this):
        return 1+this.s2buff.get()
    
    def s1latency(this, e):
        this.s1buff.on()

    def s1_proc(this, e):
        this.s1buff.off()
        this.dmg_make('s1',5.32*2)
        this.s1buff.set(0.10).on()
        Timer(this.s1latency).on(1.5/this.speed())

    def c_s1_proc(this, e):
        buff = this.s1buff.get()
        if buff == 0:
            stance = 0
        elif buff == 0.10:
            stance = 1
        elif buff == 0.15:
            stance = 2
        if stance == 0:
            this.dmg_make('s1',5.32*2)
            this.s1buff.set(0.10) #.on()
            Timer(this.s1latency).on(1.5/this.speed())
        elif stance == 1:
            this.dmg_make('s1',3.54*3)
            this.s1buff.off()
            this.s1buff.set(0.15) #.on()
            Timer(this.s1latency).on(1.5/this.speed())
        elif stance == 2:
            this.dmg_make('s1',2.13*4+4.25)
            this.s1buff.off().set(0)

    def s2_proc(this, e):
        this.s2buff.on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel or fsc
        `s2, seq=5 and cancel or fsc
        `s3, seq=5 and cancel or fsc
        """

    import cProfile
    p = cProfile.Profile()
    p.enable()
    adv_test.test(module(), conf, verbose=0, mass=1)
    p.print_stats()

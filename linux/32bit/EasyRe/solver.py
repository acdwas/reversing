
import angr
import claripy
import binascii


class FUN_0804873b(angr.SimProcedure):
    def run(self):
        pass


p = angr.Project("./EasyRe")

p.hook(0x0804873b, FUN_0804873b())

state = p.factory.entry_state()
sm = p.factory.simulation_manager(state)

sm.explore(find=0x08048dcb, avoid=(0x08048bf6, 0x08048c46, 0x08048db1))

found = sm.found[0]
print(found.posix.dumps(0)[20:52])

# GACTF{c7ack_m3_sh3ll_smc_vm_0k?}


import angr
import binascii

p = angr.Project("./Catch_Me", load_options={"auto_load_libs": False})

state = p.factory.blank_state(addr=0x04005C5, add_options={angr.options.LAZY_SOLVES})

sm = p.factory.simulation_manager(state)

l = []
ll = []

while True:
    a = state.solver.BVS('byte_6012A8', 32)
    b = state.solver.BVS('dword_6012AC', 32)

    for i in range(len(l)):
        state.add_constraints(a != l[i])
        state.add_constraints(b != ll[i])

    l.append(a)
    ll.append(b)

    state.memory.store(0x6012A8, a)
    state.memory.store(0x6012AC, b)

    sm.explore(find=0x04006D6, avoid=(0x40068E))
    found = sm.found[0]

    flag = found.memory.load(0x0601280, 32)

    # found.add_constraints(found.memory.load(0x0601280, 4) == int(binascii.hexlify(b"600d"), 16))
    # found.add_constraints(found.memory.load(0x0601280 + 4, 4) == int(binascii.hexlify(b"_j0b"), 16))

    for i in range(32):
        found.add_constraints(found.solver.Or(found.solver.And(flag.get_byte(i) >= 0x30, flag.get_byte(i) <= 0x39), found.solver.And(flag.get_byte(i) >= 0x61, flag.get_byte(i) < 0x7a), flag.get_byte(i) == 0x5f))

    flag_str = found.solver.eval(flag, cast_to=bytes)
    print(flag_str)
    sm = p.factory.simulation_manager(state)


import angr
import claripy
import binascii

p = angr.Project("./rev200", load_options={"auto_load_libs": False})


input = claripy.BVS("input", 8*9)

state = p.factory.blank_state(addr=0x0400626, add_options={angr.options.LAZY_SOLVES})

state.memory.store(0x10000, input)
state.regs.rdi = 0x10000

for i in range(9):
    state.add_constraints(input.get_byte(i) != 0)
    state.add_constraints(input.get_byte(i) >= 0x20)
    state.add_constraints(input.get_byte(i) <= 0x7f)

state.add_constraints(state.memory.load(0x10000, 5) == int(binascii.hexlify(b"#%Ye7"), 16))

sm = p.factory.simulation_manager(state)

sm.explore(find=0x0400760, avoid=(0x0400677, 0x0400730, 0x040073D))
found = sm.found[0]

flag_str = found.solver.eval(input, cast_to=bytes)
print('Password: ' + flag_str.decode())

# Password: #%Ye7m4g~
# Congratulations!!!
# flag{d1scr337_math_1s_gr3at}

import argparse
import subprocess
#from subprocess import run

commands={
    'list' : 'conda list',
    'envlist' : 'conda env list'
}

def test_var_args(f_arg, *args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print("first normal arg:", f_arg)
    for arg in args:
        print("another arg through *args :", arg)
    for key, value in kwargs.items():
        print("another arg through **kwargs : {}={}".format(key,value))

test_var_args("hola","adios",cosa="pueseso")

parser = argparse.ArgumentParser(description='Process some stuff')

parser.add_argument('command',
                    help='Commands to execute',
                    nargs='*',
                    choices=list(commands.keys()))

#parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
#parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')
args = parser.parse_args()
print(args.command)
#print(args.accumulate(args.integers))

for c in args.command:
    print(commands[c].split())
    subprocess.run(commands[c].split(), shell=True)

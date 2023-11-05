'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

argnumbers = len(sys.argv) - 1

if argnumbers == 2 :
    print("")
    print("Hasil dari penjumlahan " + str(calc.add2(str(sys.argv[1]), str(sys.argv[2]))))
    print("")
    sys.exit(0)

if argnumbers != 2 :
    print("")
    print("Anda memasukkan nilai " + str(argnumbers) + ".")
    print("")
    print("Penggunaan: 'add2vals X Y' dimana X dan Y adalah nilai individual.")
    print("       Jika add2vals tidak terdapat pada path, maka penggunaannya adalah './add2vals X Y'.")
    print("       Jika tidak terbundle, maka penggunaannya adalah 'python add2vals.py X Y'.")
    print("")
    sys.exit(1)

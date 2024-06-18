import timeit
import matplotlib.pyplot as plt
import numpy as np


def test_zip( foo, bar ):
    store = []
    for f, b in zip(foo, bar):
        #print(f, b)
        store.append( (f, b) )

def test_enumerate( foo, bar ):
    store = []
    for n, f in enumerate( foo ):
        #print(f, bar[n])
        store.append( (f, bar[n]) )

def test_count( foo, bar ):
    store = []
    count = 0
    for f in foo:
        #print(f, bar[count])
        store.append( (f, bar[count]) )
        count += 1

def test_indices( foo, bar, indices ):
    store = []
    for i in indices:
        #print(foo[i], bar[i])
        store.append( (foo[i], bar[i]) )

def test_existing_list_indices( foo, bar ):
    store = []
    for f in foo:
        #print(f, bar[f])
        store.append( (f, bar[f]) )


list_sizes = [ 10, 100, 1000, 10000, 100000, 1000000 ]
tz = []
te = []
tc = []
ti = []
tii= []

tcz = []
tce = []
tci = []
tcii= []

for a in list_sizes:
    foo = [ i for i in range(a) ]
    bar = [ i for i in range(a) ]
    indices = [ i for i in range(a) ]
    reps = 1000

    tz.append( timeit.timeit( 'test_zip( foo, bar )',
                              'from __main__ import test_zip, foo, bar',
                              number=reps
                              )
               )
    te.append( timeit.timeit( 'test_enumerate( foo, bar )',
                              'from __main__ import test_enumerate, foo, bar',
                              number=reps
                              )
               )
    tc.append( timeit.timeit( 'test_count( foo, bar )',
                              'from __main__ import test_count, foo, bar',
                              number=reps
                              )
               )
    ti.append( timeit.timeit( 'test_indices( foo, bar, indices )',
                              'from __main__ import test_indices, foo, bar, indices',
                              number=reps
                              )
               )
    tii.append( timeit.timeit( 'test_existing_list_indices( foo, bar )',
                               'from __main__ import test_existing_list_indices, foo, bar',
                               number=reps
                               )
                )

    tcz.append( timeit.timeit( '[(f, b) for f, b in zip(foo, bar)]',
                               'from __main__ import foo, bar',
                               number=reps
                               )
                )
    tce.append( timeit.timeit( '[(f, bar[n]) for n, f in enumerate( foo )]',
                               'from __main__ import foo, bar',
                               number=reps
                               )
                )
    tci.append( timeit.timeit( '[(foo[i], bar[i]) for i in indices ]',
                               'from __main__ import foo, bar, indices',
                               number=reps
                               )
                )
    tcii.append( timeit.timeit( '[(f, bar[f]) for f in foo ]',
                                'from __main__ import foo, bar',
                                number=reps
                                )
                 )

print( f'te  = {te}' )
print( f'ti  = {ti}' )
print( f'tii = {tii}' )
print( f'tc  = {tc}' )
print( f'tz  = {tz}' )

print( f'tce  = {te}' )
print( f'tci  = {ti}' )
print( f'tcii = {tii}' )
print( f'tcz  = {tz}' )

fig, ax = plt.subplots( 2, 2 )
ax[0,0].plot( list_sizes, te, label='enumerate()', marker='.' )
ax[0,0].plot( list_sizes, ti, label='index-list', marker='.' )
ax[0,0].plot( list_sizes, tii, label='element of foo', marker='.' )
ax[0,0].plot( list_sizes, tc, label='count()', marker='.' )
ax[0,0].plot( list_sizes, tz, label='zip()', marker='.')
ax[0,0].set_xscale('log')
ax[0,0].set_yscale('log')
ax[0,0].set_xlabel('List Size')
ax[0,0].set_ylabel('Time (s)')
ax[0,0].legend()
ax[0,0].grid( b=True, which='major', axis='both')
ax[0,0].grid( b=True, which='minor', axis='both')

ax[0,1].plot( list_sizes, np.array(te)/np.array(tz), label='enumerate()', marker='.' )
ax[0,1].plot( list_sizes, np.array(ti)/np.array(tz), label='index-list', marker='.' )
ax[0,1].plot( list_sizes, np.array(tii)/np.array(tz), label='element of foo', marker='.' )
ax[0,1].plot( list_sizes, np.array(tc)/np.array(tz), label='count()', marker='.' )
ax[0,1].set_xscale('log')
ax[0,1].set_xlabel('List Size')
ax[0,1].set_ylabel('Performances ( vs zip() function )')
ax[0,1].legend()
ax[0,1].grid( b=True, which='major', axis='both')
ax[0,1].grid( b=True, which='minor', axis='both')

ax[1,0].plot( list_sizes, tce, label='list comprehension using enumerate()',  marker='.')
ax[1,0].plot( list_sizes, tci, label='list comprehension using index-list()',  marker='.')
ax[1,0].plot( list_sizes, tcii, label='list comprehension using element of foo',  marker='.')
ax[1,0].plot( list_sizes, tcz, label='list comprehension using zip()',  marker='.')
ax[1,0].set_xscale('log')
ax[1,0].set_yscale('log')
ax[1,0].set_xlabel('List Size')
ax[1,0].set_ylabel('Time (s)')
ax[1,0].legend()
ax[1,0].grid( b=True, which='major', axis='both')
ax[1,0].grid( b=True, which='minor', axis='both')

ax[1,1].plot( list_sizes, np.array(tce)/np.array(tcz), label='enumerate()', marker='.' )
ax[1,1].plot( list_sizes, np.array(tci)/np.array(tcz), label='index-list', marker='.' )
ax[1,1].plot( list_sizes, np.array(tcii)/np.array(tcz), label='element of foo', marker='.' )
ax[1,1].set_xscale('log')
ax[1,1].set_xlabel('List Size')
ax[1,1].set_ylabel('Performances ( vs zip() function )')
ax[1,1].legend()
ax[1,1].grid( b=True, which='major', axis='both')
ax[1,1].grid( b=True, which='minor', axis='both')

plt.show()
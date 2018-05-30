# 2018710053 이상헌
import random

w0 = random.random()    # randomly initialization
w1 = random.random()
w2 = random.random()

n = 0.01     # learning rate = 0.01

print('[Initial point]\n', 'w0 =', w0,', w1 =', w1,', w2 =', w2)

print('\n[Iteration start]')
for i in range(1, 2000):    # iteration = 2000
    nw0 = w0
    nw1 = w1
    nw2 = w2
    w0 = w0 - n*(12*nw2 + 8*nw1 + 8*nw0 - 8)
    w1 = w1 - n*(20*nw2 + 12*nw1 + 8*nw0 - 10)
    w2 = w2 - n*(36*nw2 + 20*nw1 + 12*nw0 - 14)
    if i % 200 == 0 :
        print('iteration =',i, '// w0 =', w0,', w1 =', w1,', w2 =', w2)

print('\n[Result]\n', 'w0 =', round(w0, 10) ,', w1 =', round(w1, 10),', w2 =', round(w2, 10))
print('function f(x) =', w2, '* x^2 +', w1, '* x +',w0)
import  sys
import  time
# sys.stdout.write()

# for i in range(20):
#     sys.stdout.write('>')
#     sys.stdout.flush()
#     time.sleep(0.2)

n = 0
while n < 20:
    sys.stdout.write('>' ,)
    sys.stdout.flush()
    time.sleep(0.3)
    n += 1




conut = 0
print('#' * 20 ,end='')

while True:
    time.sleep(0.3)
    print('\r%s@%s' % ('#' * conut, '#' * (19 - conut)), end='')
    conut += 1
    if conut == 20:
         conut = 0
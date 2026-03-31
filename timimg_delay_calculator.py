
h = int(input())
m = int(input())
h1 = int(input())
m1 = int(input())
x = int(input())

def numberOfMinutesinTime(h, m):
	return h * 60 + m

n = numberOfMinutesinTime(h,m)

target = numberOfMinutesinTime(h1, m1)

n+=(x*60)
print(abs(target-n))
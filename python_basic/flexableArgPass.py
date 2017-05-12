def func(x, y=5, *a, **b):
    print x, y, a, b

func(1)
func(1,2)
func(1,2,3)
func(1,2,3,4,5,6,6,6,6,6,7,8)
func(x=1)
func(x=1,y=1)
func(x=1,y=1,a=1)
func(x=1,y=1,a=1,b=1)
func(1,y=1)
func(1,2,3,4,a=1)
func(1,2,3,4,k=1,t=2,o=4, f=3,l=4)


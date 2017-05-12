
import pickle
# save data
test_data = ['Save me!', 123.456, True]
f = file('test.data', 'w')
pickle.dump(test_data,f)
f.close()


# pick up data 
f = file('test.data')
test_data = pickle.load(f)
f.close()
print test_data
#save several objects at one time

a = 123
b='hello'
c =0.232
data = (a,b,c)
f = file('data', 'w')
pickle.dump(data,f)
f.close()

#other way
...
pickle.dump(a, f)
pickle.dump(b, f)
pickle.dump(c, f)
...
x = pickle.load(f)
y = pickle.load(f)
z = pickle.load(f)


dump 方法可以增加一个可选的参数，来指定用二进制来存储：

pickle.dump(data, f, True)

而 load 方法会自动检测数据是二进制还是文本格式，无需手动指定。


Python 还提供了另一个模块 cPickle，它的功能及用法和 pickle 模块完全相同，只不过它是用C语言编写的，因此要快得多（比pickle快1000倍）。因此你可以把上述代码中的 pickle 全部替换为 cPickle，从而提高运行速度（尽管在这个小程序中影响微乎其微）。

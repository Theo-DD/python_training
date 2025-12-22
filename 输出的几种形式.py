
num = 101
weight = 68
high = 1.81
bmi = weight/(high**2)
print(bmi)
print('代号',num,'的bmi指数为',bmi)
print('代号'+str(num)+'的bmi指数为','{:0.2f}'.format(bmi))
print('代号%s的bmi指数为%.4f' % (num,bmi))
print('代号{0}的bmi指数为{1}'.format(num,bmi))
print(f'代号{num}的bmi指数为{bmi}')




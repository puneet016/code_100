error_no=45457984738
name="John Doe"
print('hello,%s'%name)
print('hey %(name)s, your error no is %(error_no)d'%{'name':name,'error_no':error_no})



print('hello,{}'.format(name))
print('hey {name}, your error no is {error_no}'.format(name=name,error_no=error_no))
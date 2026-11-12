guests=['ravi','sita','ravi','amit','sita']
emp_lst=[]
for x in guests:
    if x in emp_lst:
        pass
    else:
        emp_lst.append(x)
print(emp_lst)
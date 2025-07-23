def my_func(f_name, l_name, age):
    print(f"my name is {f_name} {l_name}. I am {age} years old.")
my_func(f_name="shahriar", l_name="rashid", age=25)


#arbitary number of keywords

def my_func(**data):
    print(data)
    print(f"my name is {data['f_name']} {data['l_name']}.I am {data['age']} years old.I got {data['Marks']} out of 100.I live in {data['Address']}")
my_func(f_name="shahriar", l_name="rashid", age=25, Marks = "96%", Address = 'Dhaka')


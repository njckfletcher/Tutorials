example = ['left', 'right', 'up', 'down']

#= OLD METHOD ==================================================================
# for i in range(len(example)):
#     print(i, example[i])
#===============================================================================
    
# i = index, j = object
#for i, j in enumerate(example):
#    print(i, j)

new_dict = dict(enumerate(example))

#print(new_dict)

#[print(i, j) for i, j in enumerate(new_dict)]

another_dict = {'Hello': 'Why, hello there!', 'Bye': 'See you later!'}

[print(i, j) for i, j in enumerate(another_dict)]
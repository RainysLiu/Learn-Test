import os
import random

dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '爱情')

file_list = os.listdir(dir)

# for file in file_list:
#     file_path = os.path.join(dir, file)
#     with open(file_path, 'r', encoding='utf-8') as f:
#         context = f.read()
#         new_context = context.replace('。', '。\n')
#         print(new_context)
#     with open(file_path, 'w', encoding='utf-8') as f:
#         f.write(new_context)

file = random.choice(file_list)

file_path = os.path.join(dir, file)
with open(file_path, 'r', encoding='utf-8') as f:
    context = f.read()
    new_context = context.replace('。', '。\n')
    print(new_context)
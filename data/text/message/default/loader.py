from os import sep

with open(f"data{sep}text{sep}message{sep}default{sep}answer_simple_message.txt") as file:
    answer_simple_message = file.read()

with open(f"data{sep}text{sep}message{sep}default{sep}answer_forward_simple.txt") as file:
    answer_forward_simple = file.read()
with open(f"data{sep}text{sep}message{sep}default{sep}answer_photo_simple.txt") as file:
    answer_photo_simple = file.read()

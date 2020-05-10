"""
while
"""
# flag = True
# while flag:
#     userinput = input() # 標準入力
#     if userinput == 'exit':
#         flag = False

while True:
    print('入力してください')
    user_input = input()
    if user_input == 'exit':
        break
    elif user_input == 'skip':
        continue
    print('あなたの入力は：' + user_input + 'でした')

    
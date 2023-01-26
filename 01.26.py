def check(input_str):
  char_count = 0
  digit_count = 0
  symbol_count = 0

  for char in input_str:
    if char.isalpha():
      char_count += 1
    elif char.isdigit():
      digit_count += 1
    else:
      symbol_count += 1
  
  return (char_count, digit_count, symbol_count)

input_str = "dsgs@$@#_snow"
char_count, digit_count, symbol_count = check(input_str)
print(f"char : {char_count}, digit : {digit_count}, symbol : {symbol_count}")

sample_list = [11, 22, 33, 55, 66]

# 주어진 리스트의 4번째 자리에 있는 항목을 제거하고 변수에 할당해주세요.

x = sample_list.pop(3)
print(x)
print(sample_list)

#sample_list의 가장 뒤에 77을 추가해보세요
sample_list.append(77)

#할당해놓은 변수의 값을 sample_list의 2번 index에 추가해보세요.

print(sample_list)
sample_list.insert(2, x)
print(sample_list)

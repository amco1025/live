def ko_hello(name) :
  print(f'안녕하세요, {name},님!')
  print('^~^//')

def en_hello(name):
  print(f'Hello, {name}!')
  print('^~^//')

ko_hello('aiden')
en_hello('aiden')

def ko_hello(name) :
  print(f'안녕하세요, {name}님!')

def en_hello(name):
  print(f'Hello, {name}!')

def add_emoji(name, func):
  func(name)
  print("^~^//")

add_emoji('aiden', ko_hello)
add_emoji('aiden', en_hello)

def emoji_decorator(func):
  def wrapper(name):
    func(name)
    print('^~^//')

    return wrapper

def ko_hello(name) :
  print(f'안녕하세요, {name}님!')

new_func = emoji_decorator(ko_hello)
new_func('aiden')
(emoji_decorator(ko_hello))('aiden')

def emoji_decorator(func):
  def wrapper(name):
    func(name)
    print('^~^//')

    return wrapper

def en_hello(name):
  print(f'Hello, {name}!')

new_func = emoji_decorator(en_hello)
new_func('aiden')

def emoji_decorator(func):
  def wrapper(name):
    func(name)
    print('^~^//')

    return wrapper

@emoji_decorator
def ko_hello(name) :
  print(f'안녕하세요, {name}님!')

@emoji_decorator
def en_hello(name):
  print(f'Hello, {name}!')

ko_hello('aiden')
  
  
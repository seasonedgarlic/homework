calls = 0

def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    i = (len(string), string.upper(), string.lower())
    return i
def is_contains(string, list_to_search):
    count_calls()
    for _ in list_to_search:
        if string.upper() in _.upper():
            return True
    for _ in list_to_search:
        if string.lower() not in _.lower():
            return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

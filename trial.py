import time
import pprint
meridian = time.strftime('%p')
hour_now = time.strftime('%I')

if meridian.lower() == 'am': 
    greetings = 'Good morning.'
else:
    afternoon_list = [12, 1, 2, 3]
    if hour_now in afternoon_list:
        greetings = 'Good afternoon.'
    else:
        greetings = 'Good evening.'

# print("""     """, greetings)
time.sleep(0.5)

# def common_letters(phrase: str, desired_characters: str) -> str:
#     """Function prints common letters between the given variables."""
#     return set(phrase).intersection(set(desired_characters))
# pprint.pprint(sorted(common_letters("We can't miss our graduation.", 'aeiou')))


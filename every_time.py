from flask import Flask

app = Flask(__name__)

@app.route('/')
def cal() -> int:
    name = input('Enter your name: ')
    sex = input('What is your sex? ')
    if sex.lower() == 'male':
        prefix = 'Mr'
    else:
        prefix = 'Mrs'
    year_of_birth = int(input('Enter your year of birth: '))
    age = 2022 - year_of_birth
    comment = '{} {} you are {} years old'.format(prefix, name, age)
    return comment

app.run()

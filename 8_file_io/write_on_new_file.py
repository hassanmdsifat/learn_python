user_data = [
    {
        'file_name': 'user_1.txt',
        'context': "Hello This is from User 1"
    },
    {
        'file_name': 'user_2.txt',
        'context': "Hello This is from User 2"
    },
    {
        'file_name': 'user_3.txt',
        'context': "Hello This is from User 3"
    }
]

with open('test_file_2.txt', 'w') as file:
    file.write("This is a test")
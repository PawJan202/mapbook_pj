users: list = [
    {'username': 'Oliwia', 'location': 'Ryki', 'posts': 1,
     'usermessage': ['zyczenia1', 'Kocham Legie', 'Sprzedam Opla', 'kiwi']},
    {'username': 'Paweł', 'location': 'Ostróda', 'posts': 2,
     'usermessage': ['zyczenia2', 'Kocham Legie1', 'Sprzedam Opla1']},
    {'username': 'Eliza', 'location': 'Radom', 'posts': 3, 'usermessage': ['zyczenia3', 'Kocham Legie2']},
    {'username': 'Filip', 'location': 'Dęblin', 'posts': 4,
     'usermessage': ['zyczenia4', 'Kocham Legie3', 'Sprzedam Opla3', 'kiwi3']},
]


def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f'Twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')


read_data(users[1:])
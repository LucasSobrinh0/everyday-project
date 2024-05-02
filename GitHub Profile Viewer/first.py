import requests


def search(user):
    url = f"https://api.github.com/users/{user}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        name = data['name']
        bio = data['bio']
        followers = data['followers']
        repositories = data['public_repos']
        created = data['created_at']
        return (f"Name:{name}\n"
                f"Bio:{bio}\n"
                f"Followers:{followers}\n"
                f"Repositories:{repositories}\n"
                f"Created:{created}")


def main():
    user = str(input("Enter a GitHub username: "))
    result = search(user)
    print(result)


if __name__ == '__main__':
    main()

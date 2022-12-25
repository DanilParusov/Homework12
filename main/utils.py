import json
from json import JSONDecodeError

class Post:
    def __init__(self, path):
        self.path = path

    def get_posts(self):
        try:
            with open(self.path, 'r', encoding='UTF-8') as file:
                posts = json.load(file)
        except JSONDecodeError:
            print("Ошибка при загрузке json файла")

        return posts

    def get_posts_by_word(self, word):
        posts = []
        for post in self.get_posts():
            if word.lower() in post["content"].lower():
                posts.append(post)
        return posts

    def save_posts(self, posts):
        with open(self.path, 'w', encoding='UTF-8') as file:
            json.dump(posts, file)

    def add_post(self, post):
        all_posts = self.get_posts()
        all_posts.append(post)
        self.save_posts(all_posts)
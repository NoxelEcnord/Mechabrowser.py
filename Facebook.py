from bs4 import BeautifulSoup
import mechanicalsoup
import urllib.request
import requests

class Facebook:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.browser = mechanicalsoup.StatefulBrowser()

    def login(self):
        login_url = "https://www.facebook.com/login"
        self.browser.open(login_url)
        self.browser.select_form('#login_form')
        self.browser["email"] = self.email
        self.browser["pass"] = self.password
        self.browser.submit_selected()

        # Check if login is successful by checking the response URL
        if self.browser.get_url() != login_url:
            print("Login Successful!")
        else:
            print("Login Failed!")

class Login(Facebook):
    def __init__(self, email, password):
        super().__init__(email, password)

    def prompt_login(self):
        self.login()

class ViewPost(Facebook):
    def __init__(self, email, password):
        super().__init__(email, password)

    def view_post(self, post_id):
        post_url = f"https://www.facebook.com/{post_id}"
        self.browser.open(post_url)
        # Do something with the post content

    def download_images(self, post_id):
        post_url = f"https://www.facebook.com/{post_id}"
        self.browser.open(post_url)
        soup = BeautifulSoup(self.browser.get_page(), "html.parser")
        image_tags = soup.find_all("img")
        for i, image in enumerate(image_tags):
            image_url = image["src"]
            urllib.request.urlretrieve(image_url, f"image{i+1}.jpg")

    def reply_post(self, post_id, reply_content):
        post_url = f"https://www.facebook.com/{post_id}"
        self.browser.open(post_url)
        self.browser.select_form('#composer_form')
        self.browser["comment_text"] = reply_content
        self.browser.submit_selected()

    def like_post(self, post_id):
        post_url = f"https://www.facebook.com/{post_id}"
        self.browser.open(post_url)
        # Like the post using appropriate form submission

class Messaging(Facebook):
    def __init__(self, email, password):
        super().__init__(email, password)

    def view_messages(self):
        messages_url = "https://www.facebook.com/messages"
        self.browser.open(messages_url)
        # Do something with the messages content

    def reply_message(self, message_id, reply_content):
        reply_url = f"https://www.facebook.com/messages/t/{message_id}"
        self.browser.open(reply_url)
        self.browser.select_form('#composer_form')
        self.browser["message_text"] = reply_content
        self.browser.submit_selected()

class Profile(Facebook):
    def __init__(self, email, password):
        super().__init__(email, password)

    def upload_profile_pic(self, image_path):
        upload_url = "https://www.facebook.com/profile_picture"
        self.browser.open(upload_url)
        self.browser.select_form('#facebook-upload-form')
        self.browser.choose_file('pic', image_path)
        self.browser.submit_selected()

    def download_profile_pic(self, user_id):
        pic_url = f"https://www.facebook.com/{user_id}/picture"
        urllib.request.urlretrieve(pic_url, "profile_pic.jpg")

    def edit_profile(self, profile_info):
        edit_url = "https://www.facebook.com/profile"
        self.browser.open(edit_url)
        self.browser.select_form('#edit_profile_form')
        # Fill in the profile_info dictionary into the form fields
        self.browser.submit_selected()

    def view_profile(self, user_id):
        profile_url = f"https://www.facebook.com/{user_id}"
        self.browser.open(profile_url)
        # Do something with the profile content

    def view_friends_list(self, user_id):
        friends_url = f"https://www.facebook.com/{user_id}/friends"
        self.browser.open(friends_url)
        # Do something with the friends list content

class Friend(Facebook):
    def __init__(self, email, password):
        super().__init__(email, password)

    def view_friend_profile(self, friend_id):
        friend_url = f"https://www.facebook.com/{friend_id}"
        self.browser.open(friend_url)
        # Do something with the friend's profile content

    def view_friends_list(self, friend_id):
        friends_url = f"https://www.facebook.com/{friend_id}/friends"
        self.browser.open(friends_url)
        # Do something with the friend's friends list content

    def download_friend_pic(self, friend_id):
        pic_url = f"https://www.facebook.com/{friend_id}/picture"
        urllib.request.urlretrieve(pic_url, "friend_pic.jpg")

class Page(Facebook):
    def __init__(self, email, password):
        super().__init__(email, password)

    def save_page(self, page_id):
        page_url = f"https://www.facebook.com/{page_id}"
        self.browser.open(page_url)
        page_html = self.browser.get_page()
        with open("page.html", "w") as file:
            file.write(page_html)

    def view_page(self, page_id):
        page_url = f"https://www.facebook.com/{page_id}"
        self.browser.open(page_url)

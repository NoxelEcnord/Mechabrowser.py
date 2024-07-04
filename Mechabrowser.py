import mechanicalsoup
import urllib.parse
import os
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as soup

class Mechabrowser:
    def __init__(self):
        self.browser = mechanicalsoup.StatefulBrowser()
        from bs4 import BeautifulSoup
        from bs4 import BeautifulSoup as soup

    def click(self, name):
        self.browser.click(name)
    def follow(self,link,state="1"):
        try:
            return self.browser.follow_link(link)
        except mechanicalsoup.utils.LinkNotFoundError as e:
            print ("can't follow a non existent link. please make sure the link is existant\n\n",e)

    def open(self,url,state='true'):
        url_=url
        if url_[0] !='h' and url_[2] !='t' and 'http' not in url_:
            if 'ins' in state or 'alse' in state:
                url='http://'+url_
                return self.browser.open(url)
            if 'rue' in state :
                url='http://'+url_
                return self.browser.open(url)
            if 'one' in state:
                url=url_
                return self.browser.open(url)
            else:
                url=url
                print("url may be invalid")
                return self.browser.open(url)
      #  return response.Response

    def type(self, text, field_name):
        self.browser.get_current_page().find("input", {"name": field_name})["value"] = text

    def submitfoirm(self):
      return  self.browser.submit_selected()
       # return response.Response

    def details(self):
        current_page = self.browser.get_current_page()
        #user_agent = self.browser.get("User-Agent")
        cookies = self.browser.session.cookies.get_dict()
        url = self.browser.get_url()
        # Additional information can be extracted based on your requirements
        return cookies, url

    def downloadpage(self):
        current_page = self.browser.get_current_page()
        with open(os.path.expanduser('~/page.html'), 'w') as file:
            file.write(str(current_page))

    def downloadfile(self, link):
        response = self.browser.open(link)
        content = response.content
        # Save content to local file
        file_name = os.path.basename(urllib.parse.urlparse(link).path)
        with open(os.path.join(os.path.expanduser('~'), file_name), 'wb') as file:
            file.write(content)
       # return response.Response

    def clickbutton(self, btn):
        button = self.browser.get_current_page().find("button", text=btn)
        return  self.browser.open(button.attrs['onclick'])
      #  return response.Response

    def fullpage(self):
        current_page = self.browser.get_current_page()
        return current_page.get_text(),self.browser.page()

    def showlinks(self):
        links = self.browser.get_current_page().find_all("a")
        for link in links:
            print(link.get('href'))

    def out_links(self, file_name):
        links = self.browser.get_current_page().find_all("a")
        with open(file_name, 'w') as file:
            for link in links:
                file.write(link.get('href') + '\n')

    def showform(self,n=0):
        self.browser.select_form(nr=n)
        return self.browser.form.print_summary()

    def fill(self,x,y):
        self.browser[str(x)]=str(y)
        return self.browser.form.print_summary()


    def forcenew(self,tag,name,value,**kwargs):
        self.browser.form.new_control(tag,name,value,**kwargs)

    def forcefill(self,name,value):
        self.browser.form.set(name,value,False)

    def url(self):
        return self.browser.get_url()

    def post(self, url, payload):
        self.browser.open(url, method='POST', data=payload)
        return self.browser.get_current_page(),repomse.Response

    def get(self, url, payload=None):
        self.browser.open(url)
        return self.browser.get_current_page()

    def list_forms(self):
        forms = self.browser.get_current_page().find_all("form")
        for i, form in enumerate(forms):
            print("#"*10+f"Form #{i}"+"#"*10)
            print("|","'''''"*28+"|")
            print(form)
            print("\n\n")
            print("|",",,,,,,"*28+"|")
            print("-"*30)

    def select_form(self, n=0):
        self.browser.select_form(nr=n)

    def page_out(self, file_name):
        current_page = self.browser.get_current_page()
    def fill(self,x,y):
        self.browser[str(x)]=str(y)
        return self.browser.form.print_summary()
    def sub_form(self,n=0):
        self.browser.select_form(n)
        self.browser.submit_selected()


    def forcenew(self,tag,name,value,**kwargs):
        self.browser.form.new_control(tag,name,value,**kwargs)
        return self.browser.form.print_summary()

    def forcefill(self,name,value):
        self.browser.form.set(name,value,False)
        return self.browser.form.print_summary()



    def post(self, url, payload):
        self.browser.open(url, method='POST', data=payload)
        return self.browser.get_current_page(),repomse.Response

    def get(self, url, payload=None):
        self.browser.open(url)
        return self.browser.get_current_page()
    def plainpage(self):
        return BeautifulSoup(self.browser.get_current_page(),"html.parser")

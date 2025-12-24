import time
from math import trunc


from playwright.sync_api import Page

def test_PLaywright(playwright):
    print("test cases playwright")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  #context is opening browser in incognito mode(separate browsing window)
                           #each instance will have its separate instance opening
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

    # playwright.firefox.launch(headless=False)
    # playwright.webkit.launch(headless=False)
    # playwright.chromium.launch(headless=True)
    # playwright.firefox.launch(headless=True)
    # playwright.webkit.launch(headless=True)


#page ficture chromium engine headless mode on single context
def test_Shortcut(page: Page):
    page.goto("https://rahulshettyacademy.com")
    page.get_by_role("button", name="Login").click()



def test_Login(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("Consultant")
    #page.locator("checkmark").click()
    #page.get_by_role("checkbox", name="terms").click()
    page.locator("#terms").click()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button").click()
    time.sleep(5)


def test_WebsiteCheck(page: Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.locator("#userEmail").fill("rahulshettyacademy")


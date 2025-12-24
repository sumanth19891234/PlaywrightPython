import time
from math import trunc


from playwright.sync_api import Page, Playwright,expect
from pytest_playwright.pytest_playwright import browser


def test_Login(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning12")
    page.get_by_role("combobox").select_option("Consultant")
    page.locator("#terms").click()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_enabled()
    #Incorrect username/password.

    time.sleep(5)


def test_WebsiteCheck(playwright:Playwright):
    firefoxBrowser= playwright.firefox
    browser= firefoxBrowser.launch(headless=False)
    page= browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("Consultant")
    page.locator("#terms").click()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button").click()

def test_Login_CardSelection(page: Page):
    # iphone x, Blackberry
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("Consultant")
    page.locator("#terms").click()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button").click()

    iphoneProduct= page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    time.sleep(5)
    nokiaProduct= page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    time.sleep(5)
    page.get_by_text("Checkout").click()
    expect(page.locator(".media")).to_have_count(2)
    time.sleep(5)

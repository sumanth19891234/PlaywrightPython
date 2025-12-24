import time
from math import trunc


from playwright.sync_api import Page, Playwright,expect
from pytest_playwright.pytest_playwright import browser


def test_ChildWindowHandle(page: Page):
    # iphone x, Blackberry
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # python closure -
    with page.expect_popup() as popup_info:
        time.sleep(5)
        page.locator(".blinkingText[href='https://rahulshettyacademy.com/documents-request']").click()
        child_Page=popup_info.value
        time.sleep(5)
        text=child_Page.locator(".red").text_content()
        print(text)
        words=text.split("at")
        email=words[1].strip().split(" ")[0]
        print(email)
        assert email=="mentor@rahulshettyacademy.com"


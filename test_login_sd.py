from playwright.sync_api import Page, expect
import pytest
from time import sleep

import allure

creds = [("standard_user","secret_sauce"),
         ("problem_user","secret_sauce"),
         ("performance_glitch_user","secret_sauce"),
         ("error_user","secret_sauce"),
         ("visual_user","secret_sauce")
         ]

@allure.title("Test Login pake beberapa credentials di website www.saucedemo.com")
@allure.description("Test dilakukan dengan 5 credentials yang disediakan oleh www.saucedemo.com.\n\nTest ini tidak menggunakan verifikasi dua langkah, capek. Setelah berhasil login, lalu memasukkan salah satu barang 'saucelabs back pack' ke keranjang \n\nTest ini cocok digunakan sebagai test regresi")
@allure.tag("Login", "pilih barang", "check out")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Lucy")
@allure.link("https://www.saucedemo.com/", name="Saucedemo")


@pytest.mark.parametrize("username,password",creds)
def test_login(page: Page, username, password):
    # === this is the login section ===
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder('Username').fill(username)
    page.get_by_placeholder('Password').fill(password)
    page.locator("//input[@id='login-button']").click()

    # === assertion when user reach inventory page === 
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory_title = page.locator("//span[@class='title']").text_content()
    assert inventory_title == "Products"
    sleep(1)

    # === add item to the cart ===
    page.locator("//button[@id='add-to-cart-sauce-labs-backpack']").click()
    page.locator("//a[@class='shopping_cart_link']").click()
    
    #  === assertion when user reach cart section ===
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    cart_title = page.locator("//span[@class='title']").text_content()
    assert cart_title=="Your Cart"
    sleep(1)

    # === user heading to first check out phase ===
    page.locator("//button[@id='checkout']").click()
    
    # === assertion when user reach the first check out phase ===
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    chx_out_step1 = page.locator("//span[@class='title']").text_content()
    assert chx_out_step1 == "Checkout: Your Information"
    sleep(1)

    #  === close the page and browser ===
    page.close()

"""
first, run the code by typing 'pytest tets_login_sd.py --alluredir=./laporan-allure' to fetch the test result and the report that will be stored in a folder named 'laporan-allure'.

second, type 'allure serve ./laporan-allure' to show the report dashboard. klo gak jalan, mungkin tuan/puan belum install allure-nya wkwkwkwk 
"""
from RegistrPage import SearchHelper
import random
import time

def test_fill_form(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.first_name("Candidate")
    main_page.last_name("Best")
    main_page.email("mymail@type.com")
    main_page.gender()
    num = ''
    for i in range(10):
        num += str(random.randint(0, 9))
    main_page.number(num)
    main_page.date_of_birth()
    main_page.year_of_birth()
    main_page.month_of_birth()
    main_page.day_of_birth()
    main_page.subjects("Maths")
    main_page.hobby()
    main_page.picture("D:\Games\DnD\Parton.jpg")
    main_page.address("State, City, Street, house, flat")
    main_page.state_1()
    main_page.state_2()
    main_page.city_1()
    main_page.city_2()
    main_page.submit()
    time.sleep(5)

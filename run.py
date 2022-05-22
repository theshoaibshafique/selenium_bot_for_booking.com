from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency="USD")
    bot.select_place_to_go("New York")
    bot.select_dates(check_in_date="2022-05-20", check_out_date="2022-05-28")
    bot.select_adults(1)
    bot.click_search()
    bot.apply_filtrations()

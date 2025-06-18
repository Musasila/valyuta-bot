# import requests
# from pprint import pprint
#
# # API kalitingizni shu yerga yozing
# API_KEY = '4084878a71ce148a27278f49'
#
# # API manzili (EUR -> GBP konversiyasi)
# url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/UZS'
#
# # So‘rov yuborish
# response = requests.get(url)
#
# # Status kodni tekshirish
# print("Status kodi:", response.status_code)
#
# # Agar so‘rov muvaffaqiyatli bo‘lsa, natijani chiqarish
# if response.status_code == 200:
#     data = response.json()
#     pprint(data)
# else:
#     print("Xatolik yuz berdi. Tekshirib ko‘ring: API kalit va URL to‘g‘riligini.")
#
#     print(response.json()['conversion_rate'])
#
from zhdate import ZhDate

lunarDate = ZhDate(2024, 5, 5)
print(lunarDate)  #農曆

solarDate = lunarDate.to_datetime()
print(solarDate)  #國曆

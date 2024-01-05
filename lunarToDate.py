from zhdate import ZhDate
# zhdate is limited to before 2100 AD.

def lunarDateToDate(year, lunar_month, lunar_day):
	lunarDate = ZhDate(year, lunar_month, lunar_day)
	print(lunarDate)  #農曆

	solarDate = lunarDate.to_datetime()
	print(solarDate)  #國曆
	return solarDate


def create_google_calendar(Subject, Start_Date, All_Day_Event, Start_Time, End_Time, Location, Description):
	return


lunarDateToDate(2024,5,5)

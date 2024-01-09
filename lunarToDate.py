# zhdate is limited to before 2100 AD.
# https://github.com/CutePandaSh/zhdate/tree/master
from zhdate import ZhDate

def lunarDateToDate(year, lunar_month, lunar_day):
	lunarDate = ZhDate(year, lunar_month, lunar_day)
	print(lunarDate)  #農曆

	solarDate = lunarDate.to_datetime()
	print(solarDate)  #國曆
	return solarDate


def create_google_calendar(Subject, Start_Date, End_Date, isAll_Day_Event, Start_Time, End_Time, Location, Description,isPrivate):
	print (Subject + "," + Start_Time)
	return


solarDate = lunarDateToDate(2024,5,5)
print(solarDate.Date)


create_google_calendar("test", "2024/5/10", "2024/5/10", False, "12:00 PM", "01:30 PM", "Taipei","No", True)

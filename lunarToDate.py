# zhdate is limited to before 2100 AD.
# https://github.com/CutePandaSh/zhdate/tree/master
from zhdate import ZhDate

SUBJECT = "input your subject"
REPEAT_NUMBER = 20
IS_ALL_DAY_EVENT = False
START_LUNAR_DAY = {
		"year" : 2023,
		"month" : 5,
		"day" : 5
	}

START_TIME = {
		"hour" : 6,
		"minute" : 30,
		"midday" : "AM" # AM or PM
	}

END_TIME = {
		"hour" : 6,
		"minute" : 30,
		"midday" : "AM" # AM or PM
	}

LOCATION = "台北市"

DESCRIPTION = ""

IS_Private_SCHEDULE = True



def lunarDateToDate(year, lunar_month, lunar_day):
	lunarDate = ZhDate(year, lunar_month, lunar_day)
	print(lunarDate)  #農曆

	solarDate = lunarDate.to_datetime()
	print(solarDate)  #國曆
	return solarDate


def create_google_calendar(Subject, Start_Date, End_Date, isAll_Day_Event, Start_Time, End_Time, Location, Description,isPrivate):
	print (Subject + "," + Start_Time)
	return


solarDate = lunarDateToDate(START_LUNAR_DAY["year"], START_LUNAR_DAY["month"], START_LUNAR_DAY["day"])
print(solarDate)


create_google_calendar("test", "2024-5-10", "2024-5-10", False, "12:00 PM", "01:30 PM", "Taipei","No", True)

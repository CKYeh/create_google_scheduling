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

GOOGLE_CALENDAR_TITLE = ["Subject", "Start Date", "Start Time", "End Date", \
	"End Time", "All Day Event", "Description", "Private", "Location"]


def lunarDateToDate(year, lunar_month, lunar_day):
	lunarDate = ZhDate(year, lunar_month, lunar_day)
	#print(lunarDate)  #農曆

	solarDate = lunarDate.to_datetime()
	string_solor = str(solarDate)
	list_date = string_solor.split(" ")
	date = list_date[0]  # Date as 2024-12-30
	time = list_date[1]  # Time 00:00:00
	return date


def create_google_calendar(Subject, Start_Date, End_Date, isAll_Day_Event, Start_Time, End_Time, Location, Description,isPrivate):
	string = str(Subject + ",")
	string = string + str(Start_Date + "," + Start_Time + "," + Subject + ",")
	string = string + str(End_Date + "," + End_Time + ",")
	string = string + str(str(isAll_Day_Event) + "," + Description + ",")
	string = string + str(str(isPrivate) + "," + Location + "\r\n")
	return string

f = open("schedule.csv", "w")
google_calendar_title = ', '.join(GOOGLE_CALENDAR_TITLE)
f.write(google_calendar_title + str("\r\n"))


for i in range(REPEAT_NUMBER):
	solarDate = lunarDateToDate(START_LUNAR_DAY["year"] + i, START_LUNAR_DAY["month"], START_LUNAR_DAY["day"])
	schedule = create_google_calendar(SUBJECT, solarDate, solarDate, IS_ALL_DAY_EVENT, "12:00 PM", "01:30 PM", LOCATION, DESCRIPTION, IS_Private_SCHEDULE)
	print (schedule, end = "")
	f.write(schedule)


print ("schedule.csv file created.")
f.close()

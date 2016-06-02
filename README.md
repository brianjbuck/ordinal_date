# ordinaldate

Holidays such as President's Day in the US usually fall on a scheduled pattern such as the: third Monday in February. Getting that date usually involves adding/subtracting `datetime.date` objects together (no fun!) or having to remind the intern to update the database of all the holidays and their dates this year. If they forget then someone has to track down that one table that nobody remembers and sometimes a whole day is lost just because nobody made it simple (booo!). There must be a better way!

    >>> import ordinaldate
    >>> presidents_day = ordinaldate.get_by_values(
            ordinaldate.Ordinal.third,
            ordinaldate.Weekday.Monday,
            ordinaldate.Month.February,
            year=date.today().year
        )
    >>> presidents_day
    datetime.date(2016, 2, 15)

That's pretty good! But is still kind of chatty. It would be nice if I could just get the date directly. There must be a better way!

    >>> from ordinaldate import ordinaldate
    >>> presidents_day = ordinaldate.third.monday.february
    >>> presidents_day
    datetime.date(2016, 2, 15)

Now we're getting somewhere! Let's try another one!

    >>> kentucky_derby = ordinaldate.first.saturday.may
    >>> kentucky_derby
    datetime.date(2016, 5, 7)

How about this one?

    >>> memorial_day = ordinaldate.last.monday.may
    >>> memorial_day
    datetime.date(2016, 5, 30)

Nice one!

# Requirements

`ordinaldate` only requires [Enum34](https://pypi.python.org/pypi/enum34/ "Enum34 at PyPI") which is available for all versions of Python from 2.4-3.5.

`ordinaldate` was developed and has only been tested under Python3.5 but other than the requirement for Enum34 there is nothing special that should prevent it from running on Python2x.


# API

Ordinal:
- first
- second
- third
- fourth
- fifth
- last

Weekday:
- Monday
- Tuesday
- Wednesday
- Thursday
- Friday
- Saturday
- Sunday

Month:
- January
- February
- March
- April
- May
- June
- July
- August
- September
- October
- November
- December

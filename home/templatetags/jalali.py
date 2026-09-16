import jdatetime
from django import template

register = template.Library()

@register.filter
def jalali_date(value):
    if not value:
        return ''
    date = jdatetime.datetime.fromgregorian(date=value)

    months = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]
    return f"{date.year}/{months[date.month - 1]}/{date.day}, " + (f"{date.hour}:{date.minute}:{date.second}" if date.hour and date.minute and date.second else '')
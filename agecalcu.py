import streamlit as st
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import calendar

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Advanced Age Calculator",
    page_icon="🎂",
    layout="centered"
)

st.title("🎂 Advanced Age Calculator")
st.write("Calculate your age with extra insights.")

today = date.today()

# -------------------------
# Date Input
# -------------------------
dob = st.date_input(
    "📅 Select Your Date of Birth",
    min_value=date(1900,1,1),
    max_value=today
)

# -------------------------
# Functions
# -------------------------
def zodiac_sign(day, month):
    signs = [
        ("Capricorn",1,19),("Aquarius",2,18),("Pisces",3,20),
        ("Aries",4,19),("Taurus",5,20),("Gemini",6,20),
        ("Cancer",7,22),("Leo",8,22),("Virgo",9,22),
        ("Libra",10,22),("Scorpio",11,21),("Sagittarius",12,21),
        ("Capricorn",12,31)
    ]

    if month == 1 and day <= 19:
        return "Capricorn"

    previous = "Capricorn"

    for sign, m, d in signs:
        if (month == m and day <= d):
            return previous
        previous = sign

    return "Capricorn"

# -------------------------
# Button
# -------------------------
if st.button("🎉 Calculate Age"):

    age = relativedelta(today, dob)

    total_days = (today - dob).days
    total_hours = total_days * 24

    birthday_day = calendar.day_name[dob.weekday()]

    leap = calendar.isleap(dob.year)

    zodiac = zodiac_sign(dob.day, dob.month)

    next_birthday = date(today.year, dob.month, dob.day)

    if next_birthday < today:
        next_birthday = date(today.year + 1, dob.month, dob.day)

    countdown = (next_birthday - today).days

    st.success("Age Calculated Successfully!")

    st.metric("📅 Current Year", today.year)

    st.markdown("---")

    st.subheader("🎂 Your Age")

    col1, col2, col3 = st.columns(3)

    col1.metric("Years", age.years)
    col2.metric("Months", age.months)
    col3.metric("Days", age.days)

    st.markdown("---")

    st.subheader("📊 More Information")

    st.write(f"📆 **Total Days Lived:** {total_days:,}")

    st.write(f"⏰ **Approx. Hours Lived:** {total_hours:,}")

    st.write(f"🎈 **Birthday Day:** {birthday_day}")

    st.write(f"♈ **Zodiac Sign:** {zodiac}")

    st.write(f"🌍 **Birth Year Leap Year:** {'Yes ✅' if leap else 'No ❌'}")

    st.write(f"🎉 **Next Birthday In:** {countdown} days")

    st.balloons()
import streamlit as st
import requests

st.set_page_config(page_title="Azan Timings", page_icon="🕌")
st.title("🕌 Azan Timings for Any City in the World")
st.markdown("Select your **country** and **city** to see today's prayer times 🌙")

# Country & City Mapping (you can add more)
country_city_map = {
    "Pakistan": ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"],
    "Saudi Arabia": ["Makkah", "Madinah", "Riyadh", "Jeddah"],
    "India": ["Delhi", "Mumbai", "Hyderabad", "Kolkata"],
    "United Kingdom": ["London", "Manchester", "Birmingham"],
    "United States": ["New York", "Los Angeles", "Chicago", "Houston"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah"]
}

# Select Country
country = st.selectbox("🌍 Select Country", list(country_city_map.keys()))

# Select City based on Country
city = st.selectbox("🏙️ Select City", country_city_map[country])

# Button
if st.button("Get Azan Timings"):
    try:
        url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
        response = requests.get(url)
        data = response.json()

        if data['code'] == 200:
            timings = data['data']['timings']
            readable_date = data['data']['date']['readable']
            hijri_date = data['data']['date']['hijri']['date']

            st.success(f"📅 Date: {readable_date} | 🕋 Hijri: {hijri_date}")
            st.subheader("🕰️ Today's Prayer Timings:")

            azan_emojis = {
                "Fajr": "🌄",
                "Dhuhr": "🌞",
                "Asr": "🌤️",
                "Maghrib": "🌇",
                "Isha": "🌙",
                "Sunrise": "🌅",
                "Midnight": "🌌"
            }

            for prayer, time in timings.items():
                emoji = azan_emojis.get(prayer, "🕐")
                st.write(f"{emoji} **{prayer}**: `{time}`")
        else:
            st.error("Something went wrong. Try a different city/country.")

    except Exception as e:
        st.error("Error fetching data. Please try again.")

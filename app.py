
import streamlit as st
import mylibrary
from data import ATTRACTIONS, ALL_CATEGORIES, TICKET_TYPES

# Website title
st.title("🎢 Mumu's Theme Park")
st.write("Your personal theme park attraction planner!")
st.divider()

# Plan your visit
st.subheader("🎟️ Plan Your Visit")

# Choose ticket type
ticket_type = st.radio("Ticket Type", TICKET_TYPES)

# Choose arrival time

# Choose arrival time
from datetime import time

arrival_options = [
    time(hour, minute)
    for hour in range(9, 22)
    for minute in [0, 30]
]

arrival_time = st.selectbox(
    "What time will you arrive?",
    arrival_options,
    format_func=lambda t: t.strftime("%H:%M")
)


# Choose visit duration

# Choose visit duration
visit_hours = st.selectbox(
    "How many hours will you stay?",
    list(range(1, 13)),
    index=3
)


# Choose attraction categories
st.subheader("🎡 Choose Your Attractions")
choices = st.multiselect("Choose Categories", ALL_CATEGORIES)

# Get recommendations
if st.button("Get Recommendations"):

    # Check if a category was selected
    if len(choices) == 0:
        st.warning("Please select at least one category.")
        st.stop()

    # Filter attractions by category
    recommendations = mylibrary.get_recommendations(
        ATTRACTIONS, choices
    )

    # Filter by arrival time and visit duration
    recommendations = mylibrary.filter_by_time(
        recommendations, arrival_time, visit_hours
    )

    # Check if attractions were found
    if len(recommendations) > 0:

        # Prepare the recommendation table
        rows = mylibrary.build_row(
            recommendations, ticket_type, arrival_time, visit_hours
        )

        # Sort attractions by next showtime
        rows.sort(key=lambda row: row["Next Show / Availability"])

        # Display recommendations
        st.subheader("⭐ Recommended Attractions")
        
        # Create a table with rows and columns
        import html

        table = """
        <table style="width:100%; border-collapse:collapse;">
            <tr>
                <th>Name</th>
                <th>Description</th>
                <th>Next Show / Availability</th>
                <th>Wait Time (min)</th>
            </tr>
        """

        for row in rows:
            table += "<tr>"
            table += "<td>" + html.escape(str(row["Name"])) + "</td>"
            table += "<td>" + html.escape(str(row["Description"])) + "</td>"
            table += "<td>" + html.escape(str(row["Next Show / Availability"])) + "</td>"
            table += "<td>" + html.escape(str(row["Wait Time"])) + "</td>"
            table += "</tr>"

        table += "</table>"

        st.markdown(table, unsafe_allow_html=True)


        # Check for scheduling conflicts
        conflicts = mylibrary.find_conflicts(rows)

        if len(conflicts) > 0:
            for time in conflicts:
                st.warning("Scheduling conflict at " + time)

    else:
        st.write("No attractions found for your selected visit time.")

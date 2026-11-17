
# Function 1: Filter attractions by category
def get_recommendations(attractions, choices):
    out = []

    for attraction in attractions:
        for category in attraction["category"]:
            if category in choices:
                out.append(attraction)
                break

    return out


# Function 2: Build recommendation table
def build_row(attractions, ticket_type, arrival_time, visit_hours):
    rows = []

    for attraction in attractions:
        next_time = "Anytime"

        if "times" in attraction:
            arrival_minutes = arrival_time.hour * 60 + arrival_time.minute
            departure_minutes = arrival_minutes + visit_hours * 60

            for hour in attraction["times"]:
                show_minutes = hour * 60

                if arrival_minutes <= show_minutes <= departure_minutes:
                    next_time = str(hour).zfill(2) + ":00"
                    break

        row = {
            "Name": attraction["name"],
            "Description": attraction["description"],
            "Next Show / Availability": next_time
        }

        if ticket_type == "Express":
            row["Wait Time"] = attraction.get("express_wait", "N/A")
        else:
            row["Wait Time"] = attraction.get("wait", "N/A")

        rows.append(row)

    return rows


# Function 3: Filter by visit time
def filter_by_time(attractions, arrival_time, visit_hours):
    available = []

    arrival_minutes = arrival_time.hour * 60 + arrival_time.minute
    departure_minutes = arrival_minutes + visit_hours * 60

    for attraction in attractions:
        if "times" in attraction:
            for hour in attraction["times"]:
                show_minutes = hour * 60

                if arrival_minutes <= show_minutes <= departure_minutes:
                    available.append(attraction)
                    break
        else:
            available.append(attraction)

    return available


# Function 4: Find scheduling conflicts
def find_conflicts(rows):
    conflicts = []
    seen_times = []

    for row in rows:
        show_time = row["Next Show / Availability"]

        if show_time != "Anytime":
            if show_time in seen_times:
                if show_time not in conflicts:
                    conflicts.append(show_time)
            else:
                seen_times.append(show_time)

    return conflicts
    
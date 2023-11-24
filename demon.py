from datetime import datetime

# Your timestamp (in milliseconds since epoch)
timestamp_ms = int(1700473920399)  # Replace this with your actual timestamp

# Convert the timestamp to a datetime object
dt_object_ms = datetime.utcfromtimestamp(timestamp_ms / 1000.0)

# Print the result
print(dt_object_ms)
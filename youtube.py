import webbrowser
import datetime
import time

def open_youtube_search(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def wait_until(target_time):
    current_time = datetime.datetime.now().time()
    while current_time < target_time:
        time.sleep(30)  # Wait for 30 seconds before checking again
        current_time = datetime.datetime.now().time()
    return

def main():
    # Set the target time (24-hour format)
    target_time = datetime.time(19, 0)  # 7:00 PM

    while True:
        # Get the current time
        now = datetime.datetime.now()

        # If the current time is after the target time, calculate the wait time until the next target time (tomorrow)
        if now.time() >= target_time:
            # Calculate the wait time until the next target time (tomorrow)
            tomorrow = now + datetime.timedelta(days=1)
            target_datetime = datetime.datetime.combine(tomorrow.date(), target_time)
        else:
            target_datetime = datetime.datetime.combine(now.date(), target_time)

        # Calculate the time to wait in seconds
        wait_seconds = (target_datetime - now).total_seconds()

        # Wait until the target time
        print(f"Waiting until {target_datetime.time()} to open YouTube...")
        time.sleep(wait_seconds)

        # Open YouTube and search for Citizen TV Live
        search_query = "Citizen TV Live"
        open_youtube_search(search_query)
        print(f"Opened YouTube and searched for '{search_query}' at {datetime.datetime.now().time()}")

        # Sleep for 1 minute to ensure the script doesn't run again within the same minute
        time.sleep(60)

if __name__ == "__main__":
    main()

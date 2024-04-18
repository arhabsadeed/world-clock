import pytz
from datetime import datetime

def get_current_time(timezone):
    """
    Get the current time for a given timezone.
    """
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    return current_time.strftime('%Y-%m-%d %H:%M:%S %Z')

def main():
    countries = {
        'Singapore': 'Asia/Singapore',
        'Malaysia': 'Asia/Kuala_Lumpur',
        'Indonesia': 'Asia/Jakarta',
        'California': 'America/Los_Angeles',
        'India': 'Asia/Kolkata'
    }

    print("Current Time in Different Countries:")
    for country, timezone in countries.items():
        current_time = get_current_time(timezone)
        print(f"{country}: {current_time}")

if __name__ == "__main__":
    main()

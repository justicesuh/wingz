from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    def print_table(self, rows):
        max_date_len = len(max(list(map(lambda r: r[0], rows)), key=len))
        max_name_len = len(max(list(map(lambda r: r[1], rows)), key=len))
        max_count_len = len(max(list(map(lambda r: r[2], rows)), key=len))

        for date, name, count in rows:
            print(f"{date}{' ' * (max_date_len - len(date))}     ", end='')
            print(f"{name}{' ' * (max_name_len - len(name))}     ", end='')
            print(count)

    def handle(self, **options):
        cursor = connection.cursor()
        query = '''
        SELECT
            TO_CHAR(ride.pickup_time, 'YYYY-MM') AS month,
            CONCAT(driver.first_name, ' ', LEFT(driver.last_name, 1), '.') AS name,
            COUNT(*) AS ride_count
        FROM
            rides_ride ride
        JOIN
            users_user driver ON ride.driver_id = driver.id
        JOIN
            rides_rideevent pickup_event ON ride.id = pickup_event.ride_id AND pickup_event.description = 'Status changed to pickup'
        JOIN
            rides_rideevent dropoff_event ON ride.id = dropoff_event.ride_id AND dropoff_event.description = 'Status changed to dropoff'
        WHERE
            EXTRACT(HOUR FROM AGE(dropoff_event.created_at, pickup_event.created_at)) > 1
        GROUP BY
            month,
            name
        '''
        cursor.execute(query)
        rows = [('Month', 'Driver', 'Count of Trips > 1 hr')]
        for date, name, count in cursor.fetchall():
            rows.append((date, name, str(count)))
        self.print_table(rows)

from datetime import datetime, timedelta, timezone
from pytz import timezone
class Date():
    TODOIST_DEFAULT_DATE_FORMAT = '%a %d %b %Y %H:%M:%S %z'
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S%z'

    def get_now(self):
        """
        get the JST current time
        timeZone:Asia/Tokyo

        Returns
        -------
        datetime.now() : datetime
        """
        return datetime.now(timezone('Asia/Tokyo'))

    def date_to_str(self, date, format_pattern=DATE_FORMAT):
        """
        convert date to string

        Parameters
        ----------
        date : datetime
        format_pattern : %Y-%m-%d %H:%M:%S%z

        Returns
        -------
        date : string
        """
        return date.strftime(format_pattern)

    def str_to_date(self, str_date, format_pattern=TODOIST_DEFAULT_DATE_FORMAT):
        """
        convert string to date

        Parameters
        ----------
        str_date : string
        format_pattern :%a %d %b %Y %H:%M:%S %z

        Returns
        -------
        date : date
        """
        return datetime.strptime(str_date, format_pattern)

    def utc_to_jst(self, utc_time):
        """
        convert utcTime to jstTime

        Parameters
        ----------
        utc_time : string

        Returns
        -------
        date : string
        """

        return utc_time.astimezone(timezone('Asia/Tokyo'))

    def jst_to_utc(self, jst_time):
        """
        convert jstTime to utcTime

        Parameters
        ----------
        jst_time : string

        Returns
        -------
        date : string
        """

        return jst_time.astimezone(timezone('UTC'))

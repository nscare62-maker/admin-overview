"""
Custom Jinja2 filters for the admin dashboard
"""

from datetime import datetime
import pytz

# Set the timezone for India (IST)
IST = pytz.timezone('Asia/Kolkata')


def _parse_timestamp(timestamp):
    """Helper to parse a timestamp in int, float, str, or ISO format into IST datetime."""
    if timestamp in (None, '', 'N/A', 'null', 'None', '0', 0):
        return None

    # Handle float/int
    if isinstance(timestamp, (int, float)):
        ts = float(timestamp)
        if ts > 1_000_000_000_000:
            ts /= 1000.0
        return datetime.fromtimestamp(ts, tz=IST)

    # Handle string
    if isinstance(timestamp, str):
        val = timestamp.strip()
        if not val or val in ('N/A', 'null', 'None', '0'):
            return None

        # Check if numeric
        try:
            ts = float(val)
            if ts > 1_000_000_000_000:
                ts /= 1000.0
            return datetime.fromtimestamp(ts, tz=IST)
        except (ValueError, OverflowError):
            pass

        # Try ISO format
        for fmt in (
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d %H:%M',
            '%Y-%m-%dT%H:%M:%S',
            '%Y-%m-%dT%H:%M:%S.%f',
            '%Y-%m-%d'
        ):
            try:
                dt = datetime.strptime(val, fmt)
                if dt.tzinfo is None:
                    return IST.localize(dt)
                return dt.astimezone(IST)
            except ValueError:
                pass

        try:
            dt = datetime.fromisoformat(val.replace('Z', '+00:00'))
            if dt.tzinfo is None:
                return IST.localize(dt)
            return dt.astimezone(IST)
        except (ValueError, TypeError):
            pass

    return None


def timestamp_to_date(timestamp):
    """Convert millisecond timestamp to date string in IST"""
    try:
        dt = _parse_timestamp(timestamp)
        if dt:
            return dt.strftime('%Y-%m-%d')
        return 'N/A'
    except Exception:
        return 'N/A'


def permission_date(value):
    """Format permission dates stored as timestamps or ISO strings."""
    try:
        dt = _parse_timestamp(value)
        if dt:
            return dt.strftime('%Y-%m-%d')
        return 'N/A'
    except Exception:
        return 'N/A'


def timestamp_to_time(timestamp):
    """Convert millisecond timestamp to time string in IST"""
    try:
        dt = _parse_timestamp(timestamp)
        if dt:
            return dt.strftime('%I:%M %p')
        return 'N/A'
    except Exception:
        return 'N/A'


def timestamp_to_datetime(timestamp):
    """Convert millisecond timestamp to datetime string in IST"""
    try:
        dt = _parse_timestamp(timestamp)
        if dt:
            return dt.strftime('%Y-%m-%d %I:%M %p')
        return 'N/A'
    except Exception:
        return 'N/A'


def format_duration(milliseconds):
    """Format milliseconds to human readable duration"""
    try:
        if milliseconds:
            ms = float(milliseconds)
            hours = ms / (1000 * 60 * 60)
            return f"{hours:.1f}h"
        return '0h'
    except Exception:
        return '0h'


def format_minutes(minutes):
    """Format minutes as hours and remaining minutes."""
    try:
        total_minutes = max(0, int(float(minutes or 0)))
        hours, remaining_minutes = divmod(total_minutes, 60)
        if hours and remaining_minutes:
            return f'{hours}h {remaining_minutes}m'
        if hours:
            return f'{hours}h'
        return f'{remaining_minutes}m'
    except (TypeError, ValueError):
        return '0m'


def format_coord(value, precision=4):
    """Safely format coordinate floats, handling strings, None, and decimals."""
    if value in (None, '', 'N/A', 'null', 'None'):
        return 'N/A'
    try:
        num = float(value)
        return f"{num:.{precision}f}"
    except (TypeError, ValueError):
        return 'N/A'


def safe_float(value, default=0.0):
    """Safely cast value to float."""
    try:
        if value is None:
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def register_filters(app):
    """Register all custom filters with Flask app"""
    app.jinja_env.filters['timestamp_to_date'] = timestamp_to_date
    app.jinja_env.filters['permission_date'] = permission_date
    app.jinja_env.filters['timestamp_to_time'] = timestamp_to_time
    app.jinja_env.filters['timestamp_to_datetime'] = timestamp_to_datetime
    app.jinja_env.filters['format_duration'] = format_duration
    app.jinja_env.filters['format_minutes'] = format_minutes
    app.jinja_env.filters['format_coord'] = format_coord
    app.jinja_env.filters['safe_float'] = safe_float

#!/usr/bin/env python3

def basic(summary,start_time,end_time,location=None, description=None, timeZone='Japan'):
  event = {
    'summary': summary,
    'location': location,
    'description': description,
    'start': {
      'dateTime': start_time.isoformat(),
      'timeZone': timeZone,
    },
    'end': {
      'dateTime': end_time.isoformat(),
      'timeZone': timeZone,
    }
  }
  return event

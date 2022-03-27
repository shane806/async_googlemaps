Asynchronous Python Client for Google Maps Services
====================================

## Description

This library is essentially an async "wrapper" (not really wrapping anything, but not sure what better term to use)
of the [google-maps-services-python](https://github.com/googlemaps/google-maps-services-python) library

It includes all APIs used in [google-maps-services-python](https://github.com/googlemaps/google-maps-services-python)

 - Directions API
 - Distance Matrix API
 - Elevation API
 - Geocoding API
 - Geolocation API
 - Time Zone API
 - Roads API
 - Places API
 - Maps Static API

## Key Differences

 - At time of writing, [aiohttp](https://github.com/aio-libs/aiohttp) (basically an async version of Python's requests 
library for those unfamiliar) is used internally for making http requests and can't be substituted.
   - This is only due to my lack of familiarity with other asynchronous libraries
 
## Requirements

 - Python 3.5 or later.
 - A Google Maps API key.

## API Keys

Each Google Maps Web Service request requires an API key or client ID. API keys
are generated in the 'Credentials' page of the 'APIs & Services' tab of [Google Cloud console](https://console.cloud.google.com/apis/credentials).

For even more information on getting started with Google Maps Platform and generating/restricting an API key, see [Get Started with Google Maps Platform](https://developers.google.com/maps/gmp-get-started) in our docs.

**Important:** This key should be kept secret on your server.

## Installation
 
    $ pip install -U async_googlemaps

Note that you will need requests 2.4.0 or higher if you want to specify connect/read timeouts.

## Usage

This example uses the Geocoding API and the Directions API with an API key:

```python
import async_googlemaps
from datetime import datetime

async def main():
  gmaps = async_googlemaps.AsyncClient(key='Add Your Key here')

  # Geocoding an address
  geocode_result = await gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    
  # Look up an address with reverse geocoding
  reverse_geocode_result = await gmaps.reverse_geocode((40.714224, -73.961452))
    
  # Request directions via public transit
  now = datetime.now()
  directions_result = await gmaps.directions("Sydney Town Hall",
                                             "Parramatta, NSW",
                                             mode="transit",
                                             departure_time=now)
```

[//]: # (For more usage examples, check out [the tests]&#40;https://github.com/googlemaps/google-maps-services-python/tree/master/tests&#41;.)

## Features

### Retry on Failure

Automatically retry when intermittent failures occur. That is, when any of the retriable 5xx errors
are returned from the API.


[//]: # (## Building the Project)

[//]: # ()
[//]: # ()
[//]: # (    # Installing nox)

[//]: # (    $ pip install nox)

[//]: # ()
[//]: # (    # Running tests)

[//]: # (    $ nox)

[//]: # ()
[//]: # (    # Generating documentation)

[//]: # (    $ nox -e docs)

[//]: # ()
[//]: # (    # Copy docs to gh-pages)

[//]: # (    $ nox -e docs && mv docs/_build/html generated_docs && git clean -Xdi && git checkout gh-pages)

## Documentation & resources

[Documentation for the `google-maps-services-python` library](https://googlemaps.github.io/google-maps-services-python/docs/index.html)

### Getting started
- [Get Started with Google Maps Platform](https://developers.google.com/maps/gmp-get-started)
- [Generating/restricting an API key](https://developers.google.com/maps/gmp-get-started#api-key)
- [Authenticating with a client ID](https://developers.google.com/maps/documentation/directions/get-api-key#client-id)

### API docs
- [Google Maps Platform web services](https://developers.google.com/maps/apis-by-platform#web_service_apis)
- [Directions API](https://developers.google.com/maps/documentation/directions/)
- [Distance Matrix API](https://developers.google.com/maps/documentation/distancematrix/)
- [Elevation API](https://developers.google.com/maps/documentation/elevation/)
- [Geocoding API](https://developers.google.com/maps/documentation/geocoding/)
- [Geolocation API](https://developers.google.com/maps/documentation/geolocation/)
- [Time Zone API](https://developers.google.com/maps/documentation/timezone/)
- [Roads API](https://developers.google.com/maps/documentation/roads/)
- [Places API](https://developers.google.com/places/)
- [Maps Static API](https://developers.google.com/maps/documentation/maps-static/)

[//]: # (### Support)

[//]: # (- [Report an issue]&#40;https://github.com/googlemaps/google-maps-services-python/issues&#41;)

[//]: # (- [Contribute]&#40;https://github.com/googlemaps/google-maps-services-python/blob/master/CONTRIB.md&#41;)

[//]: # (- [StackOverflow]&#40;http://stackoverflow.com/questions/tagged/google-maps&#41;)

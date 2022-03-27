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

 - At time of writing, [aiohttp](https://github.com/aio-libs/aiohttp) is used for making asynchronous http requests 
and (for now) can't be substituted.
   - When creating the `async_googlemaps.AsyncClient` object, an `aiohttp.ClientSession` object is a required argument.
   - The synchronous `googlemaps.Client` has an optional parameter, `requests_session`, which is the synchronous version.
   - It's required here because (to my knowledge) there's no way to (internally) ensure the async client can be properly closed 
   before the event-loop is closed, therefore it must be handled on the user's end.
   - If you're unfamiliar with `aiohttp`, you should go read the Client quickstart guide
   in the [aiohttp docs]('https://docs.aiohttp.org/')
   - See Usage for details
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

## Usage

There are basically two ways to create the `async_googlemaps.AsyncClient`

These examples use the Geocoding API and the Directions API with an API key:

1. ('Preferred' usage) Use an async context manager for the `aiohttp.ClientSession` that will be passed to the
`async_googlemaps.AsyncClient`
```python
from async_googlemaps import AsyncClient
import aiohttp
from datetime import datetime

async def main():
   async with aiohttp.ClientSession() as maps_session:
      gmaps = AsyncClient(maps_session, key='Add Your Key here')

      # Then use the APIs just as you would with the synchronous version,
      # but with an await keyword prefacing the method
      
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
2. (More flexible) Create your `aiohttp.ClientSession` object without a context-manager, and manually close the ClientSession.

```python
from async_googlemaps import AsyncClient
import aiohttp


async def main():
  session = aiohttp.ClientSession()
  gmaps = AsyncClient(session, key='Add Your Key here')

  # Geocoding an address
  geocode_result = await gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
  
  reverse_geocode_result = await gmaps.reverse_geocode((40.714224, -73.961452))
  
  # aio_client must be closed manually
  await session.close()
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

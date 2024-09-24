import pysurfline

def get_surfline_forecast(spot_id, days, interval_hours):
    # Fetch the surf forecast using the pysurfline package
    spot_forecasts = pysurfline.get_spot_forecasts(
        spotId=spot_id,
        days=days,
        intervalHours=interval_hours,
    )
    return spot_forecasts

def display_spot_name(spot_forecasts):
    print(f"\n\nSurf Forecast for: {spot_forecasts.name}")
    print("=" * 40)

def display_waves(waves):
    print("\n\nWave Forecast:")
    for wave in waves:
        print(f"Time: {wave.timestamp}")
        print(f"Wave Height: {wave.surf.min} - {wave.surf.max} ft")
        print(f"Swell Direction: {wave.swells[0].direction}°")
        print(f"Wave Power: {wave.power}")
        print("-" * 20)

def display_wind(winds):
    print("\n\nWind Forecast:")
    for wind in winds:
        print(f"Time: {wind.timestamp}")
        print(f"Wind Speed: {wind.speed} mph")
        print(f"Wind Direction: {wind.direction}° ({wind.directionType})")
        print(f"Wind Gust: {wind.gust} mph")
        print("-" * 20)

def display_tides(tides):
    print("\n\nTide Forecast:")
    for tide in tides:
        print(f"Time: {tide.timestamp}")
        print(f"Tide Height: {tide.height} ft")
        print(f"Tide Type: {tide.type}")
        print("-" * 20)
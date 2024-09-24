import typer
from rich.console import Console
from surfapp.surfapp import get_surfline_forecast, display_spot_name, display_waves, display_wind, display_tides

# Initialize Typer app and rich console
app = typer.Typer()
console = Console()

@app.command()
def forecast(spot_id: str, days: int = 2, interval_hours: int = 3):
    """Fetch and display surf forecast for the given spot."""
    console.print(f"Fetching forecast for spot ID: {spot_id}")
    
    # Get surf forecast data
    spot_forecasts = get_surfline_forecast(spot_id, days, interval_hours)
    
    # Display the forecast using existing functions
    display_spot_name(spot_forecasts)
    display_waves(spot_forecasts.waves)
    display_wind(spot_forecasts.wind)
    display_tides(spot_forecasts.tides)

if __name__ == "__main__":
    app()
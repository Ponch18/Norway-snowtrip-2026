# Norway Ski Trip Coordinates Extraction Report

## Summary
Successfully extracted starting point GPS coordinates for **17 out of 18** ski trips from the Norway trip website.

### Extraction Statistics
- **Total Trips**: 18
- **Successful Extractions**: 17 (94.4%)
- **Failed Extractions**: 1 (5.6%)

### Data Sources Used
- **Gulliver.it**: 14 trips (most reliable source - coordinates embedded in page metadata)
- **Wikiloc**: 2 trips
- **Web Search**: 1 trip
- **Unable to extract**: 1 trip (authentication required for Strava/Garmin)

## Complete Coordinate List

### Successfully Extracted

1. **Storgalten da Sandneset**
   - Coordinates: 69.9217656, 20.19218909
   - Source: Gulliver.it
   - URL: https://www.gulliver.it/itinerari/storgalten-da-sandneset-per-il-versante-ovest/

2. **Stetinden da Sor Lenangen**
   - Coordinates: 69.87013969, 20.20385742
   - Source: Gulliver.it
   - URL: https://www.gulliver.it/itinerari/stetinden-da-sor-lenangen/

3. **Steinfjellet da Botn**
   - Coordinates: 69.76494441, 19.9848175
   - Source: Gulliver.it
   - URL: https://www.gulliver.it/itinerari/steinfjellet-da-botn-in-sor-lenangen/

4. **Rornesfjellet da Lyngseidet**
   - Coordinates: 69.56510603, 20.07339477
   - Source: Gulliver.it
   - URL: https://www.gulliver.it/itinerari/rornesfjellet-da-lyngseidet/#main

5. **Fastdalstinden SE-S**
   - Coordinates: 69.57891642, 20.23475646
   - Source: Gulliver.it
   - URL: https://www.gulliver.it/itinerari/fastdalstinden-per-versante-se-s/

6. **Sorbmegaisa (Oderdalen)**
   - Coordinates: 69.576101, 20.217846
   - Source: Gulliver.it
   - URL: https://www.gulliver.it/itinerari/sorbmegaisa-oderdalen-dal-kyofjord/#main

7. **Fastdalstinden da Lyngen**
   - Coordinates: 69.575478, 20.218836
   - Source: Gulliver.it
   - URL: https://www.gulliver.it/itinerari/fastdalstindenda-lyngen/

8. **Kavringtinden / Golsavarre**
   - Coordinates: 69.5762866, 20.2188699
   - Source: Gulliver.it
   - URL: https://www.gulliver.it/itinerari/kavringtinden-da-lyngseidet/

9. **Rornestinden**
   - Coordinates: 69.5762866, 20.2188699
   - Source: Gulliver.it
   - URL: https://www.gulliver.it/itinerari/rornestinden-versante-se/

10. **Giilavarri da Olderdalen**
    - Coordinates: 69.608054, 20.526379
    - Source: Gulliver.it
    - URL: https://www.gulliver.it/itinerari/giilavarri-da-olderdalen/

11. **Rissavarri**
    - Coordinates: 69.675164, 20.497925
    - Source: Wikiloc
    - URL: https://de.wikiloc.com/routen-skiwandern/rissavarri-16792946

12. **Storhaugen**
    - Coordinates: 69.745919, 20.510063
    - Source: Norwegian Mountains (via Web Search)
    - URL: https://www.westcoastpeaks.com/Peaks/storhaugen.html

13. **Kjevagtinden da Havnnes**
    - Coordinates: 69.78820577, 20.56726455
    - Source: Gulliver.it
    - URL: https://www.gulliver.it/itinerari/kjevagtinden-da-havnnes/

14. **Stortuva da Oldervik**
    - Coordinates: 69.74498568, 19.67994689
    - Source: Gulliver.it
    - URL: https://www.gulliver.it/itinerari/stortuva-da-oldervik/

15. **Ullstinden da Snarbyeidet**
    - Coordinates: 69.77016858, 19.55497741
    - Source: Gulliver.it
    - URL: https://www.gulliver.it/itinerari/ullstinden-da-snarbyeidet/

16. **Storfjellet (Breivikeidet)**
    - Coordinates: 69.63296347, 19.41421508
    - Source: Gulliver.it
    - URL: https://www.gulliver.it/itinerari/storfjellet-da-ponte-breivikeidet/

17. **Stormheimfjellet**
    - Coordinates: 69.625072, 19.595302
    - Source: Wikiloc
    - URL: https://www.wikiloc.com/back-country-skiing-trails/stormheimfjellet-1181-meters-791194

### Failed Extraction

18. **Traccia 7 Ponch**
    - Coordinates: NOT AVAILABLE
    - Reason: Both Strava and Garmin links require authentication. No public information available.
    - Available URLs:
      - Strava: https://www.strava.com/routes/3401530418737577182
      - Garmin: https://connect.garmin.com/modern/activity/18699892521
    - Notes: "Traccia" is Italian for "track" - this appears to be a personal GPX track with no public documentation

## Technical Notes

### Why Gulliver.it Works Best
Gulliver.it embeds GPS coordinates in the page's structured data (schema.org markup), making it easy to extract coordinates programmatically. The coordinates represent the starting point/trailhead for each route.

### Why Strava Failed
Strava loads route data dynamically via JavaScript after page load. The HTML content doesn't contain coordinate data - it's fetched from Strava's API during page rendering. Access requires authentication.

### Why Garmin Failed
Garmin Connect requires user authentication to view activity details. Public links redirect to login pages.

### Alternative Data Sources Used
When primary sources (Gulliver/Strava) weren't available, I successfully used:
- Wikiloc: Good for trail GPS data with embedded coordinates
- Web search: Found coordinates from hiking/mountaineering databases
- Norwegian Mountains website: Trail descriptions with GPS coordinates

## Recommendations for "Traccia 7 Ponch"

To obtain coordinates for this trip:
1. Access the Garmin activity directly if you have account access
2. Export GPX file from Strava route (requires login)
3. Check the original GPS device/file used to create the track
4. Look at local trip reports or guidebooks for the Lyngen/Troms area

Based on the trip stats (700m elevation, 9.4km distance) and location in the sequence, this appears to be a shorter ski tour in the Lyngen Alps area, possibly near Tromsø or the Lyngenfjord region.

## Files Generated

1. `trip_coordinates.json` - Complete coordinate data in JSON format
2. `COORDINATES_EXTRACTION_REPORT.md` - This detailed report
3. `extract_coordinates.py` - Initial trip extraction script
4. `fetch_coordinates.py` - Coordinate fetching reference script

## Usage

The `trip_coordinates.json` file can be directly imported into mapping applications, GIS software, or used for:
- Creating interactive maps
- Planning logistics and routing
- Calculating distances between trips
- Visualizing trip distribution across the region

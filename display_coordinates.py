#!/usr/bin/env python3
"""
Display extracted coordinates for Norway ski trips
"""

import json

# Read the coordinates file
with open('trip_coordinates.json', 'r', encoding='utf-8') as f:
    trips = json.load(f)

print("=" * 80)
print("NORWAY SKI TRIP STARTING POINT COORDINATES")
print("=" * 80)
print()

successful = [t for t in trips if t['lat'] is not None]
failed = [t for t in trips if t['lat'] is None]

print(f"Total trips: {len(trips)}")
print(f"Successfully extracted: {len(successful)} ({len(successful)/len(trips)*100:.1f}%)")
print(f"Failed to extract: {len(failed)}")
print()

print("=" * 80)
print("COORDINATE DATA")
print("=" * 80)
print()

for i, trip in enumerate(trips, 1):
    print(f"{i}. {trip['name']}")
    if trip['lat'] is not None:
        print(f"   Latitude:  {trip['lat']}")
        print(f"   Longitude: {trip['lng']}")
        print(f"   Source: {trip['source']}")
    else:
        print(f"   Status: COORDINATES NOT AVAILABLE")
        print(f"   Reason: {trip['source']}")
    print(f"   URL: {trip['url']}")
    print()

print("=" * 80)
print("SUMMARY BY REGION")
print("=" * 80)
print()

# Group trips by general latitude (approximate regions)
northern = [t for t in successful if t['lat'] > 69.8]
central = [t for t in successful if 69.6 <= t['lat'] <= 69.8]
southern = [t for t in successful if t['lat'] < 69.6]

print(f"Northern region (>69.8°N): {len(northern)} trips")
for t in northern:
    print(f"  - {t['name']}")
print()

print(f"Central region (69.6-69.8°N): {len(central)} trips")
for t in central:
    print(f"  - {t['name']}")
print()

print(f"Southern region (<69.6°N): {len(southern)} trips")
for t in southern:
    print(f"  - {t['name']}")
print()

print("=" * 80)
print(f"Complete data available in: trip_coordinates.json")
print("=" * 80)

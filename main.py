import cv2
import argparse
from segmentation import segment_image
from analysis import analyze_objects

parser = argparse.ArgumentParser()
parser.add_argument('--image', required=True)
args = parser.parse_args()

image = cv2.imread(args.image)

mask = segment_image(image)
areas, total_area = analyze_objects(mask)

print(f"Total Objects Detected: {len(areas)}\n")

total_fg = 0

for i, area in enumerate(areas):
    percent = (area / total_area) * 100
    total_fg += percent
    print(f"Object {i+1} Area: {area:.0f} pixels ({percent:.2f}%)")

print(f"\nTotal Foreground Coverage: {total_fg:.2f}%")
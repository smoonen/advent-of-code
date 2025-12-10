import itertools, sys, shapely

area = lambda p1, p2 : (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

coords = [(int(x), int(y)) for x, y in [line.rstrip().split(',') for line in sys.stdin.readlines()]]

best = max([area(p1, p2) for p1, p2 in itertools.combinations(coords, 2)])
print(f"Part 1: {best}")

# I experimented with floodfill but had challenges identifying an interior point.
# I tried shapely but for some reason it was slow. I think I was calculating size of every single rectangle rather than only as needed.
# I tried my own approach of ray tracing to discover interior points. Some things I learned:
#   - Needed to switch to numpy array for space efficiency (also experimented with bitarray).
#   - Needed to handle crossing of a horizontal line as a single crossing.
# Rather than do that I briefly experiemnted with calculating intersections between polygon and each rectangle.
#   My thought was that any rectangle whose edges intersected the polygon "inside" their vertices was out.
#   I think this approach should work but I had some bug in it. I never debugged because . . .
# I switched back to shapely based on Brian's results and it worked well.
# Thanks to Brian for the idea of using a shapely.box instead of four line segments.

p = shapely.Polygon(coords)
rectangles_with_area = sorted([(area(p1, p2), p1, p2) for p1, p2 in itertools.combinations(coords, 2)], key = lambda x : -x[0])
best = next((area for area, p1, p2 in rectangles_with_area if p.contains(shapely.box(min(p1[0], p2[0]), min(p1[1], p2[1]), max(p1[0], p2[0]), max(p1[1], p1[1])))))
print(f"Part 2: {best}")



class Point:
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

# def generate_weather_grid(center, ring_count, grid_spacing):
#     # returns a list containing the geographic coordinates of a square grid
#     # center: lat long location of the center the grid will be created around
#     # ring_count: how many locations to generate around the center e.g. 1 = 9 points, 2 = 25 points
#     # grid spacing: the x and y spacing of each grid point


def generate_nine_point_grid(center, grid_spacing):
    # returns a list containing the geographic coordinates of a square grid
    # center: (lon, lat) location of the center the grid will be created around
    # grid spacing: the x and y spacing of each grid point

    pos_spacing = grid_spacing
    neg_spacing = grid_spacing * -1

    north = create_offset_coord(center, 0, pos_spacing)
    northeast = create_offset_coord(center, pos_spacing, pos_spacing)
    east = create_offset_coord(center, pos_spacing, 0)
    southeast = create_offset_coord(center, pos_spacing, neg_spacing)
    south = create_offset_coord(center, 0, neg_spacing)
    southwest = create_offset_coord(center, neg_spacing, neg_spacing)
    west = create_offset_coord(center, neg_spacing, 0)
    northwest = create_offset_coord(center, neg_spacing, pos_spacing)

    return [center, north, northeast, east, southeast, south, southwest, west, northwest]


def create_offset_coord(point, lon_offset, lat_offset):
    new_lon = point.lon + lon_offset
    new_lat = point.lat + lat_offset

    if new_lon > 180:
        new_lon = -180 + (new_lon % 180)

    # for calculation safety at poles
    if new_lat > 90:
        new_lat = 90

    if new_lat < -90:
        new_lat = -90

    return Point(new_lon, new_lat)



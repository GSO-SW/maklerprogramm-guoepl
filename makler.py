from math import sin, cos, pi


def create_points(walls:list) -> list:
    angle, last_angle = 0, 0
    points: list = [(0, 0), (walls[0][1], 0)]
    for k, j in enumerate(walls[1:-1]):
        angle = (last_angle + 180 - walls[k][2]) % 360
        last_angle = angle
        x = points[k + 1][0] + round(j[1] * cos((pi / 180) * angle), 2)
        y = points[k + 1][1] + round(j[1] * sin((pi / 180) * angle), 2)
        points.append((x, y))
    return points


def calc_area(points:list , multiplier: float = 1.0) -> float:
    """
    Calculate the area of given points.
    """
    number_of_points: int = len(points)
    sum1, sum2 = 0, 0
    for i in range(number_of_points):
        if i == number_of_points - 1:
            sum1 = sum1 + points[i][0] * points[0][1]
            sum2 = sum2 + points[0][0] * points[i][1]
        else:
            sum1 = sum1 + points[i][0] * points[i + 1][1]
            sum2 = sum2 + points[i][1] * points[i + 1][0]
    return (abs(sum1 - sum2) / 2) * multiplier
    

def validate_input(choice: int, msg: str):
    """
    Return the validated input of choice.
    """
    is_valid_input = False
    while not is_valid_input:
        try:
            if choice == 1:
                valid_input = int(input(msg))
            if choice == 2:
                valid_input = float(input(msg))
        except ValueError:
            print("Ungültige Eingabe")
        else:
            is_valid_input = True
    return valid_input    


def flat_size(msg1: str = "Anzahl Räume: ", reduced: bool = False) -> float:
    area: float = 0
    number_of_rooms: int = validate_input(1, msg1)
    for _ in range(number_of_rooms):
        is_partially_reduced = False
        multiplier = 1.0
        walls: list = []
        number_of_walls = validate_input(1, "Anzahl Wände: ")
        is_right_angled = True if input("Nur rechtwinkelig? j / n : ").lower().strip() == "j" else False
        if not reduced:
            is_partially_reduced = True if input("Teilbereiche des Raumes müssen" +\
                " mit verringerten Maßen berechnet werden? j / n : ").lower().strip() == "j" else False
        else:
            multiplier = validate_input(2, "Multiplier: ")
        for i in range(number_of_walls):
            wall_width = validate_input(2, "Wandbreite: ")
            if is_right_angled:
                angle = 90
            else:
                angle = validate_input(2, "Winkel: ")
            walls.append((i, wall_width, angle))
        points = create_points(walls)
        area += calc_area(points, multiplier)
        if is_partially_reduced:
            area -= flat_size("Anzahl Teilbereiche mit reduzierter Fläche: ", True)
    return area


def main():
    area = flat_size()
    print(f"Die Wohnung ist {area} qm groß.")


if __name__ == '__main__':
    main()

from math import sin, cos, pi


def create_points(walls:list) -> list:
    angle, last_angle = 0, 0
    points = [(0, 0), (walls[0][1], 0)]
    for k, j in enumerate(walls[1:-1]):
        angle = (last_angle + 180 - walls[k][2]) % 360
        last_angle = angle
        x = points[k + 1][0] + round(j[1] * cos((pi / 180) * angle), 2)
        y = points[k + 1][1] + round(j[1] * sin((pi / 180) * angle), 2)
        points.append((x, y))
    return points


def calc_area(points:list) -> list:
    """
    Calculate the area of given points.
    """
    number_of_points = len(points)
    sum1, sum2 = 0, 0
    for i in range(number_of_points):
        if i == number_of_points - 1:
            sum1 = sum1 + points[i][0] * points[0][1]
            sum2 = sum2 + points[0][0] * points[i][1]
        else:
            sum1 = sum1 + points[i][0] * points[i + 1][1]
            sum2 = sum2 + points[i][1] * points[i + 1][0]
    return abs(sum1 - sum2) / 2
    

def validate_input(choice: int):
    """
    Return the validated input of choice.
    """
    is_valid_input = False
    while not is_valid_input:
        try:
            if choice == 1:
                valid_input = int(input("Anzahl Räume: "))
            if choice == 2:
                valid_input = int(input("Anzahl Wände: "))
            if choice == 3:
                valid_input = float(input("Wandbreite: "))
            if choice == 4:
                valid_input = float(input("Winkel: "))
        except ValueError:
            print("Ungültige Eingabe")
        else:
            is_valid_input = True
    return valid_input    


def flat_size() -> float:
    area = 0
    number_of_rooms = validate_input(1)
    for _ in range(number_of_rooms):
        number_of_walls = validate_input(2)
        walls = []
        is_right_angled = True if input("Nur rechtwinkelig? j / n : ").lower().strip() == "j" else False
        for i in range(number_of_walls):
            wall_width = validate_input(3)
            if is_right_angled:
                angle = 90
            else:
                angle = validate_input(4)
            walls.append((i, wall_width, angle))
        points = create_points(walls)
        area += calc_area(points)   
    return area


def main():
    area = flat_size()
    print(f"Die Wohnung ist {area} qm groß.")


if __name__ == '__main__':
    main()
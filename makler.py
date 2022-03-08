from math import sin, cos, pi


def flat_size():
    area = 0
    is_valid_number_of_rooms = False
    while not is_valid_number_of_rooms:
        try:
            number_of_rooms: int = int(input("Anzahl Räume: "))
        except ValueError:
            print("Ungültige Eingabe")
        else:
            is_valid_number_of_rooms = True
    for _ in range(number_of_rooms):
        is_valid_number_of_walls = False
        while not is_valid_number_of_walls:
            try:
                number_of_walls: int = int(input("Anzahl Wände: "))
            except ValueError:
                print("Ungültige Eingabe")
            else:
                is_valid_number_of_walls = True
        walls = []
        is_right_angled = True if input("Nur rechtwinkelig? j / n\n").lower().strip() == "j" else False
        for i in range(number_of_walls):
            is_valid_wall_width, is_valid_angle = False, False
            while not is_valid_wall_width:
                try:
                    wall_width: float = float(input("Wandbreite: "))
                except ValueError:
                    print("Ungültige Eingabe")
                else:
                    is_valid_wall_width = True
            if is_right_angled:
                angle = 90
            else:
                while not is_valid_angle:
                    try:
                        angle = float(input("Winkel: "))
                    except ValueError:
                        print("Ungültige Eingabe")
                    else:
                        is_valid_angle = True
            walls.append((i, wall_width, angle))
        angle, last_angle = 0, 0
        points = [(0, 0), (walls[0][1], 0)]
        for k, j in enumerate(walls[1:-1]):
            angle = (last_angle + 180 - walls[k][2]) % 360
            last_angle = angle
            x = points[k + 1][0] + round(j[1] * cos((pi / 180) * angle), 2)
            y = points[k + 1][1] + round(j[1] * sin((pi / 180) * angle), 2)
            points.append((x, y))
        number_of_points = len(points)
        sum1, sum2 = 0, 0
        for i in range(number_of_points):
            if i == number_of_points - 1:
                sum1 = sum1 + points[i][0] * points[0][1]
                sum2 = sum2 + points[0][0] * points[i][1]
            else:
                sum1 = sum1 + points[i][0] * points[i + 1][1]
                sum2 = sum2 + points[i][1] * points[i + 1][0]
        area = area + abs(sum1 - sum2) / 2
    print(f"Die Wohnung ist {area} qm groß.")


if __name__ == '__main__':
    flat_size()

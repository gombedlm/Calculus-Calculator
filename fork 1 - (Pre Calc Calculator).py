if angle_A != None and side_a != None and side_c != None:
    if side_a >= side_c:
        print("1 sol")
    else:
        print("We are going to find the height")
        height = side_c * math.degrees(math.sin(angle_A))
        print(height)
        height = math.round(height)
        print(height)
        if side_a < height:
            print("No solution")
            solutions = 0
        if side_a == height:
            print("1 sol")
            solutions = 1
        if height < side_a < side_c:
            print("2 sol")
            solutions = 2

        if solutions == 0:
            sys.exit()
        if solutions == 1:
            angle_C = (side_c * math.degrees(math.sin(angle_A))) / side_a
            angle_C = math.round(angle_C)
            angle_B = 180 - (angle_A + angle_C)
            side_b = (side_a * math.degrees(math.sin(angle_B)) / math.degrees(math.sin(angle_A)))

            print("<A:" + str(angle_A) + "  side a:" + str(side_a))
            print("<B:" + str(angle_B) + "  side b:" + str(side_b))
            print("<C:" + str(angle_C) + "  side c:" + str(side_c))

        if solutions == 2:
            angle_C = (side_c * math.degrees(math.sin(angle_A))) / side_a
            angle_C = math.round(angle_C)
            angle_B = 180 - (angle_A + angle_C)
            side_b = (side_a * math.degrees(math.sin(angle_B))) / math.degrees(math.sin(angle_A))

            angle_A2 = angle_A
            side_a2 = side_a
            side_c2 = side_c

            angle_B2 = 180 - angle_B
            angle_C2 = 180 - (angle_A2 + angle_B2)

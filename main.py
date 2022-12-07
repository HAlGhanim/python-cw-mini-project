# الجزء الاول
def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30
    elif court_type == "outdoor":
        return 20
    else:
        return False

# الجزء الثاني
def rackets_cost(racket_brand):
    if racket_brand == "Bullpadel":
        return 100
    elif racket_brand == "Nox":
        return 140
    elif racket_brand == "Siux":
        return 200
    else:
        return False

# الجزء الثالث
def padel_balls_cost(ball_boxes):
    if ball_boxes == "1":
        return "2"
    elif ball_boxes == "2":
        return "3.5"
    elif ball_boxes == "3":
        return "5"
    else:
        return False

# الجزء الرابع
def padel_game_cost():
    hours = input("Enter the amount of hours: ")
    ct= input("Enter the court type: ")
    rb =input("Enter the racket brand: ")
    bb =input("Enter the number of ball boxes: ")

    print(f"hours: {hours}")
    print(f"court_type: {padel_court_cost(ct)}")
    print(f"racket_brand: {rackets_cost(rb)}")
    print(f"ball_boxes: {padel_balls_cost(bb)}")

padel_game_cost()

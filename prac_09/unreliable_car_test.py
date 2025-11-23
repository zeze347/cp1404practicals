from unreliable_car import UnreliableCar

def main():
    my_car = UnreliableCar("car1", 100, 30)
    good_drive = 0
    bad_drive = 0
    for i in range(100):
        if my_car.drive(1) > 0:
            good_drive += 1
        else:
            bad_drive += 1

    print(good_drive)
    print(bad_drive)


if __name__ == "__main__":
    main()
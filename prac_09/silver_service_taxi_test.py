from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("FancyCar", 100, 2)

    taxi.drive(18)
    fare = taxi.get_fare()

    print(taxi)
    print(f"Fare: ${fare:.2f}")
    assert fare == 48.8, "Fare calculation is incorrect!"

if __name__ == "__main__":
    main()
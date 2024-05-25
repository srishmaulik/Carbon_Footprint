from pydantic import BaseModel, ValidationError

class Transport(BaseModel):
    mode: str
    distance: float
    passengers: int = 1

class Waste(BaseModel):
    type: str
    quantity: float

class Food(BaseModel):
    type: str
    amount: float

def calculate_footprint_transport(transport: Transport) -> float:
    if transport.mode == 'car':
        return transport.distance * 400
    elif transport.mode == 'cycle':
        return 33 * transport.distance
    elif transport.mode == 'foot':
        return 19 * transport.distance
    elif transport.mode == 'pool':
        return (400 / transport.passengers) * transport.distance
    elif transport.mode == 'motorcycle':
        return 162 * transport.distance
    else:
        raise ValueError(f"Unknown transport mode: {transport.mode}")

def calculate_waste_carbon(waste: Waste) -> float:
    carbon_footprint_per_kg = {
        "plastic": 3200,  # g CO2 eq/kg
        "paper": 700,     # g CO2 eq/kg
        "cans": 16000,    # g CO2 eq/kg
        "glass": 1000     # g CO2 eq/kg
    }
    return carbon_footprint_per_kg[waste.type] * waste.quantity

def calculate_food_carbon(food: Food) -> float:
    carbon_footprint_per_kg = {
        "meat": 10000,      # g CO2 eq/kg (high estimate for meat-based diet)
        "vegetarian": 5000, # g CO2 eq/kg (lower estimate for vegetarian diet)
        "vegan": 3500       # g CO2 eq/kg
    }
    return carbon_footprint_per_kg[food.type] * food.amount

def main():
    emissions = {
        'transport_emission': 0,
        'car': 0,
        'cycle': 0,
        'motorcycle': 0,
        'pool': 0,
        'foot': 0,
        'waste_emission': 0,
        'plastic': 0,
        'paper': 0,
        'glass': 0,
        'cans': 0,
        'food_emission': 0,
        'meat': 0,
        'vegetarian': 0,
        'vegan': 0,
        'total_emission': 0
    }

    print("Welcome to Carbon Footprint Calculator!")

    print("Transport Emissions Calculator:")
    while True:
        mode = input("Enter transport mode (car, cycle, foot, pool, motorcycle) or 'none' to stop: ").strip().lower()
        if mode == 'none':
            break
        distance = float(input(f"Enter distance traveled by {mode} in km: "))
        passengers = 1
        if mode == 'pool':
            passengers = int(input("Enter number of passengers: "))
        try:
            transport = Transport(mode=mode, distance=distance, passengers=passengers)
            emissions[mode] += calculate_footprint_transport(transport)
        except ValidationError as e:
            print(f"Input error: {e}")

    emissions['transport_emission'] = emissions['car'] + emissions['cycle'] + emissions['motorcycle'] + emissions['foot'] + emissions['pool']
    
    print("Waste Emissions Calculator:")
    while True:
        waste_type = input("Enter waste type (plastic, paper, cans, glass) or 'none' to stop: ").strip().lower()
        if waste_type == 'none':
            break
        quantity = float(input(f"Enter quantity of {waste_type} waste in kg: "))
        try:
            waste = Waste(type=waste_type, quantity=quantity)
            emissions[waste_type] += calculate_waste_carbon(waste)
        except ValidationError as e:
            print(f"Input error: {e}")

    emissions['waste_emission'] = emissions['cans'] + emissions['glass'] + emissions['paper'] + emissions['plastic']
    
    print("Food Emissions Calculator:")
    while True:
        diet_type = input("Enter diet type (meat, vegetarian, vegan) or 'none' to stop: ").strip().lower()
        if diet_type == 'none':
            break
        amount = float(input(f"Enter amount of {diet_type} diet in kg: "))
        try:
            food = Food(type=diet_type, amount=amount)
            emissions[diet_type] += calculate_food_carbon(food)
        except ValidationError as e:
            print(f"Input error: {e}")

    emissions['food_emission'] = emissions['meat'] + emissions['vegetarian'] + emissions['vegan']
    
    emissions['total_emission'] = emissions['food_emission'] + emissions['transport_emission'] + emissions['waste_emission']
    print(f"\nTotal Carbon Emissions: {emissions['total_emission']} grams CO2 equivalent")

if __name__ == "__main__":
    main()

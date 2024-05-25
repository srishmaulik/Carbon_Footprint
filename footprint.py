def calculate_footprint_transport(distance, mode, passengers):
    if mode == 'car':
        return distance * 400
    elif mode == 'cycle':
        return 33*distance
    elif mode == 'foot':
        return 19*distance
    elif mode == 'pool':
        return ((400/passengers)*distance)
    elif mode == 'motorcycle':
        return 162*distance
    
def calculate_waste_carbon(waste_type, quantity):
    carbon_footprint_per_kg = {
      "plastic": 3200,  # g CO2 eq/kg
      "paper": 700,   # g g CO2 eq/kg
      "cans" : 16000, #g CO2 eq/kg
      "glass" : 1000 #g CO2 eq/kg

      
  }
    return carbon_footprint_per_kg[waste_type]*quantity

def calculate_food_carbon(diet_type, amount):
    carbon_footprint_per_kg = {
      "meat": 10000,  # kg CO2 eq/kg (high estimate for meat-based diet)
      "vegetarian": 5000,  # kg CO2 eq/kg (lower estimate for vegetarian diet)
      "vegan": 3500 #vegan
  }
    return carbon_footprint_per_kg[diet_type] * amount


def main():
    emissions = {
        'transport_emission': 0,
        'car': 0,
        'cycle': 0,
        'motorcycle': 0,
        'pool': 0,
        'foot': 0,

        'waste_emmission': 0,
        'plastic': 0,
        'paper': 0,
        'glass': 0,
        'cans': 0,

        'food_emmission': 0,
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
        emissions[mode] += calculate_footprint_transport(distance, mode, passengers)
    emissions['transport_emission'] = emissions['car'] + emissions['cycle'] + emissions['motorcycle'] + emissions['foot'] + emissions['pool']
    
    while True:
        waste_type = input("Enter waste type (plastic, paper, cans, glass) or 'none' to stop: ").strip().lower()
        if waste_type == 'none':
            break
        quantity = float(input(f"Enter quantity of {waste_type} waste in kg: "))
        emissions[waste_type] += calculate_waste_carbon(waste_type, quantity)
    emissions['waste_emmission'] = emissions['cans']+emissions['glass']+ emissions['paper']+emissions['plastic']
    
    while True:
        diet_type = input("Enter diet type (meat, vegetarian, vegan) or 'none' to stop: ").strip().lower()
        if diet_type == 'none':
            break
        amount = float(input(f"Enter amount of {diet_type} diet in kg: "))
        emissions[diet_type] += calculate_food_carbon(diet_type, amount)
    emissions['food_emmission'] = emissions['meat']+emissions['vegetarian']+emissions['vegan']
    emissions['total_emission'] = emissions['food_emmission']+emissions['transport_emission']+emissions['waste_emmission']
    print(f"\nTotal Carbon Emissions: {emissions['total_emission']} grams CO2 equivalent")

if __name__ == "__main__":
    main()
    


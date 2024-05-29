function show(pageToShow, pageToHide) {
    document.getElementById(pageToShow).style.display = 'block';
    document.getElementById(pageToHide).style.display = 'none';
    return false;
}

function calculateEmissions(event) {
    event.preventDefault();
    
    // Transport Emissions
    const transportMode = document.getElementById('transport_mode').value;
    const transportDistance = parseFloat(document.getElementById('transport_distance').value);
    const transportPassengers = parseInt(document.getElementById('transport_passengers').value) || 1;
    
    let transportEmissions = 0;
    switch (transportMode) {
        case 'car':
            transportEmissions = transportDistance * 400;
            break;
        case 'cycle':
            transportEmissions = 33 * transportDistance;
            break;
        case 'foot':
            transportEmissions = 19 * transportDistance;
            break;
        case 'pool':
            transportEmissions = (400 / transportPassengers) * transportDistance;
            break;
        case 'motorcycle':
            transportEmissions = 162 * transportDistance;
            break;
        default:
            alert(`Unknown transport mode: ${transportMode}`);
            return;
    }
    
    // Waste Emissions
    const wasteType = document.getElementById('waste_type').value;
    const wasteQuantity = parseFloat(document.getElementById('waste_quantity').value);
    
    const wasteCarbonFootprintPerKg = {
        "plastic": 3200,
        "paper": 700,
        "cans": 16000,
        "glass": 1000
    };
    
    const wasteEmissions = wasteCarbonFootprintPerKg[wasteType] * wasteQuantity;
    
    // Food Emissions
    const foodType = document.getElementById('food_type').value;
    const foodAmount = parseFloat(document.getElementById('food_amount').value);
    
    const foodCarbonFootprintPerKg = {
        "meat": 10000,
        "vegetarian": 5000,
        "vegan": 3500
    };
    
    const foodEmissions = foodCarbonFootprintPerKg[foodType] * foodAmount;
    
    // Total Emissions
    const totalEmissions = transportEmissions + wasteEmissions + foodEmissions;
    
    // Display results
    document.getElementById('total_emissions').innerText = totalEmissions.toFixed(2);
    show('Page2', 'Page1');
}

document.getElementById('carbonForm').addEventListener('submit', calculateEmissions);

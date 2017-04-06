// Assignment: Creating Objects I
// We are going to create our very own constructor. 
//Create a VehicleConstructor that takes in the name, number of wheels, and the number of passengers. 

//Then complete the following tasks:
// Each vehicle should have a makeNoise method Using the constructor
// create a Bike Redefine the Bike’s makeNoise method to print “ring ring!” 
//Create a Sedan Redefine the Sedan’s makeNoise method to print “Honk Honk!” 
//Using the constructor, create a Bus Add a method to Bus that takes in the number of passengers to pick up and adds them to the passenger count​

function VehicleConstructor(name,wheels,num_passengers) {
  var vehicle={};
  vehicle.name = name;
  vehicle.wheels = wheels;
  vehicle.num_passengers = num_passengers;
  vehicle.makeNoise = function() {
    console.log("Beep Beep")
  }
  return vehicle;
}
var Bike = VehicleConstructor(Bike,2,1);
Bike.makeNoise = function(){
  console.log("ring ring!");
}
Bike.makeNoise()

var Sedan=VehicleConstructor(Sedan,4,5)
  Sedan.makeNoise=function(){
    console.log("Honk Honk");
  }
Sedan.makeNoise();

var Bus = VehicleConstructor(Bus,4,10)
  Bus.addPassengers=function(passenger){
    Bus.num_passengers= Bus.num_passengers + passenger;
    console.log(Bus.num_passengers)
  }
Bus.makeNoise();
Bus.addPassengers(3);
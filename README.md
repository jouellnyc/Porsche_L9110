# Porsche_L9110

A toy car using hobby motors and the L9110 DC Motor Controller.

The repository name is hopefully obviously silly.


# What is this?

The goal here was to create a toy car using some basic electronics components (the more basic the better). 
<BR>
I wanted to see if I could create it from scratch  powered by a Raspberry Pi Pico or an ESP 32.

Some of the design goals were:
- Low cost / Simple Design
- Creating from scratch / not following any particular recipe
- Start 'now' - even without a proper chassis or wheels - just what I have currently. Make it better later.
<BR>
I had a few of these L9110  motor controllers so I figured I'd try to use some of these and some 5 volt motors.

# Prototype Suggestions/Parts



| Item | Details |Pic/Other|
|---|---|---|
| Pi Pico | [Anywhere Picos are sold](https://www.raspberrypi.com/products/raspberry-pi-pico/)|<img src="https://github.com/user-attachments/assets/318ca87a-3d7b-445c-9ac5-b7a4d846f526" width="100" height="100">|
| 10 popsicle sticks| [Amazon](https://www.amazon.com/gp/product/B08BZSNVSQ)|<img src="https://github.com/user-attachments/assets/b28e239e-7de9-4ed8-b0d9-d221ec426c9a" width="100" height="100">|
| Battery pack when mobile|[Adafruit](https://www.adafruit.com/product/3905)|<img src="https://github.com/user-attachments/assets/a447f1aa-ab6f-475a-ba90-896815e2cebe" width="100" height="100">|
| 2 x L9110|[L9110](https://www.amazon.com/HiLetgo-H-bridge-Stepper-Controller-Arduino/dp/B00M0F243E)|<img src="https://github.com/user-attachments/assets/725afd47-e233-48fa-a526-6681a73b5cbb" width="100" height="100">|
| Wheels and Motors| [Wheels](https://www.amazon.com/gp/product/B0CG1C7T8J)|<img src="https://github.com/user-attachments/assets/5d096c64-0a00-4735-a2d5-15d49f6d733f" width="100" height="100">|
| 400 point breadboard | [Amazon](https://www.amazon.com/Breadborad-Solderless-Breadboards-Distribution-Connecting/dp/B082VYXDF1/)|<img src="https://github.com/user-attachments/assets/73578bff-e890-43b0-9ae0-a52ea4e461f7" width="100" height="100">
| Tissue Paper Roll | Left up to the reader|
| Small latching button | Optional - most any will do | It can help to turn the car/pico on/off|

Note: I chose 2 motor controllers just because it seemed to be more balanced. It's not a requirement as the L9110 can handle 2 motors.

# First steps assembling the Prototype

- Got 8 popsicle sticks, glued them together and created a square out of them.
- Got 2 more and made a support bar in the middle of the square.
- Took the motors and held them tight with some elastics criss crossed.
- Added the Tissue Paper Roll
   - To save time on a quick prototype 
   - There was not a lot of room left
- Hooked up the motor controllers to each of the motors and tucked the wires through the Tissue Paper Roll.

# Prototype A
![image](https://github.com/user-attachments/assets/c0387acd-d72a-432a-9408-f1052f367763)

## Code

Next I tried to understand how the wheels would be moving forward and backward in terms of <A HREF="https://docs.micropython.org/en/latest/library/machine.PWM.html">PWM</A> and the pins on the L9110.

<P>

The L9110 PCB is overly verbose:

![image](https://github.com/user-attachments/assets/ab90f580-209f-45e6-b4e8-3fcbc46748e7)

The names could just be A1, A2, B1, and B2. 

<BR>

I matched up the names of the pins to the variables to make it make sense but it looks a bit 'busy':

![image](https://github.com/user-attachments/assets/a89fc2eb-1d34-48da-8c50-7ff73591c402)

and not overly optimized:

![image](https://github.com/user-attachments/assets/92bb156e-6590-48dc-a6f2-0ba7861754de)


## Pre First Spin
Once the API was done I added the battery pack and took it out for a spin, not having a very high expectation of great motion.

## Prototype A with 4.8 V mobile battery pack
<img src="https://github.com/user-attachments/assets/d9a93cd9-c9dc-4652-83d8-0ac29dbf39c1" width="550" height="450">

## First Spin

Goal: move forward, stop, move backward, stop, turn left at 50% speed, stop, turn right at 50% speed, then stop.

![image](https://github.com/user-attachments/assets/2097411b-7469-452f-9472-e4592f0da8e7)

It didn't really do that so much. It definitely interested the cat and appears as if it was seeking her out:

<A href="https://github.com/jouellnyc/Porsche_L9110/raw/main/media/first_spin.mp4">First Spin Video</A>

It seems like the tissue roll impeded the movement and  the right wheel just wasn't working well when switching speeds.

Since it is actually working, next steps are to put a more 'proper' chassis and work some bugs out.


# Prototype B - Using an actual Chassis   

Swapping out the popsicle sticks and tissue paper for a 'proper' toy chassis:

| Item | Details |Pic/Other|
|---|---|---|
| Motor Smart Robot Car Chassis Kit | [AliExpress](https://www.aliexpress.us/item/3256805787518210.html)|<img src="https://github.com/user-attachments/assets/ef5b128b-40f2-4295-882c-b8f25ee62923" width="100" height="100">|

<img src="https://github.com/user-attachments/assets/09399dc6-7f6f-47f3-9293-c8f51cb290d7" width="550" height="450">

## Second  Spin
Things went went. The car followed the steps well. 
<BR>
But there was big jump/herky-jerky movement on moving backward because of the weight and placement of the battery.

<A href="https://github.com/jouellnyc/Porsche_L9110/raw/main/media/second_spin.mp4">Second Spin Video</A>

## Updated Placement:

Moved the battery holder closer and the flipped it the breadboard:

<img src="https://github.com/user-attachments/assets/e91a1727-8c62-4c10-9072-c1efffec6896" width="550" height="450">

## Third Spin
Things went better. After placing the battery pack closer to the center of gravity, the car followed the steps significantly more smoothly.

<A href="https://github.com/jouellnyc/Porsche_L9110/raw/main/media/third_spin.mp4">Third Spin Video</A>


## Fourth Spin
After correcting the left and right turns, the api was complete and minimally viable. The car can move forward, backward, turn left and turn right.




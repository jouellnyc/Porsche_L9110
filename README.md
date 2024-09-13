# Porsche_L9110

A remote control car based off of toy motors and the L9110 DC Motor  Controller.

The repository name is hopefully obviously silly.

TBD: 'more words'

# What is this?

The goal here was to create a toy  car using some basic electronics components ( the more basic the better). 
I wanted to see if I could create it from scratch  powered by a Raspberry Pi Pico or an ESP 32.

Some of the design goals were low cost and  creating from scratch / not following any particular recipe.
I had a few of these L9110  motor controllers so I figured I'd try to use some of these and some 5 volt motors.

# Prototype Sugesstions/Parts

| Item | Details |Pic/Other|
|---|---|---|
| Pi Pico | [Anywhere Picos are sold](https://www.raspberrypi.com/products/raspberry-pi-pico/)|<img src="https://github.com/user-attachments/assets/b1bd51ea-bdc2-4049-8a72-e881141e6e18" width="100" height="100">|
| 8 popsicle sticks| [Amazon](https://www.amazon.com/gp/product/B08BZSNVSQ)|<img src="https://github.com/user-attachments/assets/b28e239e-7de9-4ed8-b0d9-d221ec426c9a" width="100" height="100">|
| Battery pack when mobile|[Adafruit](https://www.adafruit.com/product/3905)|<img src="https://github.com/user-attachments/assets/a447f1aa-ab6f-475a-ba90-896815e2cebe" width="100" height="100">|
| L9110|[L9110](https://www.amazon.com/HiLetgo-H-bridge-Stepper-Controller-Arduino/dp/B00M0F243E)|<img src="https://github.com/user-attachments/assets/725afd47-e233-48fa-a526-6681a73b5cbb" width="100" height="100">|
| Wheels and Motors| [Wheels](https://www.amazon.com/gp/product/B0CG1C7T8J)|<img src="https://github.com/user-attachments/assets/5d096c64-0a00-4735-a2d5-15d49f6d733f" width="100" height="100">|
| Tissue Paper Roll | Left up to the reader|
| 400 point breadboard | [Amazon](https://www.amazon.com/Breadborad-Solderless-Breadboards-Distribution-Connecting/dp/B082VYXDF1/)|<img src="https://github.com/user-attachments/assets/73578bff-e890-43b0-9ae0-a52ea4e461f7" width="100" height="100">


Once the Coating in API was done I added the battery pack and took it out for a spin again not having a very high expectation of the actual motion for it


# First steps assembling the Prototype

- Got 8 popsicle sticks, glued them together and created a square out of them.  
- Took the motors and held them tight with some elastics criss crossed.
- Added the Tissue Paper Roll
   - To save time
   - Tere was not a lot of room left
   - It's a quick prototype 
- Hooked up the motor controllers to each of the motors and tucked the wires through the Tissue Paper Roll.
- Tried to understand how the wheels would be moving forward and backward.

# Prototype
![image](https://github.com/user-attachments/assets/c0387acd-d72a-432a-9408-f1052f367763)

# Code

The L9110 is overly verbose. I matched up the names of the pins to the variables to make it make sense but it looks a bit 'busy':

![image](https://github.com/user-attachments/assets/a89fc2eb-1d34-48da-8c50-7ff73591c402)

and not overly optimized:

![image](https://github.com/user-attachments/assets/92bb156e-6590-48dc-a6f2-0ba7861754de)


# Pre First Spin
Once the  API was done I added the battery pack and took it out for a spin, not having a very high expectation of great motion.

# Prototype with 4.8 V mobile battery pack
<img src="https://github.com/user-attachments/assets/d9a93cd9-c9dc-4652-83d8-0ac29dbf39c1" width="550" height="450">

# First Spin

Goal: move forward, stop, move backward, stop, turn left at 50% speed, stop, turn right at 50% speed, then stop.

![image](https://github.com/user-attachments/assets/2097411b-7469-452f-9472-e4592f0da8e7)

It didn't really do that so much. It definitely interested the cat and appears as if it was seeking her out:

<A href="https://github.com/jouellnyc/Porsche_L9110/blob/main/first_spin.mp4">Video</A>



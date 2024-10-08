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
| Pi Pico | [Anywhere Picos are sold](https://www.raspberrypi.com/products/raspberry-pi-pico/)|<img src="https://github.com/user-attachments/assets/318ca87a-3d7b-445c-9ac5-b7a4d846f526" width="200" height="100">|
| 10 popsicle sticks| [Amazon](https://www.amazon.com/gp/product/B08BZSNVSQ)|<img src="https://github.com/user-attachments/assets/b28e239e-7de9-4ed8-b0d9-d221ec426c9a" width="100" height="100">|
| Battery pack when mobile|[Adafruit](https://www.adafruit.com/product/3905)|<img src="https://github.com/user-attachments/assets/a447f1aa-ab6f-475a-ba90-896815e2cebe" width="100" height="100">|
| 2 x L9110|[L9110](https://www.amazon.com/HiLetgo-H-bridge-Stepper-Controller-Arduino/dp/B00M0F243E)|<img src="https://github.com/user-attachments/assets/725afd47-e233-48fa-a526-6681a73b5cbb" width="100" height="100">|
| Wheels and Motors| [Wheels](https://www.amazon.com/gp/product/B0CG1C7T8J)|<img src="https://github.com/user-attachments/assets/5d096c64-0a00-4735-a2d5-15d49f6d733f" width="100" height="100">|
| 400 point breadboard | [Amazon](https://www.amazon.com/Breadborad-Solderless-Breadboards-Distribution-Connecting/dp/B082VYXDF1/)|<img src="https://github.com/user-attachments/assets/73578bff-e890-43b0-9ae0-a52ea4e461f7" width="100" height="100">
| Tissue Paper Roll | Left up to the reader|
| Small latching button | Optional - most any will do | It can help to turn the car/pico on/off|
| IR Receiver |[Amazon](https://www.amazon.com/gp/product/B06XYNDRGF)|<img src="https://github.com/user-attachments/assets/4f9df3a3-6206-4b6b-bc9b-b784a9361db0" width="100" height="100">>|

Note: I chose 2 motor controllers just because it seemed to be more balanced. It's not a requirement as the L9110 can handle 2 motors.

Note: The IR Receiver is optional if you don't want remote control abilities


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

<A href="/media/first_spin.mp4">First Spin Video</A>

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

<A href="/media/second_spin.mp4">Second Spin Video</A>

## Updated Placement:

Moved the battery holder closer and the flipped it the breadboard:

<img src="https://github.com/user-attachments/assets/e91a1727-8c62-4c10-9072-c1efffec6896" width="550" height="450">

## Third Spin
Things went better. After placing the battery pack closer to the center of gravity, the car followed the steps significantly more smoothly.

<A href="/media/third_spin.mp4">Third Spin Video</A>


## Fourth Spin
Added the IR sensor and integrated that with the current simple car api. In the end you can use just about any hobby remote with it. Make note of what code comes across as you hit the button. 

I chose:

| Button | Action|
| --------  | --------- |
| 1 | Move Forward|
| 2 | Move Backward|
| 4 | Move Left|
| 5 | Move Right|

and are mapped accordingly in `infra_car_control.py`:

![image](https://github.com/user-attachments/assets/9a03f0df-8a50-451f-af51-b6fd3ca48e7a)


Try to keep the IR sensor toward the edge, so it is more likely to receive the IR beam and not be hidden:

<img src="/media/car_ir.jpg">

**IR Receiver Connections**

| GPIO Pin | Connection|
| --------  | --------- |
| GPIO 12   | IN  (left leg) |
| GND PIN 18| GND (middle leg) |
| 3.3/Pin 36| VCC (right leg|

After correcting the left and right turns functions (I had them inverted) and realizing the wheels and chassis are pretty good but the don't always proceed in a 'perfect' straight line, the api was complete and minimally viable. The car can move forward, backward, turn left and turn right. This was overall a success and leaves plenty of opportunities to build upon.

## Pain Points
- Not everything went smoothly, the l9110 motor drivers went up in smoke - https://github.com/orgs/micropython/discussions/15938
- Don't try to troubleshoot when you are too tired - I made mistakes but learned more about the L298N (despite it's size and voltage drop, it works pretty well) - https://forums.raspberrypi.com/viewtopic.php?t=377361. When I ran out of l9110's I used an L298N for troubleshooting. There is a L298.py file to jump start in the repo for simple testing.
- I ultimately  simplified the api by simply using one l9110. As mentioned, you can choose to use 1 or 2.

## Credits
- IR code used from https://github.com/peterhinch/micropython_ir/tree/master 


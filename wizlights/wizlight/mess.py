import asyncio
from typing import List

from pywizlight import wizlight, PilotBuilder, discovery
from wizlight.my_bulbs import Group, bulb_details


BROADCAST_ADDRESS = "192.168.1.255"


async def discover() -> List[wizlight]:
    # Discover all bulbs in the network via broadcast datagram (UDP)
    # function takes the discovery object and returns a list with wizlight objects.
    discovered_bulbs = await discovery.discover_lights(broadcast_space=BROADCAST_ADDRESS)
    for bulb in discovered_bulbs:
        print(f"Found {bulb_details[bulb.mac]['name']}")
    return discovered_bulbs
    

async def toggle_bulbs_in_group(bulbs: List[wizlight], group: Group):
    group_bulbs = [bulb for bulb in bulbs if bulb_details[bulb.mac]['group'] == group]
    import ipdb; ipdb.set_trace()

    # for bulb in bulbs:
    #     if bulb_details[bulb.mac]['group'] == group:
    #         print(f"Turning on {bulb_details[bulb.mac]['name']}")
    #         await bulb.turn_on()

    
async def fade_table():
    table1 = wizlight

async def mess():
    """Sample code to work with bulbs."""
    

    found_bulbs = await discover()
    await toggle_bulbs_in_group(found_bulbs, Group.LivingRoom)

    import ipdb; ipdb.set_trace()

#     # Set up a standard light
#     light = wizlight("192.168.1.83")
#     # Set up the light with a custom port
#     #light = wizlight("your bulb's IP address", port=12345)

#     # The following calls need to be done inside an asyncio coroutine
#     # to run them fron normal synchronous code, you can wrap them with
#     # asyncio.run(..).

#     # Turn on the light into "rhythm mode"
#     await light.turn_on(PilotBuilder())

#     # Set bulb brightness
#     await light.turn_on(PilotBuilder(brightness=255))

#     # Set bulb brightness (with async timeout)
#     timeout = 10
#     await asyncio.wait_for(light.turn_on(PilotBuilder(brightness=255)), timeout)

#     # Set bulb to warm white
#     await light.turn_on(PilotBuilder(warm_white=255))

#     # Set RGB values
#     # red to 0 = 0%, green to 128 = 50%, blue to 255 = 100%
#     await light.turn_on(PilotBuilder(rgb=(0, 128, 255)))

#     # Get the current color temperature, RGB values
#     state = await light.updateState()
#     print(state.get_colortemp())
#     red, green, blue = state.get_rgb()
#     print(f"red {red}, green {green}, blue {blue}")

#     # Start a scene
#     await light.turn_on(PilotBuilder(scene=4))  # party

#     # Get the name of the current scene
#     state = await light.updateState()
#     print(state.get_scene())

#     # Get the features of the bulb
#     bulb_type = await bulbs[0].get_bulbtype()
#     # returns true if brightness is supported
#     print(bulb_type.features.brightness)
#     print(bulb_type.features.color)  # returns true if color is supported
#     # returns true if color temperatures are supported
#     print(bulb_type.features.color_tmp)
#     print(bulb_type.features.effect)  # returns true if effects are supported
#     print(bulb_type.kelvin_range.max)  # returns max kelvin in in INT
#     print(bulb_type.kelvin_range.min)  # returns min kelvin in in INT
#     print(bulb_type.name)  # returns the module name of the bulb

#     # Turns the light off
#     # await light.turn_off()

#     # Do operations on multiple lights parallely
#     #bulb1 = wizlight("<your bulb1 ip>")
#     #bulb2 = wizlight("<your bulb2 ip>")
#     # await asyncio.gather(bulb1.turn_on(PilotBuilder(brightness = 255)),
#     #    bulb2.turn_on(PilotBuilder(warm_white = 255)), loop = loop)

loop = asyncio.get_event_loop()
loop.run_until_complete(mess())

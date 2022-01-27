bl_info = {
    "name": "KCL Creator",
    "author": "Bear & BillyNoodles",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "3D View > Properties Panel > KCL Creator",
    "description": "Helps create KCL files in Blender",
    "warning": "",
    "doc_url": "",
    "category": "Export",
}

import os
import bpy
import random
from bpy.types import Operator
from bpy_extras.io_utils import ExportHelper

flag = "mat"
effect = 0
variant = 0
variantnum = 0
hexconv = 256
effectnum = 0
objectname = 'name'
LowerUnits = 30
InclAngle = 45

        
class DropDown(bpy.types.PropertyGroup):
    
     # Defines the list of Flags and variants
    enum : bpy.props.EnumProperty(
        name= "Flag",
        description= "",
        items= [('OP1', "Road", ""),
                ('OP2', "Slippery Road 1", ""),
                ('OP3', "Weak Off-road", ""),
                ('OP4', "Off-road", ""),
                ('OP5', "Heavy Off-road", ""),
                ('OP6', "Slippery Road 2", ""),
                ('OP7', "Boost Panel", ""),
                ('OP8', "Boost Ramp", ""),
                ('OP9', "Jump Pad", ""),
                ('OP10', "Solid Fall", ""),
                ('OP11', "Moving Road", ""),
                ('OP12', "Wall", ""),
                ('OP13', "Invisible Wall", ""),
                ('OP14', "Fall Boundary", ""),
                ('OP15', "Cannon Activator", ""),
                ('OP16', "Half-Pipe Ramp", ""),
                ('OP17', "Gravity Road", ""),
                ('OP18', "Sound Trigger", ""),
                ('OP19', "Effect Trigger", "")
            ]
        )
        
    trickable : bpy.props.EnumProperty(
        name= "Trickable?",
        description= "",
        items= [('NOTTRICKABLE', "No", ""),
                ('TRICKABLE', "Yes", "")
            ]
        )

    slot : bpy.props.EnumProperty(
        name= "Slot",
        description= "",
        items= [('LC', "Luigi Circuit", ""),
                ('MMM', "Moo Moo Meadows", ""),
                ('MG', "Mushroom Gorge", ""),
                ('TF', "Toad's Factory", ""),
                ('MC', "Mario Circuit", ""),
                ('CM', "Coconut Mall", ""),
                ('DKS', "DK Summit", ""),
                ('WGM', "Wario's Gold Mine", ""),
                ('DC', "Daisy Circuit", ""),
                ('KC', "Koopa Cape", ""),
                ('MT', "Maple Treeway", ""),
                ('GV', "Grumble Volcano", ""),
                ('DDR', "Dry Dry Ruins", ""),
                ('MH', "Moonview Highway", ""),
                ('BC', "Bowser's Castle", ""),
                ('RR', "Rainbow Road", ""),
                ('rPB', "GCN Peach Beach", ""),
                ('rYF', "DS Yoshi Falls", ""),
                ('rGV2', "SNES Ghost Valley 2", ""),
                ('rMR', "N64 Mario Raceway", ""),
                ('rSL', "N64 Sherbet Land", ""),
                ('rSGB', "GBA Shy Guy Beach", ""),
                ('rDS', "DS Delfino Square", ""),
                ('rWS', "GCN Waluigi Stadium", ""),
                ('rDH', "DS Desert Hills", ""),
                ('rBC3', "GBA Bowser Castle 3", ""),
                ('rDKJP', "N64 DK's Jungle Parkway", ""),
                ('rMC', "GCN Mario Circuit", ""),
                ('rMC3', "SNES Mario Circuit 3", ""),
                ('rPG', "DS Peach Gardens", ""),
                ('rDKM', "GCN DK Mountain", ""),
                ('rBC', "N64 Bowser's Castle", "")
            ]
        )
        
    # Road variant Enumerator
    roadvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('ROAD1', "Asphalt", ""),
                ('ROAD2', "Dirt with GFX (Only slots DKJP and DKM)", ""),
                ('ROAD3', "Dirt without GFX", ""),
                ('ROAD4', "Smooth", ""),
                ('ROAD5', "Wood", ""),
                ('ROAD6', "Snow", ""),
                ('ROAD7', "Metal Grate", ""),
                ('ROAD8', "Normal, but the sound cuts off", ""),
                ('ROAD9', "Normal road, different sound", ""),
                ('ROAD10', "Carpet", ""),
                ('ROAD11', "Grass, gfx on GCN DK Mountain", ""),
                ('ROAD12', "Normal road, used on green mushrooms", ""),
                ('ROAD13', "Grass", ""),
                ('ROAD14', "Glass road with SFX", ""),
                ('ROAD15', "Dirt (unused)", ""),
                ('ROAD16', "Normal road, SFX on Rainbow Road", "")
            ]
        )
    # Slippery Road 1 variant Enumerator
    sliproad1variant : bpy.props.EnumProperty(
        name= "Variant",
        description= "Slippery, does not slow you down.",
        items= [('SLIPROAD1OP1', "White Sand", ""),
                ('SLIPROAD1OP2', "Dirt", ""),
                ('SLIPROAD1OP3', "Water", ""),
                ('SLIPROAD1OP4', "Snow", ""),
                ('SLIPROAD1OP5', "Grass", ""),
                ('SLIPROAD1OP6', "Yellow Sand", ""),
                ('SLIPROAD1OP7', "Sand, No GFX", ""),
                ('SLIPROAD1OP8', "Dirt, No GFX", "")
            ]
        )
    # Weak Off-Road variant Enumerator
    weakoffroadvariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "",
        items= [('WEAKOFFROADOP1', "White Sand", ""),
                ('WEAKOFFROADOP2', "Dirt", ""),
                ('WEAKOFFROADOP3', "Water", ""),
                ('WEAKOFFROADOP4', "Snow", ""),
                ('WEAKOFFROADOP5', "Grass", ""),
                ('WEAKOFFROADOP6', "Yellow Sand", ""),
                ('WEAKOFFROADOP7', "Sand, No GFX", ""),
                ('WEAKOFFROADOP8', "Dirt, No GFX", "")
            ]
        )
    # Off-Road variant Enumerator
    offroadvariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "",
        items= [('OFFROADOP1', "Sand", ""),
                ('OFFROADOP2', "Dirt", ""),
                ('OFFROADOP3', "Mud", ""),
                ('OFFROADOP4', "Water, No GFX", ""),
                ('OFFROADOP5', "Grass", ""),
                ('OFFROADOP6', "Sand, lighter GFX", ""),
                ('OFFROADOP7', "Gravel", ""),
                ('OFFROADOP8', "Carpet", "")
            ]
        )
    # Heavy Off-Road variant Enumerator
    heavyoffroadvariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "",
        items= [('HEAVYOFFROADOP1', "Sand", ""),
                ('HEAVYOFFROADOP2', "Dirt", ""),
                ('HEAVYOFFROADOP3', "Mud", ""),
                ('HEAVYOFFROADOP4', "Flowers", ""),
                ('HEAVYOFFROADOP5', "Grass", ""),
                ('HEAVYOFFROADOP6', "Snow", ""),
                ('HEAVYOFFROADOP7', "Sand", ""),
                ('HEAVYOFFROADOP8', "Dirt, No GFX", "")
            ]
        )
    # Slippery Road 2 variant Enumerator
    sliproad2variant : bpy.props.EnumProperty(
        name= "Variant",
        description= "Slippery and slightly slows you down.",
        items= [('SLIPROAD2OP1', "Ice", ""),
                ('SLIPROAD2OP2', "Mud", ""),
                ('SLIPROAD2OP3', "Water", ""),
                ('SLIPROAD2OP4', "Normal Road, Different sound", "")
            ]
        )
    # Boost Panel variant Enumerator
    boostpanvariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "",
        items= [('BOOSTPANOP1', "Default", ""),
                ('BOOSTPANOP2', "If used, and casino_roulette is near, the road slowly rotates everything nearby counterclockwise. Used in Chain Chomp Wheel.", ""),
                ('BOOSTPANOP3', "Unknown. Unused.", "")
            ]
        )
    # Boost Ramp variant Enumerator
    boostrampvariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "Do not use collision effectect 'Trickable' with this flag",
        items= [('BOOSTRAMPOP1', "2 Flips", ""),
                ('BOOSTRAMPOP2', "1 Flip", ""),
                ('BOOSTRAMPOP3', "No flips", "")
            ]
        )
    # Jump Pad variant Enumerator
    jumppadvariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "Higher stages mean approximately longer air time and more distance.",
        items= [('JUMPPADOP1', "Stage 2, used in GBA Bowser Castle 3", ""),
                ('JUMPPADOP2', "Stage 3, used in SNES Ghost Valley 2", ""),
                ('JUMPPADOP3', "Stage 1, used in GBA Shy Guy Beach", ""),
                ('JUMPPADOP4', "Stage 4, used in Mushroom Gorge", ""),
                ('JUMPPADOP5', "Stage 5, Bouncy mushroom (Causes off-road glitch)", ""),
                ('JUMPPADOP6', "Stage 4, used in Chain Chomp Wheel", ""),
                ('JUMPPADOP7', "Stage 2, used in DS Yoshi Falls and Funky Stadium", ""),
                ('JUMPPADOP8', "Stage 4, unused.", "")
            ]
        )
    # Solid Fall variant Enumerator
    solidfallvariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "",
        items= [('SOLIDFALLOP1', "Sand", ""),
                ('SOLIDFALLOP2', "Sand/Underwater", ""),
                ('SOLIDFALLOP3', "Unknown.", ""),
                ('SOLIDFALLOP4', "Ice", ""),
                ('SOLIDFALLOP5', "Dirt", ""),
                ('SOLIDFALLOP6', "Grass", ""),
                ('SOLIDFALLOP7', "Wood", ""),
                ('SOLIDFALLOP8', "Unknown.", "")
            ]
        )
    # Moving Road variant Enumerator
    movingroadvariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "",
        items= [('MOVINGROADOP1', "Follows a route, pulling the player down", ""),
                ('MOVINGROADOP2', "Follows a route, strongly pulling the player down.", ""),
                ('MOVINGROADOP3', "Follows a route from the start of the path to the end of it.", ""),
                ('MOVINGROADOP4', "No route, pulls the player down, unable to move from it.", ""),
                ('MOVINGROADOP5', "Moving asphalt, unused.", ""),
                ('MOVINGROADOP6', "Moving asphalt, unused.", ""),
                ('MOVINGROADOP7', "Moving road, unused.", ""),
                ('MOVINGROADOP8', "Moving road, unused..", "")
            ]
        )
    # Wall variant Enumerator
    wallvariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "",
        items= [('WALLOP1', "Normal", ""),
                ('WALLOP2', "Rock", ""),
                ('WALLOP3', "Metal", ""),
                ('WALLOP4', "Wood", ""),
                ('WALLOP5', "Ice", ""),
                ('WALLOP6', "Bush", ""),
                ('WALLOP7', "Rope", ""),
                ('WALLOP8', "Rubber", "")
            ]
        )
    # Invisible Wall variant Enumerator
    invwallvariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "",
        items= [('INVWALLOP1', "Default", ""),
                ('INVWALLOP2', "Spark and character wall hit voice", "")
            ]
        )
    # Fall Boundary variant Enumerator
    fallvariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "",
        items= [('FALLOP1', "Air Fall", ""),
                ('FALLOP2', "Water", ""),
                ('FALLOP3', "Lava", ""),
                ('FALLOP4', "Icy Water (Ice on respawn)", ""),
                ('FALLOP5', "Lava, No GFX", ""),
                ('FALLOP6', "Burning air fall", ""),
                ('FALLOP7', "Quicksand", ""),
                ('FALLOP8', "Short Fall", "")
                
            ]
        )
    # Cannon Activator variant enumerator
    cannonvariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "",
        items= [('CANNONOP1', "To point 0", ""),
                ('CANNONOP2', "To point 1", ""),
                ('CANNONOP3', "To point 2", ""),
                ('CANNONOP4', "To point 3 (unused)", ""),
                ('CANNONOP5', "To point 4 (unused)", ""),
                ('CANNONOP6', "To point 5 (unused)", ""),
                ('CANNONOP7', "To point 6 (unused)", ""),
                ('CANNONOP8', "To point 7 (unused)", "")
                
            ]
        )
    # Half-pipe variant enumerator
    halfpipevariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "Best used with Invisible Wall, although not needed to function.",
        items= [('HALFPIPEOP1', "Default", ""),
                ('HALFPIPEOP2', "Boost pad applied", "")
            ]
        )
    # Gravity Road variant enumerator
    gravityroadvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('GRAVITYROADOP1', "Wood", ""),
                ('GRAVITYROADOP2', "Gravel, different impact SFX", ""),
                ('GRAVITYROADOP3', "Carpet", ""),
                ('GRAVITYROADOP4', "Dirt, no GFX", ""),
                ('GRAVITYROADOP5', "Sand, different impact and drift SFX, no GFX", ""),
                ('GRAVITYROADOP6', "Normal road, SFX on Rainbow Road", ""),
                ('GRAVITYROADOP7', "Normal road", ""),
                ('GRAVITYROADOP8', "Mud with GFX.", "")
            ]
        )
    # Luigi Circuit variant enumerator
    lcvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('LCOP1', "No audience noise", ""),
                ('LCOP2', "Soft audience noise", ""),
                ('LCOP3', "Audience noise (race starts with this)", ""),
                ('LCOP4', "Loud audience noise", "")
            ]
        )
    # Mushroom Gorge variant enumerator
    mgvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('MGOP1', "Deactivate all", ""),
                ('MGOP2', "Enable cave SFX + echo", "")
            ]
        )
    # Toad's Factory variant enumerator
    tfvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('TFOP1', "Sounds Off", ""),
                ('TFOP2', "Hydraulic press area", ""),
                ('TFOP3', "Shipping dock area", ""),
                ('TFOP4', "Moving belt area", ""),
                ('TFOP5', "Steam Room", ""),
                ('TFOP6', "Restart music at beginning", ""),
                ('TFOP7', "Bulldozer area", ""),
                ('TFOP8', "Audience area", "")
            ]
        )
    # Mario Circuit variant enumerator
    mcvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('MCOP1', "Deactivates echo.", ""),
                ('MCOP2', "Weak echo.", ""),
                ('MCOP3', "Loud echo.", "")
            ]
        )
    # Coconut Mall variant enumerator
    cmvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('CMOP1', "Resets all sound triggers. Shopping mall ambience requires this to play", ""),
                ('CMOP2', "Weak shopping mall ambience + disables echo", ""),
                ('CMOP3', "Loud shopping mall ambience + strong echo", ""),
                ('CMOP4', "Resets all sound triggers and prevents shopping mall ambience from playing until option 1 is hit again.", "")
            ]
        )
    # DK Summit variant enumerator
    dksvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('DKSOP1', "Deactivates cheering.", ""),
                ('DKSOP2', "Weak cheering ambience.", ""),
                ('DKSOP3', "Loud cheering ambience.", ""),
                ('DKSOP4', "Loudest cheering ambience.", ""),
                ('DKSOP5', "Enables cheering when going off half-pipe ramps.", "")
            ]
        )
    # Wario's Gold Mine variant enumerator
    wgmvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('WGMOP1', "Music change (outside)", ""),
                ('WGMOP2', "Music change (cave) + gentle echo", ""),
                ('WGMOP3', "Echo", ""),
                ('WGMOP4', "Strong Echo", "")
            ]
        )
    # Daisy Circuit variant enumerator
    dcvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('DCOP1', "Deactivate echo", ""),
                ('DCOP2', "Weak echo", ""),
                ('DCOP3', "Echo", "")
            ]
        )
    # Koopa Cape variant enumerator
    kcvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('KCOP1', "Music change (normal)", ""),
                ('KCOP2', "Music change (normal), echo.", ""),
                ('KCOP3', "Stronger echo.", ""),
                ('KCOP4', "Music change (underwtaer), water ambience enabled when entering from options 1, 6 or 7, disabled otherwise.", ""),
                ('KCOP5', "Strongest echo, water ambience enabled.", ""),
                ('KCOP6', "Music change (normal), strongest echo, water ambience enabled when entering from option 4.", ""),
                ('KCOP7', "Music change (riverside)", "")
            ]
        )
    # Maple Treeway variant enumerator
    mtvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('MTOP1', "Deactivate echo and wind ambience.", ""),
                ('MTOP2', "No effect.", ""),
                ('MTOP3', "Weak echo.", ""),
                ('MTOP4', "Loud echo.", ""),
                ('MTOP5', "Enabled wind ambience, deactivates echo.", "")
            ]
        )
    # Grumble Volcano variant enumerator
    gvvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('GVOP1', "Deactivate echo", ""),
                ('GVOP2', "Weak echo, toggles after two seconds.", ""),
                ('GVOP3', "Loud echo, toggles after one second.", ""),
                ('GVOP4', "Loud echo, toggles after two seconds.", "")
            ]
        )
    # Dry Dry Ruins variant enumerator
    ddrvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('DDROP1', "Music change (normal)", ""),
                ('DDROP2', "Music change (indoors, where the bats come from the sides)", ""),
                ('DDROP3', "Music change (indoors, where the half-pipes are)", ""),
                ('DDROP4', "Music change (indoors, where the pokeys are)", "")
            ]
        )
    # Moonview Highway variant enumerator
    mhvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('MHOP1', "Deactivate city ambience, default music.", ""),
                ('MHOP2', "Stage 2, Weak city ambience, adds flute to music.", ""),
                ('MHOP3', "Stage 4, Louder city ambience, disable echo.", ""),
                ('MHOP4', "Stage 5, Loudest city ambience, disable echo.", ""),
                ('MHOP5', "Stage 3, Loud city ambience, enable echo.", ""),
                ('MHOP6', "Stage 1, Weakest city ambience, enable echo.", "")
            ]
        )
    # Bowser's Castle variant enumerator
    bcvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('BCOP1', "Disable one-time use sound trigger (like Bowser's howl)", ""),
                ('BCOP2', "Bowser's howl + echo. Put option 8 at the end of a turn to be able to reuse Bowser's howl.", ""),
                ('BCOP3', "Sound distortion + echo", ""),
                ('BCOP4', "Deactivate sound distortion + echo", ""),
                ('BCOP5', "Add drums + echo on music + koopaBall/koopaFigure SFX", ""),
                ('BCOP6', "Deactivate koopaBall/koopaFigure SFX", ""),
                ('BCOP7', "Add drums without echo", ""),
                ('BCOP8', "Back to normal. Allow reuse for one-time use sound trigger.", "")
            ]
        )
    # Rainbow Road variant enumerator
    rrvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('RROP1', "Deactivator", ""),
                ('RROP2', "Gate sound 1 (add a deactivator before and after if you use only one gate)", ""),
                ('RROP3', "Boost pad star ring sound 1", ""),
                ('RROP4', "Boost pad star ring sound 2", ""),
                ('RROP5', "Boost pad star ring sound 3", ""),
                ('RROP6', "Boost pad star ring sound 4", ""),
                ('RROP7', "Tunnel sound (add a deactivator to stop it)", "")
            ]
        )
    # N64 Mario Raceway variant enumerator
    rmrvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('RMROP1', "Deactivates cheering.", ""),
                ('RMROP2', "Loud cheering.", ""),
                ('RMROP3', "Louder cheering.", ""),
                ('RMROP4', "Weak cheering.", "")
            ]
        )
    # N64 Sherbet Land variant enumerator
    rslvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('RSLOP1', "Deactivate all.", ""),
                ('RSLOP2', "Cave echo.", ""),
                ('RSLOP3', "Cave SFX.", "")
            ]
        )
    # DS Delfino Square variant enumerator
    rdsvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('RDSOP1', "Unknown. In a position such that a player may collide with this trigger if they complete the dock shortcut.", ""),
                ('RDSOP2', "Very, very distant whistles, cheers and chatter from spectators.", ""),
                ('RDSOP3', "Very distant whistles, cheers and chatter from spectators.", ""),
                ('RDSOP4', "Distant whistles, cheers and chatter from specators.", ""),
                ('RDSOP5', "Whistles, cheers and chatter from spectators.", ""),
                ('RDSOP6', "Single wid gust just before dock section.", ""),
                ('RDSOP7', "No spectator ambience.", ""),
                ('RDSOP8', "The same as last, used in between triggers of last type.", "")
            ]
        )
    # N64 DK's Jungle Parkway variant enumerator
    rdkjpvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('RDKJPOP1', "No jungle ambience. Used near water sections.", ""),
                ('RDKJPOP2', "Jungle ambience (bird squawks, insect hum, animal roar) Used as a buffer between types above and below.", ""),
                ('RDKJPOP3', "Intense jungle ambience, used in areas of deep forest.", ""),
                ('RDKJPOP4', "Cave ambience.", "")
            ]
        )
    # GCN Mario Circuit variant enumerator
    rmcvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('RMCOP1', "No echo", ""),
                ('RMCOP2', "Weak echo", ""),
                ('RMCOP3', "Loud echo", "")
            ]
        )
    # GCN DK Mountain variant enumerator
    rdkmvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('RDKMOP1', "Deactivate all.", ""),
                ('RDKMOP2', "Jungle SFX (animals)", ""),
                ('RDKMOP3', "Water + wind SFX", "")
            ]
        )
    # N64 Bowser's Castle variant enumerator
    rbcvariant : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('RBCOP1', "Disable one-time use sound trigger (like Bowser's howl)", ""),
                ('RBCOP2', "Turns lava SFX off + disables echo", ""),
                ('RBCOP3', "Bowser's howl + echo. Put option 1 at the end of a turn to be able to reuse Bowser's howl.", ""),
                ('RBCOP4', "Turns lava SFX off", ""),
                ('RBCOP5', "Turns lava SFX off + echo", ""),
                ('RBCOP6', "Echo", ""),
                ('RBCOP7', "Strong echo", "")
            ]
        )
    # Effect Trigger variant enumerator
    effecttriggervariant : bpy.props.EnumProperty(
        name= "Variant",
        description= "",
        items= [('EFFECTOP1', "BRSTM reset", ""),
                ('EFFECTOP2', "Enable shadow effect", ""),
                ('EFFECTOP3', "Water splash (pocha) (only reusable if a fall boundary is triggered)", ""),
                ('EFFECTOP4', "starGate door activation", ""),
                ('EFFECTOP5', "Half-pipe cancellation", ""),
                ('EFFECTOP6', "Coin despawner", ""),
                ('EFFECTOP7', "Smoke effect on the player when going through dark smoke (truckChimSmkW)", "")
            ]
        )
    # Pocha number enumerator
    pocha : bpy.props.EnumProperty(
        name= "Pocha number",
        description= "Reference this number in KMP Setting 1 of pocha object",
        items= [('POCHA1', "1", ""),
                ('POCHA2', "2", ""),
                ('POCHA3', "3", ""),
                ('POCHA4', "4", ""),
                ('POCHA5', "5 - Leaf splash on Moonview Highway slot", ""),
                ('POCHA6', "6", ""),
                ('POCHA7', "7", ""),
                ('POCHA8', "8", "")
            ]
        )

class APPLY_OT_apply_op(Operator):
    bl_idname = 'apply.apply_op'
    bl_label = 'Apply'
    bl_description = 'Apply Flag'
    
    @classmethod 
    def poll(cls, context):
        ob = context.active_object
        return ob and ob.type == 'MESH'
    
    def flagmat(self, flag, ob):
# Get material
      mat = bpy.data.materials.get(flag)
      if mat is None:
    # create material
          mat = bpy.data.materials.new(name=flag)
          mat.diffuse_color = (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),1)

# Assign it to object
      if ob.data.materials:
    # assign to 1st material slot
          ob.data.materials[0] = mat
      else:
    # no slots
          ob.data.materials.append(mat)
          
    def rename(self, objectname, ob):
        ob.name = objectname
        ob.data.name = objectname

    def execute(self, context):
        ob = context.active_object
        self.flagmat(flag, ob)
        self.rename(objectname, ob)
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        ob = context.active_object
        self.flagmat(flag, ob)
        self.rename(objectname, ob)
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
        return {'FINISHED'}

class EXPORT_OT_flag_op(Operator, ExportHelper):
    bl_idname = 'export.flag_op'
    bl_label = 'Flag'
    bl_description = 'Export Flag File'
    
    filename_ext = ".flag"  # ExportHelper mixin class uses this
    def execute(self, context):
        obs = filter(lambda ob: ob.type == 'MESH', context.scene.collection.all_objects)
        fp = self.filepath
        
        with open(fp, 'w') as f:   
            for ob in obs:
                f.write(ob.name + " = 0x" + ob.name[-4:] + "\n")
        
        return{'FINISHED'}

class EXPORT_OT_kcl_op(Operator, ExportHelper):
    bl_idname = 'export.kcl_op'
    bl_label = 'KCL'
    bl_description = 'Export KCL File'
    
    ScaleValue : bpy.props.FloatProperty(name= "Scale", default=1, precision=2, min=0, max=1000)
    
    KCLSizes = [("Medium", "Medium", ""),
        ("Small", "Small", ""),
        ("Chary", "Chary", "")]
    KCLSize    : bpy.props.EnumProperty(name="Complexity", items=KCLSizes)
    
    DropUnused : bpy.props.BoolProperty(name="Drop Unused Tris")
    DropInval  : bpy.props.BoolProperty(name="Drop Invalid Tris")
    DropFixed  : bpy.props.BoolProperty(name="Drop Fixed Tris")
    RmFacedown : bpy.props.BoolProperty(name="Remove Facedown Tris")
    RmFaceup   : bpy.props.BoolProperty(name="Remove Faceup Walls")
    ConvFaceup : bpy.props.BoolProperty(name="Convert Faceup Walls")
    WeakWalls  : bpy.props.BoolProperty(name="Weak Walls")
    LowerWalls  : bpy.props.BoolProperty(name="Lower Walls")
    
    filename_ext = ".kcl"  # ExportHelper mixin class uses this
    def execute(self, context):
        obs = filter(lambda ob: ob.type == 'MESH', context.scene.collection.all_objects)
        fp = self.filepath
        
        with open(fp[:-4] + ".flag", 'w') as f:   
            for ob in obs:
                f.write(ob.name + " = 0x" + ob.name[-4:] + "\n")
        
        bpy.ops.export_scene.obj(
            filepath=fp, 
            group_by_object=True,
            use_blen_objects=False,
            use_normals=True,
            use_triangles=True,
            use_materials=False,
            global_scale=self.ScaleValue)
            
        if self.LowerWalls:
            LowerUnits : bpy.props.FloatProperty(name="Units to Lower by", default=30,precision=2,min=20,max=50)
            InclAngle : bpy.props.FloatProperty(name="Inclination Angle",default=45,precision=2,min=0,max=180)
            
        command = "wkclt encode \"" + fp + "\" --kcl="
        command = command + ("DROPUNUSED," if self.DropUnused else "")
        command = command + ("DROPINVALID," if self.DropUnused else "")
        command = command + ("DROPFIXED," if self.DropFixed else "")
        command = command + ("RMFACEDOWN," if self.RmFacedown else "")
        command = command + ("RMFACEUP," if self.RmFaceup else "")
        command = command + ("CONVFACEUP," if self.ConvFaceup else "")
        command = command + ("WEAKWALLS," if self.WeakWalls else "")
        command = command + (self.KCLSize + " --kcl-script=lower-walls.txt --const lower=" + LowerUnits + ",degree=" + InclAngle if self.LowerWalls else "")
        command = command + self.KCLSize
        
        os.system(command)
                    
        return{'FINISHED'}
    
#class EXPORT_PT_export_settings(bpy.types.Panel):
#    bl_space_type = 'FILE_BROWSER'
#    bl_region_type = 'TOOL_PROPS'
#    bl_label = "Settings Panel"
#    bl_options = {'DEFAULT_CLOSED'}
#    
#    @classmethod
#    def poll(cls, context):
#        sfile = context.space_data
#        operator = sfile.active_operator
#        return operator.bl_idname == "EXPORT_OT_kcl_op"
#    
#    def draw(self, context):
#        layout = self.layout
#        layout.use_property_split = True
#        layout.use_property_decorate = False  # No animation.

#        sfile = context.space_data
#        operator = sfile.active_operator

#        layout.prop(operator, 'ScaleValue')


class KCL_PT_MainPanel(bpy.types.Panel):
    bl_label = "KCL Creator"
    bl_idname = "KCL_PT_MainPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "KCL Creator"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        KCLOp = scene.my_tool
        row = layout.row()
        row.prop(KCLOp, "enum")
        global flag
        global variant
        global effect
        global variantnum
        global effectnum
        global hexconv
        global objectname
        variantnum = 0
        variant = 0
        effect = 0
        effectnum = 0
        hexconv = 256
        flag = "_" + hex(variant)[2:4].zfill(2) + "_"
        
        def ChangeEffect(effect, effectnum):
            effect = effect + effectnum
            return effect              
        
        def EffectName(variant, variantnum, hexvariant):
            variantnum = variantnum + variant << 5
            variantnum = hex(variantnum + hexvariant)[2:6]
            return variantnum
        
        if KCLOp.enum == 'OP1':
            row = layout.row()
            row.prop(KCLOp, "roadvariant")  # Road variant
            
            if KCLOp.roadvariant == 'ROAD1':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    #print(objectname)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row() 
                    objectname = flag + "F" + str(EffectName(0, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    #print(objectname)
                    row.operator("apply.apply_op")
                              
            if KCLOp.roadvariant == 'ROAD2':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    #print(objectname)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    #print(objectname)
                    row.operator("apply.apply_op")
      
            if KCLOp.roadvariant == 'ROAD3':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.roadvariant == 'ROAD5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.roadvariant == 'ROAD9':
                variant = 23
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    #print(objectname)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row() 
                    objectname = flag + "F" + str(EffectName(0, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    #print(objectname)
                    row.operator("apply.apply_op")
                              
            if KCLOp.roadvariant == 'ROAD10':
                variant = 23
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    #print(objectname)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    #print(objectname)
                    row.operator("apply.apply_op")
      
            if KCLOp.roadvariant == 'ROAD10':
                variant = 23
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD11':
                variant = 23
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.roadvariant == 'ROAD12':
                variant = 23
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD13':
                variant = 23
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD14':
                variant = 23
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD15':
                variant = 23
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP2':
            row = layout.row()
            variant = 1
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "sliproad1variant") # Slippery Road 1 variant

            if KCLOp.sliproad1variant == "SLIPROAD1OP1":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
            
            if KCLOp.sliproad1variant == "SLIPROAD1OP2":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.sliproad1variant == "SLIPROAD1OP3":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.sliproad1variant == 'SLIPROAD1OP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.sliproad1variant == 'SLIPROAD1OP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.sliproad1variant == 'SLIPROAD1OP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.sliproad1variant == 'SLIPROAD1OP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.sliproad1variant == 'SLIPROAD1OP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP3':
            row = layout.row()
            variant = 2
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "weakoffroadvariant") # Weak Off-road variant

            if KCLOp.weakoffroadvariant == "WEAKOFFROADOP1":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.weakoffroadvariant == "WEAKOFFROADOP2":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.weakoffroadvariant == "WEAKOFFROADOP3":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP4':
            row = layout.row()
            variant = 3
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "offroadvariant") # Off-road variant
            
            if KCLOp.offroadvariant == 'OFFROADOP1':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.offroadvariant == "OFFROADOP2":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.offroadvariant == "OFFROADOP3":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.offroadvariant == 'OFFROADOP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.offroadvariant == 'OFFROADOP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.offroadvariant == 'OFFROADOP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.offroadvariant == 'OFFROADOP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.offroadvariant == 'OFFROADOP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP5':
            row = layout.row()
            variant = 4
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "heavyoffroadvariant") # Heavy off-road variant

            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP1':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.heavyoffroadvariant == "HEAVYOFFROADOP2":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.heavyoffroadvariant == "HEAVYOFFROADOP3":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP6':
            row = layout.row()
            variant = 5
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "sliproad2variant") # Slippery road 2 variant

            if KCLOp.sliproad2variant == "SLIPROAD2OP1":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
            
            if KCLOp.sliproad2variant == "SLIPROAD2OP2":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.sliproad2variant == "SLIPROAD2OP3":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.sliproad2variant == 'SLIPROAD2OP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP7':
            row = layout.row()
            variant = 6
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "boostpanvariant") # Boost panel variant

            if KCLOp.boostpanvariant == 'BOOSTPANOP1':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                              
            if KCLOp.boostpanvariant == 'BOOSTPANOP2':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
      
            if KCLOp.roadvariant == 'BOOSTPANOP3':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP8':
            row = layout.row()
            variant = 7
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "boostrampvariant") # Boost ramp variant

            if KCLOp.boostrampvariant == "BOOSTRAMPOP1":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.boostrampvariant == "BOOSTRAMPOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.boostrampvariant == "BOOSTRAMPOP3":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

        if KCLOp.enum == 'OP9':
            row = layout.row()
            variant = 8
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "jumppadvariant") # Jump Pad variant

            if KCLOp.jumppadvariant == "JUMPPADOP1":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP3":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP4":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP5":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP6":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP7":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP8":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

        if KCLOp.enum == 'OP10':
            row = layout.row()
            variant = 10
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "solidfallvariant") # Solid Fall variant

            if KCLOp.solidfallvariant == "SOLIDFALLOP1":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP3":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP4":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP5":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP6":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP7":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP8":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

        if KCLOp.enum == 'OP11':
            row = layout.row()
            variant = 11
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "movingroadvariant") # Moving Road variant

            if KCLOp.movingroadvariant == 'MOVINGROADOP1':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                              
            if KCLOp.movingroadvariant == 'MOVINGROADOP2':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
      
            if KCLOp.movingroadvariant == 'MOVINGROADOP3':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.movingroadvariant == 'MOVINGROADOP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.movingroadvariant == 'MOVINGROADOP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.movingroadvariant == 'MOVINGROADOP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.movingroadvariant == 'MOVINGROADOP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.movingroadvariant == 'MOVINGROADOP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP12':
            row = layout.row()
            variant = 12
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "wallvariant") # Wall variant

            if KCLOp.wallvariant == "WALLOP1":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP3":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP4":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP5":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP6":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP7":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP8":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

        if KCLOp.enum == 'OP13':
            row = layout.row()
            variant = 13
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "invwallvariant") # Invisible Wall variant

            if KCLOp.invwallvariant == "INVWALLOP1":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.invwallvariant == "INVWALLOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")
        
        if KCLOp.enum == 'OP14':
            row = layout.row()
            variant = 16
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "fallvariant")

            if KCLOp.fallvariant == "FALLOP1":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.fallvariant == "FALLOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.fallvariant == "FALLOP3":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.fallvariant == "FALLOP4":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.fallvariant == "FALLOP5":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.fallvariant == "FALLOP6":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.fallvariant == "FALLOP7":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.fallvariant == "FALLOP8":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

        if KCLOp.enum == 'OP15':
            row = layout.row()
            variant = 17
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "cannonvariant")

            if KCLOp.cannonvariant == "CANNONOP1":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.cannonvariant == "CANNONOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.cannonvariant == "CANNONOP3":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.cannonvariant == "CANNONOP4":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.cannonvariant == "CANNONOP5":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.cannonvariant == "CANNONOP6":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.cannonvariant == "CANNONOP7":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.cannonvariant == "CANNONOP8":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

        if KCLOp.enum == 'OP16':
            row = layout.row()
            variant = 19
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "halfpipevariant") # Half pipe variant

            if KCLOp.halfpipevariant == "HALFPIPEOP1":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.halfpipevariant == "HALFPIPEOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

        if KCLOp.enum == 'OP17':
            row = layout.row()
            variant = 22
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "gravityroadvariant") # Off-road variant
            
            if KCLOp.gravityroadvariant == 'GRAVITYROADOP1':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.gravityroadvariant == "GRAVITYROADOP2":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.gravityroadvariant == "GRAVITYROADOP3":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.gravityroadvariant == 'GRAVITYROADOP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.gravityroadvariant == 'GRAVITYROADOP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.gravityroadvariant == 'GRAVITYROADOP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.gravityroadvariant == 'GRAVITYROADOP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP18':
            row = layout.row()
            variant = 24
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "slot")

            if KCLOp.slot == "LC":
                row = layout.row()
                row.prop(KCLOp, "lcvariant")

                if KCLOp.lcvariant == "LCOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.lcvariant == "LCOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.lcvariant == "LCOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.lcvariant == "LCOP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "MMM":
                row = layout.row()
            
            if KCLOp.slot == "MG":
                row = layout.row()
                row.prop(KCLOp, "mgvariant")

                if KCLOp.mgvariant == "MGOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.mgvariant == "MGOP2":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "TF":
                row = layout.row()
                row.prop(KCLOp, "tfvariant")

                if KCLOp.tfvariant == "TFOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.tfvariant == "TFOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.tfvariant == "TFOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.tfvariant == "TFOP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.tfvariant == "TFOP5":
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.tfvariant == "TFOP6":
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.tfvariant == "TFOP7":
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.tfvariant == "TFOP8":
                    objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "MC":
                row = layout.row()
                row.prop(KCLOp, "mcvariant")

                if KCLOp.tfvariant == "MCOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.tfvariant == "MCOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.tfvariant == "MCOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "CM":
                row = layout.row()
                row.prop(KCLOp, "cmvariant")

                if KCLOp.cmvariant == "CMOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.cmvariant == "CMOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.cmvariant == "CMOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.cmvariant == "CMOP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.cmvariant == "CMOP5":
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.cmvariant == "CMOP6":
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "DKS":
                row = layout.row()
                row.prop(KCLOp, "dksvariant")

                if KCLOp.dksvariant == "DKSOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.dksvariant == "DKSOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.dksvariant == "DKSOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.dksvariant == "DKSOP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "WGM":
                row = layout.row()
                row.prop(KCLOp, "wgmvariant")

                if KCLOp.wgmvariant == "WGMOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.wgmvariant == "WGMOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.wgmvariant == "WGMOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.wgmvariant == "WGMOP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.wgmvariant == "WGMOP5":
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "DC":
                row = layout.row()
                row.prop(KCLOp, "dcvariant")

                if KCLOp.dcvariant == "DCOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.dcvariant == "DCOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.dcvariant == "DCOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "KC":
                row = layout.row()
                row.prop(KCLOp, "kcvariant")

                if KCLOp.kcvariant == "KCOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.kcvariant == "KCOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.kcvariant == "KCOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.kcvariant == "KCOP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.kcvariant == "KCOP5":
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.kcvariant == "KCOP6":
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.kcvariant == "KCOP7":
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "MT":
                row = layout.row()
                row.prop(KCLOp, "mtvariant")

                if KCLOp.mtvariant == "MTOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.mtvariant == "MTOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.mtvariant == "MTOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.mtvariant == "MTOP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.mtvariant == "MTOP5":
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "GV":
                row = layout.row()
                row.prop(KCLOp, "gvvariant")

                if KCLOp.gvvariant == "GVOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.gvvariant == "GVOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.gvvariant == "GVOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.gvvariant == "GVOP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "DDR":
                row = layout.row()
                row.prop(KCLOp, "ddrvariant")

                if KCLOp.ddrvariant == "DDROP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.ddrvariant == "DDROP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.ddrvariant == "DDROP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.ddrvariant == "DDROP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "MH":
                row = layout.row()
                row.prop(KCLOp, "mhvariant")

                if KCLOp.mhvariant == "MHOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.mhvariant == "MHOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.mhvariant == "MHOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.mhvariant == "MHOP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.mhvariant == "MHOP5":
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.mhvariant == "MHOP6":
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "BC":
                row = layout.row()
                row.prop(KCLOp, "bcvariant")

                if KCLOp.bcvariant == "BCOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.bcvariant == "BCOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.bcvariant == "BCOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.bcvariant == "BCOP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.bcvariant == "BCOP5":
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.bcvariant == "BCOP6":
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.bcvariant == "BCOP7":
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.bcvariant == "BCOP8":
                    objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "RR":
                row = layout.row()
                row.prop(KCLOp, "rrvariant")

                if KCLOp.rrvariant == "RROP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rrvariant == "RROP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rrvariant == "RROP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rrvariant == "RROP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rrvariant == "RROP5":
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rrvariant == "RROP6":
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rrvariant == "RROP7":
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "rPB":
                row = layout.row()

            if KCLOp.slot == "rYF":
                row = layout.row()

            if KCLOp.slot == "rGV2":
                row = layout.row()

            if KCLOp.slot == "rMR":
                row = layout.row()
                row.prop(KCLOp, "rmrvariant")

                if KCLOp.rmrvariant == "RMROP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rmrvariant == "RMROP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rmrvariant == "RMROP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "rSGB":
                row = layout.row()

            if KCLOp.slot == "rDS":
                row = layout.row()
                row.prop(KCLOp, "rdsvariant")

                if KCLOp.rdsvariant == "RDSOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rdsvariant == "RDSOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rdsvariant == "RDSOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rdsvariant == "RDSOP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rdsvariant == "RDSOP5":
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rdsvariant == "RDSOP6":
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rdsvariant == "RDSOP7":
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rdsvariant == "RDSOP8":
                    objectname = flag + "F" + str(EffectName(7, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "rWS":
                row = layout.row()

            if KCLOp.slot == "rDH":
                row = layout.row()

            if KCLOp.slot == "rBC3":
                row = layout.row()

            if KCLOp.slot == "rDKJP":
                row = layout.row()
                row.prop(KCLOp, "rdkjpvariant")

                if KCLOp.rdkjpvariant == "RDKJPOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rdkjpvariant == "RDKJPOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rdkjpvariant == "RDKJPOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rdkjpvariant == "RDKJPOP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "rMC":
                row = layout.row()
                row.prop(KCLOp, "rmcvariant")

                if KCLOp.rmcvariant == "RMCOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rmcvariant == "RMCOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rmcvariant == "RMCOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "rMC3":
                row = layout.row()

            if KCLOp.slot == "rPG":
                row = layout.row()

            if KCLOp.slot == "rDKM":
                row = layout.row()
                row.prop(KCLOp, "rdkmvariant")

                if KCLOp.rdkmvariant == "RDKMOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rdkmvariant == "RDKMOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rdkmvariant == "RDKMOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.slot == "rBC":
                row = layout.row()
                row.prop(KCLOp, "rbcvariant")

                if KCLOp.rbcvariant == "RBCOP1":
                    objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rbcvariant == "RBCOP2":
                    objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rbcvariant == "RBCOP3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rbcvariant == "RBCOP4":
                    objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rbcvariant == "RBCOP5":
                    objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rbcvariant == "RBCOP6":
                    objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.rbcvariant == "RBCOP7":
                    objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP19':
            row = layout.row()
            variant = 26
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "effecttriggervariant")

            if KCLOp.effecttriggervariant == "EFFECTOP1":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(0, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.effecttriggervariant == "EFFECTOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.effecttriggervariant == "EFFECTOP3":
                row = layout.row()
                if KCLOp.pocha == "POCHA1":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                  
                if KCLOp.pocha == "POCHA2":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 16))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.pocha == "POCHA3":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 32))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.pocha == "POCHA4":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 48))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.pocha == "POCHA5":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 64))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op)

                if KCLOp.pocha == "POCHA6":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 80))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.pocha == "POCHA7":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 96))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

                if KCLOp.pocha == "POCHA8":
                    objectname = flag + "F" + str(EffectName(2, 0, variant)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 112))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.effecttriggervariant == "EFFECTOP4":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(3, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.effecttriggervariant == "EFFECTOP5":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(4, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.effecttriggervariant == "EFFECTOP6":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(5, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.effecttriggervariant == "EFFECTOP7":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(6, 0, variant)).zfill(4)
                flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

        row = layout.row()
        row.label(text='Export As:',icon='BLENDER')
        row = layout.row()
        row.operator("export.flag_op")
        row.operator("export.kcl_op")

classes = [DropDown, APPLY_OT_apply_op, EXPORT_OT_kcl_op, EXPORT_OT_flag_op, KCL_PT_MainPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        bpy.types.Scene.my_tool = bpy.props.PointerProperty(type= DropDown)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()

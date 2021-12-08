import bpy
from bpy.types import Operator

ob = bpy.context.active_object
flag = "mat"

class DropDown(bpy.types.PropertyGroup): # Defines the list of Flags and Variants
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
                ('OP19', "Effect Trigger", ""),
                ('OP20', "Half-Pipe Invisible Wall", "")
            ]
        )
    # Road Variant Enumerator
    roadvar : bpy.props.EnumProperty( 
        name= "Variant",
        description= "",
        items= [('ROAD1', "Asphalt", ""),
                ('ROAD2', "Dirt with GFX (Only slots DKJP and DKM)", ""),
                ('ROAD3', "Dirt without GFX", ""),
                ('ROAD4', "Smooth", ""),
                ('ROAD5', "Wood", ""),
                ('ROAD6', "Snow", ""),
                ('ROAD7', "Metal Grate", ""),
                ('ROAD8', "Normal, but the sound cuts off", "")
            ]
        )
    # Slippery Road 1 Variant Enumerator
    sliproad1var : bpy.props.EnumProperty(
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
    # Weak Off-Road Variant Enumerator
    weakoffroadvar : bpy.props.EnumProperty(
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
    # Off-Road Variant Enumerator
    offroadvar : bpy.props.EnumProperty(
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
    # Heavy Off-Road Variant Enumerator
    heavyoffroadvar : bpy.props.EnumProperty(
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
    # Slippery Road 2 Variant Enumerator
    sliproad2var : bpy.props.EnumProperty(
        name= "Variant",
        description= "Slippery and slightly slows you down.",
        items= [('SLIPROAD2OP1', "Ice", ""),
                ('SLIPROAD2OP2', "Mud", ""),
                ('SLIPROAD2OP3', "Water", ""),
                ('SLIPROAD2OP4', "Normal Road, Different sound", "")
            ]
        )
    # Boost Panel Variant Enumerator
    boostpanvar : bpy.props.EnumProperty(
        name= "Variant",
        description= "",
        items= [('BOOSTPANOP1', "Default", ""),
                ('BOOSTPANOP2', "If used, and casino_roulette is near, the road slowly rotates everything nearby counterclockwise. Used in Chain Chomp Wheel.", ""),
                ('BOOSTPANOP3', "Unknown. Unused.", "")
            ]
        )
    # Boost Ramp Variant Enumerator
    boostrampvar : bpy.props.EnumProperty(
        name= "Variant",
        description= "Do not use collision effect 'Trickable' with this flag",
        items= [('BOOSTRAMPOP1', "2 Flips", ""),
                ('BOOSTRAMPOP2', "1 Flip", ""),
                ('BOOSTRAMPOP3', "No flips", "")
            ]
        )
    # Jump Pad Variant Enumerator
    jumppadvar : bpy.props.EnumProperty(
        name= "Variant",
        description= "Higher stages mean approximately longer air time and more distance.",
        items= [('JUMPPADOP1', "Stage 2, used in GBA Bowser Castle 3", ""),
                ('JUMPPADOP2', "Stage 3, used in SNES Ghost Valley 2", ""),
                ('JUMPPADOP3', "Stage 1, used in GBA Shy Guy Beach", ""),
                ('JUMPPADOP4', "Stage 4, used in Mushroom Gorge", ""),
                ('JUMPPADOP5', "Stage 5, Bouncy mushroom (Causes off-road glitch)", ""),
                ('JUMPPADOP6', "Stage 4, used in Chain Chomp Wheel", ""),
                ('JUMPPADOP7', "Stage 2, used in DS Yoshi Falls and Funky Stadium", ""),
                ('JUMPPADOP6', "Stage 4, unused.", "")
            ]
        )
    # Solid Fall Variant Enumerator
    solidfallvar : bpy.props.EnumProperty(
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
    # Moving Road Variant Enumerator
    movingroadvar : bpy.props.EnumProperty(
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
    # Wall Variant Enumerator
    wallvar : bpy.props.EnumProperty(
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
    # Invisible Wall Variant Enumerator
    invwallvar : bpy.props.EnumProperty(
        name= "Variant",
        description= "",
        items= [('INVWALLOP1', "Default", ""),
                ('INVWALLOP2', "Spark and character wall hit voice", ""),
            ]
        )

class APPLY_OT_apply_op(Operator):
    bl_idname = 'apply.apply_op'
    bl_label = 'Apply'
    bl_description = 'Apply Flag'
    
    def flagmat(self, flag, ob):
# Get material
      mat = bpy.data.materials.get(flag)
      if mat is None:
    # create material
          mat = bpy.data.materials.new(name=flag)

# Assign it to object
      if ob.data.materials:
    # assign to 1st material slot
          ob.data.materials[0] = mat
      else:
    # no slots
          ob.data.materials.append(mat)

    def execute(self, context):
        ob = context.active_object
        self.flagmat(flag,ob)
        return {'FINISHED'}

class EXPORT_OT_flag_op(Operator):
    bl_idname = 'export.flag_op'
    bl_label = 'Flag'
    bl_description = 'Export Flag File'

class EXPORT_OT_kcl_op(Operator):
    bl_idname = 'export.kcl_op'
    bl_label = 'KCL'
    bl_description = 'Export KCL File'

class KCL_PT_MainPanel(bpy.types.Panel):
    bl_label = "KCL Creator"
    bl_idname = "KCL_PT_MainPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
        
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        KCLOp = scene.my_tool
        row = layout.row()
        row.prop(KCLOp, "enum")
        
        if KCLOp.enum == 'OP1':
            row = layout.row()
            row.prop(KCLOp, "roadvar") # Road Variant
            
            if KCLOp.roadvar == 'ROAD1':
                flag = "Test"
                ob = bpy.context.active_object
                row = layout.row()
                row.operator("apply.apply_op")
        
        if KCLOp.enum == 'OP2':
            row = layout.row()
            row.prop(KCLOp, "sliproad1var") # Slippery Road 1 Variant

        if KCLOp.enum == 'OP3':
            row = layout.row()
            row.prop(KCLOp, "weakoffroadvar") # Weak Off-road Variant

        if KCLOp.enum == 'OP4':
            row = layout.row()
            row.prop(KCLOp, "offroadvar") # Off-road Variant

        if KCLOp.enum == 'OP5':
            row = layout.row()
            row.prop(KCLOp, "heavyoffroadvar") # Heavy off-road Variant

        if KCLOp.enum == 'OP6':
            row = layout.row()
            row.prop(KCLOp, "sliproad2var") # Slippery road 2 Variant

        if KCLOp.enum == 'OP7':
            row = layout.row()
            row.prop(KCLOp, "boostpanvar") # Boost panel Variant

        if KCLOp.enum == 'OP8':
            row = layout.row()
            row.prop(KCLOp, "boostrampvar") # Boost ramp Variant

        if KCLOp.enum == 'OP9':
            row = layout.row()
            row.prop(KCLOp, "jumppadvar") # Jump Pad Variant

        if KCLOp.enum == 'OP10':
            row = layout.row()
            row.prop(KCLOp, "solidfallvar") # Solid Fall Variant

        if KCLOp.enum == 'OP11':
            row = layout.row()
            row.prop(KCLOp, "movingroadvar") # Moving Road Variant

        if KCLOp.enum == 'OP12':
            row = layout.row()
            row.prop(KCLOp, "wallvar") # Wall Variant

        if KCLOp.enum == 'OP13':
            row = layout.row()
            row.prop(KCLOp, "invwallvar") # Invisible Wall Variant

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
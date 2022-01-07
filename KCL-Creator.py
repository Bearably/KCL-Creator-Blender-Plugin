import bpy
import random
from bpy.types import Operator
from bpy_extras.io_utils import ExportHelper
        
ob = bpy.context.active_object
flag = "mat"
effect = 0
variant = 0
variantnum = 0
hexconv = 256
effectnum = 0
objectname = 'name'

        
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
                ('OP19', "Effect Trigger", ""),
                ('OP20', "Half-Pipe Invisible Wall", "")
            ]
        )
        
    trickable : bpy.props.EnumProperty(
        name= "Trickable?",
        description= "",
        items= [('NOTTRICKABLE', "No", ""),
                ('TRICKABLE', "Yes", "")
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
                ('ROAD8', "Normal, but the sound cuts off", "")
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
        filepath = self.filepath
        # f = open(filepath, 'w')
        # f.write(stuff)
        # f.close()
        return{'FINISHED'}

class EXPORT_OT_kcl_op(Operator, ExportHelper):
    bl_idname = 'export.kcl_op'
    bl_label = 'KCL'
    bl_description = 'Export KCL File'
    
    ScaleValue : bpy.props.FloatProperty(name= "Scale", min=0, max=1000)
    
    filename_ext = ".kcl"  # ExportHelper mixin class uses this
    def execute(self, context):
        filepath = self.filepath
        # f = open(filepath, 'w')
        # f.write(stuff)
        # f.close()
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
        
        def EffectName(variant, variantnum):
            variantnum = variantnum + variant << 5
            variantnum = hex(variantnum)[2:6]
            print(variantnum)
            return variantnum
        
        if KCLOp.enum == 'OP1':
            row = layout.row()
            row.prop(KCLOp, "roadvariant")  # Road variant
            
            if KCLOp.roadvariant == 'ROAD1':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    #print(objectname)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row() 
                    objectname = flag + "F" + str(EffectName(0, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    #print(objectname)
                    row.operator("apply.apply_op")
                              
            if KCLOp.roadvariant == 'ROAD2':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    #print(objectname)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    #print(objectname)
                    row.operator("apply.apply_op")
      
            if KCLOp.roadvariant == 'ROAD3':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.roadvariant == 'ROAD5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 256)).zfill(4)
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
                    objectname = flag + "F" + str(EffectName(0, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
            
            if KCLOp.sliproad1variant == "SLIPROAD1OP2":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.sliproad1variant == "SLIPROAD1OP3":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.sliproad1variant == 'SLIPROAD1OP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.sliproad1variant == 'SLIPROAD1OP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.sliproad1variant == 'SLIPROAD1OP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.sliproad1variant == 'SLIPROAD1OP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.sliproad1variant == 'SLIPROAD1OP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 256)).zfill(4)
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
                    objectname = flag + "F" + str(EffectName(0, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.weakoffroadvariant == "WEAKOFFROADOP2":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.weakoffroadvariant == "WEAKOFFROADOP3":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 256)).zfill(4)
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
                    objectname = flag + "F" + str(EffectName(0, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.offroadvariant == "OFFROADOP2":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.offroadvariant == "OFFROADOP3":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.offroadvariant == 'OFFROADOP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.offroadvariant == 'OFFROADOP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.offroadvariant == 'OFFROADOP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.offroadvariant == 'OFFROADOP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.offroadvariant == 'OFFROADOP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 256)).zfill(4)
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
                    objectname = flag + "F" + str(EffectName(0, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.heavyoffroadvariant == "HEAVYOFFROADOP2":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.heavyoffroadvariant == "HEAVYOFFROADOP3":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 256)).zfill(4)
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
                    objectname = flag + "F" + str(EffectName(0, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
            
            if KCLOp.sliproad2variant == "SLIPROAD2OP2":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.sliproad2variant == "SLIPROAD2OP3":
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.sliproad2variant == 'SLIPROAD2OP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256)).zfill(4)
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
                    objectname = flag + "F" + str(EffectName(0, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                              
            if KCLOp.boostpanvariant == 'BOOSTPANOP2':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
      
            if KCLOp.roadvariant == 'BOOSTPANOP3':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256)).zfill(4)
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
                objectname = flag + "F" + str(EffectName(0, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.boostrampvariant == "BOOSTRAMPOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.boostrampvariant == "BOOSTRAMPOP3":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(2, 0)).zfill(4)
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
                objectname = flag + "F" + str(EffectName(0, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP3":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(2, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP4":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(3, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP5":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(4, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP6":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(5, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP7":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(6, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP8":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(7, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

        if KCLOp.enum == 'OP10':
            row = layout.row()
            variant = 9
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "solidfallvariant") # Solid Fall variant

            if KCLOp.solidfallvariant == "SOLIDFALLOP1":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(0, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP3":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(2, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP4":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(3, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP5":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(4, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP6":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(5, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP7":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(6, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP8":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(7, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

        if KCLOp.enum == 'OP11':
            row = layout.row()
            variant = 10
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "movingroadvariant") # Moving Road variant

            if KCLOp.movingroadvariant == 'MOVINGROADOP1':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(0, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(0, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                              
            if KCLOp.movingroadvariant == 'MOVINGROADOP2':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(1, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(1, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
      
            if KCLOp.movingroadvariant == 'MOVINGROADOP3':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(2, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(2, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.movingroadvariant == 'MOVINGROADOP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(3, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(3, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.movingroadvariant == 'MOVINGROADOP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(4, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(4, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.movingroadvariant == 'MOVINGROADOP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(5, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(5, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.movingroadvariant == 'MOVINGROADOP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(6, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(6, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.movingroadvariant == 'MOVINGROADOP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 0)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    objectname = flag + "F" + str(EffectName(7, 256)).zfill(4)
                    flag = flag + hex(ChangeEffect(7, 256))[2:5].zfill(3)
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP12':
            row = layout.row()
            variant = 11
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "wallvariant") # Wall variant

            if KCLOp.wallvariant == "WALLOP1":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(0, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP3":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(2, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(2, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP4":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(3, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(3, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP5":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(4, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(4, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP6":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(5, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(5, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP7":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(6, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(6, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP8":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(7, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(7, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

        if KCLOp.enum == 'OP13':
            row = layout.row()
            variant = 12
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "invwallvariant") # Invisible Wall variant

            if KCLOp.invwallvariant == "INVWALLOP1":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(0, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(0, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")

            if KCLOp.invwallvariant == "INVWALLOP2":
                row = layout.row()
                objectname = flag + "F" + str(EffectName(1, 0)).zfill(4)
                flag = flag + hex(ChangeEffect(1, 0))[2:5].zfill(3)
                #print(flag)
                row.operator("apply.apply_op")
        
        if KCLOp.enum == 'OP14':
            row = layout.row()
            variant = 13
            flag = "_" + hex(variant)[2:4].zfill(2) + "_"
            row.prop(KCLOp, "

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

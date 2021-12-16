import bpy
import random
from bpy.types import Operator
        
ob = bpy.context.active_object
flag = "mat"
effect = 0
variant = 0
variantnum = 0
hexconv = 156

        
class DropDown(bpy.types.PropertyGroup):
    
    ScaleValue : bpy.props.FloatProperty(name= "FBX Scale", min=0, max=1000)
    
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
          mat.diffuse_color = (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),1)

# Assign it to object
      if ob.data.materials:
    # assign to 1st material slot
          ob.data.materials[0] = mat
      else:
    # no slots
          ob.data.materials.append(mat)

    def execute(self, context):
        ob = context.active_object
        self.flagmat(flag, ob)
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        ob = context.active_object
        self.flagmat(flag, ob)
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
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
        global flag
        global variant
        global effect
        global variantnum
        global hexconv
        variantnum = 0
        variant = 100
        effect = 1000
        hexconv = 156
        flag = "_" + str(variant)[1:3] + "_"
        
        def ChangeEffect(effect, effectnum):
            effect = effect + effectnum
            return effect              
        
        if KCLOp.enum == 'OP1':
            row = layout.row()
            row.prop(KCLOp, "roadvariant")  # Road variant
            
            if KCLOp.roadvariant == 'ROAD1':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(effect)[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 100))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                              
            if KCLOp.roadvariant == 'ROAD2':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 1))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 101))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
      
            if KCLOp.roadvariant == 'ROAD3':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 2))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 102))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 3))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 103))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.roadvariant == 'ROAD5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 4))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 104))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 5))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 105))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 6))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 106))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.roadvariant == 'ROAD8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 7))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 107))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP2':
            row = layout.row()
            variantnum = 1
            variant = hex(100 + hexconv + variantnum)[3:5]
            flag = "_" + str(variant) + "_"
            row.prop(KCLOp, "sliproad1variant") # Slippery Road 1 variant

            if KCLOp.sliproad1variant == "SLIPROAD1OP1":
              row = layout.row()
              row.prop(KCLOp, "trickable")

              if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(effect)[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
              if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 100))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
            
            if KCLOp.sliproad1variant == "SLIPROAD1OP2":
              row = layout.row()
              row.prop(KCLOp, "trickable")

              if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 1))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
              if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 101))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")

            if KCLOp.sliproad1variant == "SLIPROAD1OP3":
              row = layout.row()
              row.prop(KCLOp, "trickable")

              if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 2))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
              if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 102))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")

            if KCLOp.sliproad1variant == 'SLIPROAD1OP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 3))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 103))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.sliproad1variant == 'SLIPROAD1OP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 4))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 104))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.sliproad1variant == 'SLIPROAD1OP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 5))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 105))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.sliproad1variant == 'SLIPROAD1OP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 6))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 106))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.sliproad1variant == 'SLIPROAD1OP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 7))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 107))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP3':
            row = layout.row()
            variantnum = 2
            variant = hex(100 + hexconv + variantnum)[3:5]
            flag = "_" + str(variant) + "_"
            row.prop(KCLOp, "weakoffroadvariant") # Weak Off-road variant

            if KCLOp.weakoffroadvariant == "WEAKOFFROADOP1":
              row = layout.row()
              row.prop(KCLOp, "trickable")

              if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(effect)[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
              if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 100))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")

            if KCLOp.weakoffroadvariant == "WEAKOFFROADOP2":
              row = layout.row()
              row.prop(KCLOp, "trickable")

              if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 1))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
              if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 101))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")

            if KCLOp.weakoffroadvariant == "WEAKOFFROADOP3":
              row = layout.row()
              row.prop(KCLOp, "trickable")

              if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 2))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
              if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 102))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")

            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 3))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 103))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 4))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 104))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 5))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 105))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 6))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 106))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.weakoffroadvariant == 'WEAKOFFROADOP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 7))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 107))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP4':
            row = layout.row()
            variantnum = 3
            variant = hex(100 + hexconv + variantnum)[3:5]
            flag = "_" + str(variant) + "_"
            row.prop(KCLOp, "offroadvariant") # Off-road variant
            
            if KCLOp.offroadvariant == 'OFFROADOP1':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(effect)[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 100))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")

            if KCLOp.offroadvariant == "OFFROADOP2":
              row = layout.row()
              row.prop(KCLOp, "trickable")

              if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 1))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
              if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 101))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")

            if KCLOp.offroadvariant == "OFFROADOP3":
              row = layout.row()
              row.prop(KCLOp, "trickable")

              if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 2))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
              if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 102))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")

            if KCLOp.offroadvariant == 'OFFROADOP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 3))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 103))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.offroadvariant == 'OFFROADOP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 4))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 104))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.offroadvariant == 'OFFROADOP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 5))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 105))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.offroadvariant == 'OFFROADOP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 6))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 106))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.offroadvariant == 'OFFROADOP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 7))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 107))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP5':
            row = layout.row()
            variantnum = 4
            variant = hex(100 + hexconv + variantnum)[3:5]
            flag = "_" + str(variant) + "_"
            row.prop(KCLOp, "heavyoffroadvariant") # Heavy off-road variant

            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP1':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(effect)[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 100))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")

            if KCLOp.heavyoffroadvariant == "HEAVYOFFROADOP2":
              row = layout.row()
              row.prop(KCLOp, "trickable")

              if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 1))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
              if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 101))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")

            if KCLOp.heavyoffroadvariant == "HEAVYOFFROADOP3":
              row = layout.row()
              row.prop(KCLOp, "trickable")

              if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 2))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
              if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 102))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")

            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 3))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 103))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 4))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 104))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 5))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 105))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 6))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 106))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.heavyoffroadvariant == 'HEAVYOFFROADOP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 7))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 107))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP6':
            row = layout.row()
            variantnum = 5
            variant = hex(100 + hexconv + variantnum)[3:5]
            flag = "_" + str(variant) + "_"
            row.prop(KCLOp, "sliproad2variant") # Slippery road 2 variant

            if KCLOp.sliproad2variant == "SLIPROAD2OP1":
              row = layout.row()
              row.prop(KCLOp, "trickable")

              if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(effect)[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
              if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 100))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
            
            if KCLOp.sliproad2variant == "SLIPROAD2OP2":
              row = layout.row()
              row.prop(KCLOp, "trickable")

              if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 1))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
              if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 101))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")

            if KCLOp.sliproad2variant == "SLIPROAD2OP3":
              row = layout.row()
              row.prop(KCLOp, "trickable")

              if KCLOp.trickable == 'NOTTRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 2))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")
                
              if KCLOp.trickable == 'TRICKABLE':
                  row = layout.row()
                  flag = flag + str(ChangeEffect(effect, 102))[1:4]
                  #print(flag)
                  row.operator("apply.apply_op")

            if KCLOp.sliproad2variant == 'SLIPROAD2OP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 3))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 103))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP7':
            row = layout.row()
            variantnum = 6
            variant = hex(100 + hexconv + variantnum)[3:5]
            flag = "_" + str(variant) + "_"
            row.prop(KCLOp, "boostpanvariant") # Boost panel variant

            if KCLOp.boostpanvariant == 'BOOSTPANOP1':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(effect)[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 100))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                              
            if KCLOp.boostpanvariant == 'BOOSTPANOP2':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 1))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 101))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
      
            if KCLOp.roadvariant == 'BOOSTPANOP3':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 2))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 102))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP8':
            row = layout.row()
            variantnum = 7
            variant = hex(100 + hexconv + variantnum)[3:5]
            flag = "_" + str(variant)[1:3] + "_"
            row.prop(KCLOp, "boostrampvariant") # Boost ramp variant

            if KCLOp.boostrampvariant == "BOOSTRAMPOP1":
              row = layout.row()
              flag = flag + str(effect)[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.boostrampvariant == "BOOSTRAMPOP2":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 1))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.boostrampvariant == "BOOSTRAMPOP3":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 2))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

        if KCLOp.enum == 'OP9':
            row = layout.row()
            variantnum = 8
            variant = hex(100 + hexconv + variantnum)[3:5]
            flag = "_" + str(variant) + "_"
            row.prop(KCLOp, "jumppadvariant") # Jump Pad variant

            if KCLOp.jumppadvariant == "JUMPPADOP1":
              row = layout.row()
              flag = flag + str(effect)[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP2":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 1))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP3":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 2))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP4":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 3))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP5":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 4))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP6":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 5))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP7":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 6))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.jumppadvariant == "JUMPPADOP8":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 7))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

        if KCLOp.enum == 'OP10':
            row = layout.row()
            variantnum = 9
            variant = hex(100 + hexconv + variantnum)[3:5]
            flag = "_" + str(variant) + "_"
            row.prop(KCLOp, "solidfallvariant") # Solid Fall variant

            if KCLOp.solidfallvariant == "SOLIDFALLOP1":
              row = layout.row()
              flag = flag + str(effect)[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP2":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 1))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP3":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 2))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP4":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 3))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP5":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 4))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP6":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 5))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP7":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 6))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.solidfallvariant == "SOLIDFALLOP8":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 7))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

        if KCLOp.enum == 'OP11':
            row = layout.row()
            variantnum = 10
            variant = hex(100 + hexconv + variantnum)[3:5]
            flag = "_" + str(variant) + "_"
            row.prop(KCLOp, "movingroadvariant") # Moving Road variant

            if KCLOp.movingroadvariant == 'MOVINGROADOP1':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(effect)[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 100))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                              
            if KCLOp.movingroadvariant == 'MOVINGROADOP2':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 1))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 101))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
      
            if KCLOp.movingroadvariant == 'MOVINGROADOP3':
                row = layout.row()
                row.prop(KCLOp, "trickable")
                
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 2))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 102))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.movingroadvariant == 'MOVINGROADOP4':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 3))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 103))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

            if KCLOp.movingroadvariant == 'MOVINGROADOP5':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 4))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 104))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.movingroadvariant == 'MOVINGROADOP6':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 5))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 105))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.movingroadvariant == 'MOVINGROADOP7':
                row = layout.row()
                row.prop(KCLOp, "trickable")

                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 6))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 106))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
            if KCLOp.movingroadvariant == 'MOVINGROADOP8':
                row = layout.row()
                row.prop(KCLOp, "trickable")
        
                if KCLOp.trickable == 'NOTTRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 7))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")
                
                if KCLOp.trickable == 'TRICKABLE':
                    row = layout.row()
                    flag = flag + str(ChangeEffect(effect, 107))[1:4]
                    #print(flag)
                    row.operator("apply.apply_op")

        if KCLOp.enum == 'OP12':
            row = layout.row()
            variantnum = 11
            variant = hex(100 + hexconv + variantnum)[3:5]
            flag = "_" + str(variant) + "_"
            row.prop(KCLOp, "wallvariant") # Wall variant

            if KCLOp.wallvariant == "WALLOP1":
              row = layout.row()
              flag = flag + str(effect)[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP2":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 1))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP3":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 2))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP4":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 3))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP5":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 4))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP6":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 5))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP7":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 6))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.wallvariant == "WALLOP8":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 7))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

        if KCLOp.enum == 'OP13':
            row = layout.row()
            variantnum = 12
            variant = hex(100 + hexconv + variantnum)[3:5]
            flag = "_" + str(variant) + "_"
            row.prop(KCLOp, "invwallvariant") # Invisible Wall variant

            if KCLOp.invwallvariant == "INVWALLOP1":
              row = layout.row()
              flag = flag + str(effect)[1:4]
              #print(flag)
              row.operator("apply.apply_op")

            if KCLOp.invwallvariant == "INVWALLOP2":
              row = layout.row()
              flag = flag + str(ChangeEffect(effect, 1))[1:4]
              #print(flag)
              row.operator("apply.apply_op")

        row = layout.row()
        row.label(text='Export As:',icon='BLENDER')
        row = layout.row()
        row.prop(KCLOp, "ScaleValue")
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

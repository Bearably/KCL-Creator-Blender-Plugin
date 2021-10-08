import bpy
from bpy.types import Operator

mat = bpy.data.materials.new(name="KCL Flag")
ob = bpy.context.active_object

class DropDown(bpy.types.PropertyGroup):
    enum : bpy.props.EnumProperty(
        name= "KCL Flag",
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
        # I AM SO STUPID.
    roadvar : bpy.props.EnumProperty(
        name= "KCL Variant",
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
        
    sliproad1var : bpy.props.EnumProperty(
        name= "KCL Variant",
        description= "",
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
                
class APPLY_OT_apply_op(Operator):
    bl_idname = 'apply.apply_op'
    bl_label = 'Apply'
    bl_description = 'Apply Flag'

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
        
        #row = layout.row()
        #row.prop(mytool, "apply")
        
        if KCLOp.enum == 'OP1':
            row = layout.row()
            row.prop(KCLOp, "roadvar")
        
        if KCLOp.enum == 'OP2':
            row = layout.row()
            row.prop(KCLOp, "sliproad1var")
        
        row = layout.row()
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

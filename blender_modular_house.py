import bpy

wall_type = "Larg"

unit_length_given = 200
unit_length = 0

active_dir = "w"

pesting = True

objects_name = ""

duplicated_objects_name = []

material_name = "MaterialName"

main_database = {
    'roof': {'type': 'single', 'list':{"theObject": "roofPlane"}},
    'roof1': {'type': 'single', 'list':{"theObject": "roofBox"}},
    'roof2s': {'type': 'single', 'list':{"theObject": "roofBase"}},
    'roof2': {'type': 'multi', 'list':{
    "corner1small": "corner1small",
    "corner2small": "corner2small",
    "corner3small": "corner3small",
    "corner4small": "corner4small",
    "corner1large": "roofcon1",
    "corner2large": "roofcon2",
    "corner3large": "roofcon3",
    "corner4large": "roofcon4",
    "corner1small_inverted": "corner1small_inverted",
    "corner2small_inverted": "corner2small_inverted",
    "corner3small_inverted": "corner3small_inverted",
    "corner4small_inverted": "corner4small_inverted",
    "corner1large_inverted": "roofcon1_invert",
    "corner2large_inverted": "roofcon2_invert",
    "corner3large_inverted": "roofcon3_invert",
    "corner4large_inverted": "roofcon4_invert",
    "wall1small": "wall1small",
    "wall2small": "wall2small",
    "wall3small": "wall3small",
    "wall4small": "wall4small",
    "wall1large": "roofSide1",
    "wall2large": "roofSide2",
    "wall3large": "roofSide3",
    "wall4large": "roofSide4"
}},
    'wall': {'type': 'multi', 'list':{
    "corner1small": "corner1small",
    "corner2small": "corner2small",
    "corner3small": "corner3small",
    "corner4small": "corner4small",
    "corner1large": "corner1large",
    "corner2large": "corner2large",
    "corner3large": "corner3large",
    "corner4large": "corner4large",
    "corner1small_inverted": "corner1small_inverted",
    "corner2small_inverted": "corner2small_inverted",
    "corner3small_inverted": "corner3small_inverted",
    "corner4small_inverted": "corner4small_inverted",
    "corner1large_inverted": "corner1large_inverted",
    "corner2large_inverted": "corner2large_inverted",
    "corner3large_inverted": "corner3large_inverted",
    "corner4large_inverted": "corner4large_inverted",
    "wall1small": "wall1small",
    "wall2small": "wall2small",
    "wall3small": "wall3small",
    "wall4small": "wall4small",
    "wall1large": "wall1large",
    "wall2large": "wall2large",
    "wall3large": "wall3large",
    "wall4large": "wall4large"
}},
    'wall2': {'type': 'multi', 'list':{
    "corner1small": "corner1small",
    "corner2small": "corner2small",
    "corner3small": "corner3small",
    "corner4small": "corner4small",
    "corner1large": "corner1large_wall2",
    "corner2large": "corner2large_wall2",
    "corner3large": "corner3large_wall2",
    "corner4large": "corner4large_wall2",
    "corner1small_inverted": "corner1small_inverted",
    "corner2small_inverted": "corner2small_inverted",
    "corner3small_inverted": "corner3small_inverted",
    "corner4small_inverted": "corner4small_inverted",
    "corner1large_inverted": "corner3large_wall2",
    "corner2large_inverted": "corner4large_wall2",
    "corner3large_inverted": "corner1large_wall2",
    "corner4large_inverted": "corner2large_wall2",
    "wall1small": "wall1small",
    "wall2small": "wall2small",
    "wall3small": "wall3small",
    "wall4small": "wall4small",
    "wall1large": "wall1large_wall2",
    "wall2large": "wall2large_wall2",
    "wall3large": "wall3large_wall2",
    "wall4large": "wall4large_wall2"
}}}




extracted_list = {}
objects_Type = "multi"


def move_3d_cursor_to_point(cursor_location):
    bpy.context.scene.cursor.location = cursor_location

def duplicate_object_by_name(object_name):
    # Find the object by its name
    obj = bpy.data.objects.get(str(object_name))
    print(str(object_name))

    if obj is not None:
        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')

        # Select the object
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        # Duplicate the object
        bpy.ops.object.duplicate(linked=False)

        # Apply global offset based on 3D cursor location
        duplicated_obj = bpy.context.active_object
        duplicated_obj.location = bpy.context.scene.cursor.location

        # Clear the selection
        bpy.ops.object.select_all(action='DESELECT')
        
        duplicated_objects_name.append(str(duplicated_obj.name))
        
def delete_object_by_name(object_name):
    # Find the object by its name
    obj = bpy.data.objects.get(object_name)

    if obj is not None:
        # Select the object
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        # Move 3D cursor to object origin
        bpy.context.scene.cursor.location = obj.location

        # Delete the object
        bpy.ops.object.delete()
        

def assignmaterial(object_name, material_name):
    # Retrieve the material and object
    material = bpy.data.materials.get(material_name)
    obj = bpy.data.objects.get(object_name)
    if material is None:
        print("Material '{}' not found.".format(material_name))
        return
    if obj is None:
        print("Object '{}' not found.".format(object_name))
        return
    # Check if the object is a mesh
    if obj.type != 'MESH':
        print("Object '{}' is not a mesh.".format(object_name))
        return
    # Create a material slot if needed
    if len(obj.data.materials) == 0:
        obj.data.materials.append(material)
    # Assign the material to the first material slot
    obj.data.materials[0] = material
    print("Material '{}' applied to object '{}'.".format(material_name, object_name))


def creat_list_of_selectedObjects():
    bpy.context.view_layer.objects.active = None
    selected_object_names = [obj.name for obj in bpy.context.selected_objects]
    print("Selected Objects:")
    return selected_object_names

#print(creat_list_of_selectedObjects())

def assignMaterial_to_Selected(material_name):
    # Get all objects in the scene
    objects = bpy.data.objects

    # Check if any object is selected
    any_object_selected = any(obj.select_get() for obj in objects)

    # Print the result
    if any_object_selected:
        objects_list = creat_list_of_selectedObjects()
        for i in range(0, len(objects_list)):
            assignmaterial(str(objects_list[i]), material_name)
    else:
        print("No objects are selected.")

#assignMaterial_to_Selected("genMaterial")
    
def change_Drawing_Mode(trueFalse):
    global pesting
    if trueFalse == "True":
        pesting = True
    elif trueFalse == "False":
        pesting = False
    pass

def reset_dir(dir_to_set_argument):
    global active_dir
    dir_to_set = str(dir_to_set_argument)
    lowercase_text = dir_to_set.lower()
    trimmed_text = lowercase_text.lstrip()
    if trimmed_text == "w":
        active_dir = "w"
    elif trimmed_text == "n":
        active_dir = "n"
    elif trimmed_text == "e":
        active_dir = "e"
    elif trimmed_text == "s":
        active_dir = "s"
    duplicated_objects_name.clear()


def half_Steps(trueFalse):
    global wall_type
    global unit_length
    if trueFalse == "True":
        wall_type = "Small"
        unit_length = unit_length_given/2
    elif trueFalse == "False":
        wall_type = "Larg"
        unit_length = unit_length_given
        
def set_objects(objects_name):
    global objects_Type
    global extracted_list
    if objects_name in main_database:
        if main_database[objects_name]["type"] == "single":
            objects_Type = "single"
            extracted_list = main_database[objects_name]['list']
            print(extracted_list)
        elif main_database[objects_name]["type"] == "multi":
            objects_Type = "multi"
            extracted_list = main_database[objects_name]['list']
            print(extracted_list)
    else:
        print("object not in database")


def print_L():
    print(len(extracted_list))
    pass

def s():
    global active_dir
    cursor_location = bpy.context.scene.cursor.location
    vector_x, vector_y, vector_z = cursor_location
    vector_y -= unit_length
    if objects_Type == "multi":
        if pesting == True:
            if active_dir == "s":
                if wall_type == "Small":
                    duplicate_object_by_name(extracted_list["wall1small"])
                elif wall_type == "Larg":
                    duplicate_object_by_name(extracted_list["wall1large"])
            elif active_dir == "e":
                if wall_type == "Small":
                    duplicate_object_by_name(extracted_list["corner1small_inverted"])
                elif wall_type == "Larg":
                    duplicate_object_by_name(extracted_list["corner1large_inverted"])
            elif active_dir == "n":
                pass
            elif active_dir == "w":
                if wall_type == "Small":
                    duplicate_object_by_name(extracted_list["corner4small"])
                elif wall_type == "Larg":
                    duplicate_object_by_name(extracted_list["corner4large"])
        else:
            pass
    elif objects_Type == "single":
        if pesting == True:
            duplicate_object_by_name(extracted_list["theObject"])
    active_dir = "s"
    move_3d_cursor_to_point((vector_x, vector_y, vector_z))
    print_L()



def e():
    global active_dir
    cursor_location = bpy.context.scene.cursor.location
    vector_x, vector_y, vector_z = cursor_location
    vector_x += unit_length
    if objects_Type == "multi":
        if pesting == True:
            if active_dir == "s":
                if wall_type == "Small":
                    duplicate_object_by_name(extracted_list["corner1small"])
                elif wall_type == "Larg":
                    duplicate_object_by_name(extracted_list["corner1large"])
            elif active_dir == "e":
                if wall_type == "Small":
                    duplicate_object_by_name(extracted_list["wall2small"])
                elif wall_type == "Larg":
                    duplicate_object_by_name(extracted_list["wall2large"])
            elif active_dir == "n":
                if wall_type == "Small":
                    duplicate_object_by_name(extracted_list["corner2small_inverted"])
                elif wall_type == "Larg":
                    duplicate_object_by_name(extracted_list["corner2large_inverted"])
            elif active_dir == "w":
                pass
        else:
            pass
    elif objects_Type == "single":
        if pesting == True:
            duplicate_object_by_name(extracted_list["theObject"])
    active_dir = "e"
    move_3d_cursor_to_point((vector_x, vector_y, vector_z))
    print_L()


def n():
    global active_dir
    cursor_location = bpy.context.scene.cursor.location
    vector_x, vector_y, vector_z = cursor_location
    vector_y += unit_length
    if objects_Type == "multi":
        if pesting == True:
            if active_dir == "s":
                pass
            elif active_dir == "e":
                if wall_type == "Small":
                    duplicate_object_by_name(extracted_list["corner2small"])
                elif wall_type == "Larg":
                    duplicate_object_by_name(extracted_list["corner2large"])
            elif active_dir == "n":
                if wall_type == "Small":
                    duplicate_object_by_name(extracted_list["wall3small"])
                elif wall_type == "Larg":
                    duplicate_object_by_name(extracted_list["wall3large"])
            elif active_dir == "w":
                if wall_type == "Small":
                    duplicate_object_by_name(extracted_list["corner3small_inverted"])
                elif wall_type == "Larg":
                    duplicate_object_by_name(extracted_list["corner3large_inverted"])
        else:
            pass
    elif objects_Type == "single":
        if pesting == True:
            duplicate_object_by_name(extracted_list["theObject"])
    active_dir = "n"
    move_3d_cursor_to_point((vector_x, vector_y, vector_z))
    print_L()


def w():
    global active_dir
    cursor_location = bpy.context.scene.cursor.location
    vector_x, vector_y, vector_z = cursor_location
    vector_x -= unit_length
    if objects_Type == "multi":
        if pesting == True:
            if active_dir == "s":
                if wall_type == "Small":
                    duplicate_object_by_name(extracted_list["corner4small_inverted"])
                elif wall_type == "Larg":
                    duplicate_object_by_name(extracted_list["corner4large_inverted"])
            elif active_dir == "e":
                pass
            elif active_dir == "n":
                if wall_type == "Small":
                    duplicate_object_by_name(extracted_list["corner3small"])
                elif wall_type == "Larg":
                    duplicate_object_by_name(extracted_list["corner3large"])
            elif active_dir == "w":
                if wall_type == "Small":
                    duplicate_object_by_name(extracted_list["wall4small"])
                elif wall_type == "Larg":
                    duplicate_object_by_name(extracted_list["wall4large"])
        else:
            pass
    elif objects_Type == "single":
        if pesting == True:
            duplicate_object_by_name(extracted_list["theObject"])
    active_dir = "w"
    move_3d_cursor_to_point((vector_x, vector_y, vector_z))
    print_L()

def z_plus():
    cursor_location = bpy.context.scene.cursor.location
    vector_x, vector_y, vector_z = cursor_location
    vector_z += unit_length
    move_3d_cursor_to_point((vector_x, vector_y, vector_z))
    print_L()

def z_minus():
    cursor_location = bpy.context.scene.cursor.location
    vector_x, vector_y, vector_z = cursor_location
    vector_z -= unit_length
    move_3d_cursor_to_point((vector_x, vector_y, vector_z))

def delete():
    global active_dir
    if 'con4' in duplicated_objects_name[-1]:
        active_dir = "s"
    elif 'con1' in duplicated_objects_name[-1]:
        active_dir = "e"
    elif 'con2' in duplicated_objects_name[-1]:
        active_dir = "n"
    elif 'con3' in duplicated_objects_name[-1]:
        active_dir = "w"
    elif 'wal1' in duplicated_objects_name[-1]:
        active_dir = "s"
    elif 'wal2' in duplicated_objects_name[-1]:
        active_dir = "e"
    elif 'wal3' in duplicated_objects_name[-1]:
        active_dir = "n"
    elif 'wal4' in duplicated_objects_name[-1]:
        active_dir = "w"
    delete_object_by_name(duplicated_objects_name[-1])
    del duplicated_objects_name[-1]



class MyAddOnPanel1(bpy.types.Panel):
    bl_label = "Drawing Section"
    bl_idname = "OBJECT_PT_my_addon"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "My Addon"
    # bl_context = "object"

    def draw(self, context):
        layout = self.layout
        object = context.object
        
        layout.label(text="Enter Objects Name / List:")
        layout.prop(context.scene, "my_text1", text="")
        layout.operator("object.print_text_operator", text="Set Object")
        
        layout.label(text="Enter Custom Steps:")
        layout.prop(context.scene, "my_text2", text="")
        layout.operator("object.print_text_operator2", text="Set Steps")
        
        layout.label(text="Reset Dir:")
        layout.prop(context.scene, "my_text4", text="")
        layout.operator("object.print_text_operator4", text="reset")
        
        # Add other UI elements here
        layout.label(text="Draw BUilding")

        # Create a new box for the joystick-like layout
        box = layout.box()
        col = box.column(align=True)

        # Add the third button (n)
        col.operator("object.operator_1", text="n")

        # Add the second row for the e and w buttons
        row = col.row(align=True)
        row.operator("object.operator_2", text="w")
        row.operator("object.operator_3", text="e")

        # Add the first button (s)
        col.operator("object.operator_4", text="s")
        row = col.row(align=True)
        row.operator("object.operator_5", text="z+")
        row.operator("object.operator_6", text="z-")
        col.operator("object.operator_7", text="delete")
        
        
        layout.label(text="Set Material:")
        layout.prop(context.scene, "my_text3", text="")
        layout.operator("object.print_text_operator3", text="Apply Material")
        
        
class MyTickButton1(bpy.types.Panel):
    global pesting
    """
    Creates a Panel in the sidebar.
    """
    bl_label = "My Bool Panel"
    bl_idname = "VIEW3D_PT_my_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "My Addon"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
#        object = context.object

        # Draw a toggle button
        layout.prop(scene, "pesting_property", text="Drawing")

        # Check the value of the toggle property
        if scene.pesting_property:
            change_Drawing_Mode("True")
            layout.label(text="Drawing is ON")
        else:
            change_Drawing_Mode("False")
            layout.label(text="Drawing is OFF")
            
        # Draw a toggle button
        layout.prop(scene, "half_step_property", text="Half Step")

        # Check the value of the toggle property
        if scene.half_step_property:
            half_Steps("True")
            layout.label(text="Half_Step is ON")

        else:
            half_Steps("False")
            layout.label(text="Half_Step is OFF")
            
        # layout.operator("object.operator_7", text="refrash")

class MyOperator1(bpy.types.Operator):
    bl_idname = "object.operator_1"
    bl_label = "Operator 1"

    def execute(self, context):
        n()
        self.report({'INFO'}, "Button N")
        return {'FINISHED'}
class MyOperator2(bpy.types.Operator):
    bl_idname = "object.operator_2"
    bl_label = "Operator 2"

    def execute(self, context):
        w()
        self.report({'INFO'}, "Button 4 W")
        return {'FINISHED'}
class MyOperator3(bpy.types.Operator):
    bl_idname = "object.operator_3"
    bl_label = "Operator 3"

    def execute(self, context):
        e()
        self.report({'INFO'}, "Button E")
        return {'FINISHED'}
class MyOperator4(bpy.types.Operator):
    bl_idname = "object.operator_4"
    bl_label = "Operator 4"

    def execute(self, context):
        s()
        self.report({'INFO'}, "Button S")
        return {'FINISHED'}
class MyOperator5(bpy.types.Operator):
    bl_idname = "object.operator_5"
    bl_label = "Operator 5"

    def execute(self, context):
        z_plus()
        self.report({'INFO'}, "z+")
        return {'FINISHED'}
    
class MyOperator6(bpy.types.Operator):
    bl_idname = "object.operator_6"
    bl_label = "Operator 6"

    def execute(self, context):
        z_minus()
        self.report({'INFO'}, "z-")
        return {'FINISHED'}
    
class MyOperator7(bpy.types.Operator):
    bl_idname = "object.operator_7"
    bl_label = "Operator 7"

    def execute(self, context):
        delete()
        self.report({'INFO'}, "delete")
        return {'FINISHED'}
    
class textAssignOperator(bpy.types.Operator):
    """
    Operator to print the entered text.
    """
    bl_idname = "object.print_text_operator"
    bl_label = "Print Text"
    def execute(self, context):
        scene = context.scene
        print("Text 1:", scene.my_text1)
        objects_name = str(scene.my_text1)
        set_objects(objects_name)
        return {'FINISHED'}
    
class textAssignOperator2(bpy.types.Operator):
    global unit_length_given
    """
    Operator to print the entered text.
    """
    bl_idname = "object.print_text_operator2"
    bl_label = "Print Text"
    def execute(self, context):
        global unit_length_given
        scene = context.scene
        print("Text 1:", scene.my_text2)
        unit_length_given = float(scene.my_text2)
        return {'FINISHED'}
    
class textAssignOperator3(bpy.types.Operator):
    global unit_length_given
    """
    Operator to print the entered text.
    """
    bl_idname = "object.print_text_operator3"
    bl_label = "Print Text"
    def execute(self, context):
        global unit_length_given
        scene = context.scene
        print("Text 1:", scene.my_text3)
        assignMaterial_to_Selected(str(scene.my_text3))
        return {'FINISHED'}
    
class textAssignOperator4(bpy.types.Operator):
    global unit_length_given
    """
    Operator to print the entered text.
    """
    bl_idname = "object.print_text_operator4"
    bl_label = "Print Text"
    def execute(self, context):
        global unit_length_given
        scene = context.scene
        reset_dir(scene.my_text4)
        print("Text 1:", scene.my_text4)
        return {'FINISHED'}



classes = (MyAddOnPanel1, MyOperator1, MyOperator2, MyOperator3, MyOperator4, MyOperator5, MyOperator6, MyOperator7, MyTickButton1, textAssignOperator, textAssignOperator2, textAssignOperator3, textAssignOperator4)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.my_text1 = bpy.props.StringProperty()
    bpy.types.Scene.my_text2 = bpy.props.StringProperty()
    bpy.types.Scene.my_text3 = bpy.props.StringProperty()
    bpy.types.Scene.my_text4 = bpy.props.StringProperty()
    bpy.types.Scene.pesting_property = bpy.props.BoolProperty(default=True)
    bpy.types.Scene.half_step_property = bpy.props.BoolProperty(default=False)
     

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_text1
    del bpy.types.Scene.my_text2
    del bpy.types.Scene.my_text3
    del bpy.types.Scene.my_text4
    del bpy.types.Scene.pesting_property
    del bpy.types.Scene.half_step_property


if __name__ == "__main__":
    register()

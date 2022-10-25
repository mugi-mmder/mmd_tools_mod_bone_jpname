# Copyright (c) 2022 mugi
import bpy

from bpy.types import Panel

translat = bpy.app.translations



class BONE_OT_mmdtools_bone_jpname_all_overwrite(bpy.types.Operator):
    bl_idname = "object.mmd_bone_jp_name_all_overwrite"
    bl_label = "ボーン名から取得"
    bl_description = "mmdtoolsの全てのJPnameをボーン名から取得"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if (bpy.context.active_bone):
            return True
        elif (bpy.context.active_pose_bone):
            return True
        elif (bpy.context.active_object.type == 'ARMATURE'):
            return True
        
        return False

    def execute(self, context):
        act_p_bones = bpy.context.active_object.pose.bones
        print("=========  act_p_bones  =========")
        print(act_p_bones)

        for p_bone in act_p_bones:
            mmd_bone = p_bone.mmd_bone

            print("=========  p_bone  =========")
            print("len===",len(mmd_bone.name_j),"name======",p_bone.name)
            # print("_dummy_" in p_bone.name or "_shadow_" in p_bone.name)
            if not ("_dummy_" in p_bone.name or "_shadow_" in p_bone.name): #_dummy_&_shadow_は無視

                if (p_bone.name.endswith(".L")):
                    boneLRname = "左" + p_bone.name[0:-2]
                    # print(p_bone.name.endswith(".L"),"==書き換え＝＝",p_bone.name,"--->",boneLRname)

                elif(p_bone.name.endswith(".R")):
                    boneLRname = "右" + p_bone.name[0:-2]
                    # print(p_bone.name.endswith(".R"),"==書き換え＝＝",p_bone.name,"--->",boneLRname)
                else:
                    boneLRname = p_bone.name
                mmd_bone.name_j = boneLRname
                print(" mmd_bone.name_j  --->",mmd_bone.name_j)


        self.report({'INFO'}, "mmdtoolsの和名をボーン名から取得") 
        return {'FINISHED'}

    def invoke(self, context, event):  # 確認メッセージ表示
        wm = context.window_manager

        return wm.invoke_confirm(self, event)



class BONE_OT_mmdtools_bone_Engname_all_clear(bpy.types.Operator):
    bl_idname = "object.mmd_bone_eng_name_all_clear"
    bl_label = "英名を全て空に"
    bl_description = "mmdtoolsの全てのEng_nameを空に"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if (context.active_bone):
            return True
        elif (context.active_pose_bone):
            return True
        elif (context.active_object.type == 'ARMATURE'):
            return True
        
        return False

    def execute(self, context):
        act_p_bones = bpy.context.active_object.pose.bones

        print("=========  act_p_bones  =========")
        print(act_p_bones)

        for p_bone in act_p_bones:
            mmd_bone = p_bone.mmd_bone

            if not ("_dummy_" in p_bone.name or "_shadow_" in p_bone.name): #_dummy_&_shadow_は無視
                mmd_bone.name_e = ""                                        #英名欄に空を入れる
                # print(p_bone.name,"mmd_bone.name_e  --->",mmd_bone.name_e)
        self.report({'INFO'}, "mmdtoolsの英名を全て空に") 
        return {'FINISHED'}

    def invoke(self, context, event):  # 確認メッセージ表示
        wm = context.window_manager

        return wm.invoke_confirm(self, event)




class BONE_OT_mmdtools_bone_jpname_all_clear(bpy.types.Operator):
    bl_idname = "object.mmd_bone_jp_name_all_clear"
    bl_label = "和名を全て空に"
    bl_description = "mmdtoolsの全てのJP_nameを空に"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if (bpy.context.active_bone):
            return True
        elif (bpy.context.active_pose_bone):
            return True
        elif (bpy.context.active_object.type == 'ARMATURE'):
            return True
        
        return False

    def execute(self, context):
        act_p_bones = bpy.context.active_object.pose.bones

        print("=========  act_p_bones  =========")
        print(act_p_bones)

        for p_bone in act_p_bones:
            mmd_bone = p_bone.mmd_bone

            if not ("_dummy_" in p_bone.name or "_shadow_" in p_bone.name): #_dummy_&_shadow_は無視
                mmd_bone.name_j = ""                                        #和名欄に空を入れる
                # print(p_bone.name,"mmd_bone.name_j  --->",mmd_bone.name_j)
        self.report({'INFO'}, "mmdtoolsの和名を全て空に") 
        return {'FINISHED'}
        
    def invoke(self, context, event):  # 確認メッセージ表示
        wm = context.window_manager

        return wm.invoke_confirm(self, event)


class BONE_PT_modpanel_bone_jpname(Panel):
    bl_idname = "BONE_PT_mmdtools_modpanel_bone_jpname"
    bl_label = "mmdtools_mod_bone_jpname"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "bone"

    @classmethod
    def poll(cls, context):
        return bpy.context.active_bone

    def draw(self, context):
        act_p_bones = bpy.context.active_object.pose.bones
        act_bone = act_p_bones.get(bpy.context.active_bone.name, None)
        
        if act_bone == None:
            return
        act_mmd_bone = act_bone.mmd_bone
        layout = self.layout

        col = layout.column()
        col.prop(act_mmd_bone, "name_j")
        col.prop(act_mmd_bone, "name_e")

        col = layout.column(align=True)
        row = col.row(align=True)
        row.operator(BONE_OT_mmdtools_bone_jpname_all_overwrite.bl_idname, text = translat.pgettext("JP_name_all_overwrite"))
        row = col.row(align=True)
        row.operator(BONE_OT_mmdtools_bone_jpname_all_clear.bl_idname, text = translat.pgettext("JP_name_all_clear"))
        row.separator()
        row.operator(BONE_OT_mmdtools_bone_Engname_all_clear.bl_idname, text = translat.pgettext("Eng_name_all_clear"))

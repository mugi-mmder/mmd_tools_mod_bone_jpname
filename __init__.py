# Copyright (c) 2022 mugi
import bpy
from .operator import BONE_OT_mmdtools_bone_jpname_all_overwrite,BONE_OT_mmdtools_bone_jpname_all_clear,\
                      BONE_OT_mmdtools_bone_Engname_all_clear,BONE_PT_modpanel_bone_jpname

bl_info = {
    "name": "mmdtools JPname overwrite",
    "author": "mugi",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "location": "Properties > bone",
    "description": "mmdtools JPname overwrite.",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "User Interface"
}

classes = (
    # コレクションクラスのインポートの順番に注意
    BONE_OT_mmdtools_bone_jpname_all_overwrite,
    BONE_OT_mmdtools_bone_jpname_all_clear,
    BONE_OT_mmdtools_bone_Engname_all_clear,
    BONE_PT_modpanel_bone_jpname,
     )

# 翻訳用辞書
translation_dict = {
    "en_US" :
        {("*", "JP_name_all_overwrite") : "JP_name_all_overwrite",
         ("*", "JP_name_all_clear") : "JP_name_all_clear",
         ("*", "Eng_name_all_clear") : "Eng_name_all_clear",
        },
    "ja_JP" :
        {("*", "JP_name_all_overwrite") : "全てのボーンの和名取得",
         ("*", "JP_name_all_clear") : "和名を全て空に",
         ("*", "Eng_name_all_clear") : "英名を全て空に",
        },
}


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.app.translations.register(__name__, translation_dict)   # 辞書の登録



def unregister():
    bpy.app.translations.unregister(__name__)   # 辞書の削除
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()

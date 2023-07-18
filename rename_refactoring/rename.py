from .rename_method import *
from .rename_class import *
from name_smells.Types import *

def rename(type,file_path, class_name, method_name, new_method_name):
    if type==Types.Method:
        rename_method(file_path, class_name, method_name, new_method_name)
    if type==Types.Class:
        rename_class(file_path, class_name, method_name, new_method_name)
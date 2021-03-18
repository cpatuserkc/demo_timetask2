import os
import sys
import subprocess
import requests
import datetime
import shutil
#from data.api import api_srv
#from ...data import api
#data\api\api_srv.py
from pathlib import Path
# from scripts.files.dirs import DirMgr
# from scripts.files.templates import Template, DjangoTemplate
# from .data.resources import CpaTechResource

now = datetime.datetime.now()


class AppSetup:
    #DJANGO_TEMPLATES_DIR = DjangoTemplate.BASE_DIR
    VERSION = 1.0
    
    def __init__(self,app_name=None,type_=None,env=None,frame_work="django",created=None,version=0.0,*args,**kwargs):
        self.app_name = app_name
        self.type_ = type_
        self.env = env
        self.frame_work = frame_work
        self.created = now
        self.version = AppSetup.VERSION
        print(f"new AppSetup created")
        self.display_details()


    def display_details(self):
        print(f"{self.app_name} -> {self.frame_work}")


    def get_project_dir(self):
        pass


    def install_default_req(self):
        result = subprocess.run([sys.executable, "-c", "print('ocean')"])
        # try:
        #     completed = subprocess.run([sys.executable,"-c","./installs.ps1"],
        #                                 capture_output=True,
        #                                 text=True,
        #                                 check=True)
        #     print("args",completed.args)
        #     # 0 = success, all else are errors
        #     print("return code",completed.returncode)
        #     print("stderr",completed.stderr)
        #     context_str = completed.stderr
        #     # std output
        #     print("stdout",completed.stdout)
        #     print('I got teh object! \n ',context_str)
        #     #print(completed.stdout)
        # except subprocess.CalledProcessError as ex:
        #     print(ex)


    def add_django_app(self):
        result = subprocess.run([sys.executable, "-c", "print('ocean')"])
        print(f"result of install def req {result}")


    def add_setup_defaults(self):
        base_dir = "S:\CpaTech\servers\django\dev\resources_proj"
        

    def get_default_params(self):
        default_params = {
            "program":"django",
            "dir_name":"api",
            "file_name":"view",
            "extension":".txt",
        }
        return default_params


    def get_api_files(self):
        default_params = {
            "program":"django",
            "dir_name":"api",
            "file_name":"view",
            "extension":".txt",
        }
        return default_params


    def get_default_context(self):
        default_context = {
            "Serializer":"MachLrnModel",
            "ModelName":"MachLrnModel",
            "Query_Field":"name",
            "Lookup_Field":"id",
            "View_Context_Headers":"dictionary"
        }
        return default_context


    def build_app_module(self,params=None,context=None):
        if not params:
            params = self.get_default_params()
        print(params)
        file_n = params.get("file_name")
        ext = params.get("extension")
        dir_n = params.get("dir_name")
        file_name = f"{file_n}{ext}"
        print('file name',file_name)
        template_obj = DjangoTemplate(file_name=file_name,file_extension=ext,dir_name=dir_n)
        if dir_n == "model":
            obj_model_context = self.build_data_model_obj()
        rendered_template = self.build_app_template(template_obj)
        if rendered_template != None:
            template_obj.write_file(file_name=f"{file_n}{ext}",content=rendered_template)
        
        
    def get_appsetup_obj(self):
        return AppSetup(app_name="fancyApp")


    def build_data_model_obj(self,obj_type="model"):
        model_name=None
        if self.model_name != None:
            model_name=self.model_name
        dm_obj = AppDataModel(model_name=model_name)
        required_context = dm_obj.get_required_datamodel_context()
        print(required_context)
        return dm_obj.get_api_context(data_model_obj="model")


    def build_app_template(self,template_obj=None):
        api_context = template_obj.get_api_template_context()
        print(api_context)
        template_context = self.get_default_context()
        return template_obj.render_with_context(context=template_context)
        #print('template with context -> ',rendered_template)
        


    def output_template(self,template):
        mytemp = get_template()
        my_render = render(mytemp,context)




def get_project_config():
    config = {
        "type_":"webapp",
        "env":"dev",
        "app_name":"aisrv",
        "start_folders":"start",
        "project_dir":"",
    }
    print(f'returning config {config}')
    return config
    



def add_new_project():
    config = get_project_config()
    new_app = AppSetup(type_=config['type_'],env=config['env'],app_name=config['app_name'])
    new_app.add_django_app()
    
    


if __name__ == "__main__":
    add_new_project()
    
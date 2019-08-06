import os,io
import json
project_path = os.getcwd()
this_file_path = os.path.abspath(os.path.dirname(__file__))
rasa_nlu_model_path = os.path.join(this_file_path,"slot_filling","default","all")
rasa_nlu_model_path_save = os.path.join(this_file_path,"slot_filling")
action_tmp_path = os.path.join(this_file_path,"template","action_tmp.txt")
rasa_nlu_data_path = os.path.join(this_file_path,"trainingdata","nlu_all.md")
rasa_nlu_config_yml = os.path.join(this_file_path,"nlu_config.yml")
buy_tv_story = os.path.join(this_file_path,"template","stories_buy_tv.md")
any_story = os.path.join(this_file_path,"template","stories_{}.md")
fsm_config = os.path.join(this_file_path,"template","fsm_{}.md")
fsm_transition_config = os.path.join(this_file_path,"template","transition","tran_{}.json")
fsm_state_action_config = os.path.join(this_file_path,"template","state_to_actions","actionMapper_{}.json")
fsm_edge_rule_config = os.path.join(this_file_path,"template","edge_to_rule","ruleMapper_{}.json")
story_config = os.path.join(this_file_path,"template","task_config.json")

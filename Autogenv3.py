#This is to demonstrate a simple single agent autogen

import autogen

config_list_mistral = [
    {
        'base_url': "http://localhost:1234/v1",
        "model": "mistralai_mistral-7b-instruct-v0.2",
        'api_key': "NULL"
    }
]

llm_config_mistral={
    "config_list": config_list_mistral,
}

Coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config_mistral,
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "Codes","use_docker":False,},
    llm_config=llm_config_mistral,
    system_message="""Reply TERMINATE at the end if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task=""""
You are a helpful assistant. You will understand the task, reason and act.

Write a python program to generate two numbers and sum those two numbers.

Ask user_proxy agent to run it and test it.
"""

user_proxy.initiate_chat(Coder, message=task)
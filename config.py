# Config file for tgclean

# Class for a chat group
class ChatGroup:
  def __init__(self, chatlist, delete_before_days):
    assert type(chatlist) is list;
    assert type(delete_before_days) is int;
    self.chatlist = chatlist;
    self.delete_before_days = delete_before_days;
  chatlist = [];
  delete_before_days = 1;

# API id and hash obtained during setup
tg_api_id = 1054125;
tg_api_hash = "62e934254fecb43c753975e766d5a150";

# List of chats for a group

listA = [
  "https://t.me/joinchat/RE3FvVY695c1_yLATpvzmA",
  -1001446705047
];


# List of GroupChat targets
# Taking lists as first argument and days to not delete as second

targets = [
  ChatGroup(listA, 1),
]

# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @bar_lo0o0 © Rocks
# Owner BARLO


QUEUE = {}

def add_to_queue(chat_id, songname, link, ref, type, quality):
   if chat_id in QUEUE:
      chat_queue = QUEUE[chat_id]
      chat_queue.append([songname, link, ref, type, quality])
      return int(len(chat_queue)-1)
   else:
      QUEUE[chat_id] = [[songname, link, ref, type, quality]]

def get_queue(chat_id):
   if chat_id in QUEUE:
      chat_queue = QUEUE[chat_id]
      return chat_queue
   else:
      return 0

def pop_an_item(chat_id):
   if chat_id in QUEUE:
      chat_queue = QUEUE[chat_id]
      chat_queue.pop(0)
      return 1
   else:
      return 0
      
def clear_queue(chat_id):
   if chat_id in QUEUE:
      QUEUE.pop(chat_id)
      return 1
   else:
      return 0


# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.